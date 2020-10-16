#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict
from time import perf_counter
from math import ceil
from functools import partial
from anndata import AnnData
from typing import Callable, Optional, Union

import pickle
import gc
import scanpy as sc
import traceback
import os
os.environ['NUMBA_DISABLE_CUDA'] = "1"

import pandas as pd
import numpy as np

import scvelo as scv
import cellrank as cr

import slepc4py  # sanity check imports for CellRank
import petsc4py

CORES = 32


def timeit(func: Callable) -> Callable:
    
    def decorator(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        elapsed = perf_counter() - start
        return res, elapsed
    
    return decorator


def create_kernel(adata: AnnData, backward: bool = False) -> cr.tl.kernels.Kernel:
    vk = cr.tl.kernels.VelocityKernel(adata, backward=backward).compute_transition_matrix(
        mode="deterministic", show_progress_bar=False,
        softmax_scale=4, n_jobs=16,
        backend="loky"
    )
    ck = cr.tl.kernels.ConnectivityKernel(adata, backward=backward).compute_transition_matrix()

    return (0.8 * vk + 0.2 * ck).compute_transition_matrix()
    
    
def get_split(dir: str) -> dict:
    dfs = {}
    split_root = Path(dir)

    for split in os.listdir(split_root):
        if split.endswith('.csv'):
            size = int(split[:-4].split('_')[1])
            dfs[size] = pd.read_csv(split_root / split, index_col=0)

    return {k: dfs[k] for k in sorted(dfs.keys()) if k != 104679}


def _benchmark_cellrank_or_dynamo(adata: AnnData, dfs, Estimator: Union[str, type(cr.tl.estimators.BaseEstimator)],
                                  n_states: int = 3, path: str = "",
                                  dynamo_roots: Optional[str] = None,
                                  backward=False) -> defaultdict:
    res = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    if backward:
        n_states = 1
    
    if Estimator == "dynamo":
        assert dynamo_roots is not None, "Supply path to dynamo root cells."
        with open(dynamo_roots, "rb") as fin:
            roots = pickle.load(fin)
    
    for size, split in dfs.items():
        for j, col in enumerate(split.columns):
            e, ixs, bdata, k = None, None, None, None
            try:
                print(f"Subsetting data to `{size}`, split `{col}`.")
                ixs = split[col].values
                bdata = adata[ixs].copy()                    
                
                assert bdata.n_obs == size

                if Estimator is cr.tl.estimators.GPCCA:
                    assert bdata.obsp["distances"].shape == (size, size)
                    assert bdata.obsp["connectivities"].shape == (size, size)
                    assert bdata.uns["velocity_graph"].shape == (size, size)
                    assert bdata.uns["velocity_graph_neg"].shape == (size, size)

                    print("Recomputing neighbors")
                    scv.pp.neighbors(bdata)

                    print("Recomputing velocity graph")
                    _, vtime = velocity_graph(bdata, mode_neighbors='connectivities', n_recurse_neighbors=0)

                    print("Computing kernel")
                    k, ktime = create_kernel(bdata, backward=backward)

                    e = Estimator(k)
                    
                    compute_eig = timeit(e.compute_eigendecomposition)
                    compute_schur = timeit(e.compute_schur)
                    compute_macro = timeit(e.compute_macrostates)
                    compute_ap = timeit(e.compute_absorption_probabilities)

                    if backward:
                        print("Computing Eigendecomposition")
                        _, res[size][col]['eig_time'] = compute_eig(only_evals=False)
                    
                    print("Computing Schur decomposition")
                    try:
                        _, dectime = compute_schur(n_components=n_states + 1)
                    except:
                        _, dectime = compute_schur(n_components=n_states + 2)
                    
                    print("Computing macrostates")
                    try:
                        _, macrotime = compute_macro(n_states=n_states)
                    except:
                        _, macrotime = compute_macro(n_states=n_states + 1)
                    
                    if backward:
                        e.set_terminal_states_from_macrostates(n_cells=int(ceil(size // 100)))
                        res[size][col]['dec_time'] = dectime
                        res[size][col]['meta_time'] = macrotime
                        res[size][col]['root_states'] = e.terminal_states.copy()
                        res[size][col]['root_states_probs'] = e.terminal_states_probabilities.copy()
                        save_results(res, path)
                        continue

                    e.set_terminal_states_from_macrostates(n_cells=int(ceil(size // 100)))
                    print("Computing absorption probabilities")
                    _, aptime = compute_ap(use_petsc=True, solver="gmres",
                                           show_progress_bar=False,
                                           n_jobs=CORES, backend="loky")
                   
                    lin_drivers = e.compute_lineage_drivers(return_drivers=True)
                    
                    res[size][col]['main_states'] = e.terminal_states.copy()
                    res[size][col]['main_states_probs'] = e.terminal_states_probabilities.copy()
                    res[size][col]['lin_probs'] = e.absorption_probabilities.X.copy()
                    res[size][col]['lin_drivers'] = lin_drivers.copy()
                    
                    res[size][col]['vg_time'] = vtime
                    res[size][col]['k_time'] = ktime
                    res[size][col]['dec_time'] = dectime
                    res[size][col]['meta_time'] = macrotime
                    res[size][col]['ap_time'] = aptime
                    
                elif Estimator == 'dynamo':
                    import dynamo as dyn
                    
                    print("Fetching root states")
                    init_cells = roots[size][col]["root_states"]
                    assert np.all(init_cells.index == bdata.obs_names), "Index mismatch."
                    
                    print("Preprocessing and clustering")
                    dyn.pp.recipe_monocle(bdata, keep_filtered_cells=False, keep_filtered_genes=False)
                    sc.pp.neighbors(bdata, n_neighbors=30)
                    sc.tl.louvain(bdata)
                    
                    # after preprocessing, we might've gotten rid of some states
                    init_cells = init_cells[list(set(init_cells.index) & set(bdata.obs_names))]
                    # should be only 1 category, just in case
                    init_cells = list(np.where(init_cells == init_cells.cat.categories[0])[0])
                    
                    print("Calculating moments")
                    _, res[size][col]['mom'] = moments(bdata)
                    print("Calculating dynamics")
                    _, res[size][col]['dyn'] = dynamics(bdata, cores=CORES)

                    print("Dimnesionality reduction")
                    dyn.tl.reduceDimension(bdata, basis='umap', enforce=True)
                    
                    print("Calculating velocities")
                    _, res[size][col]['velo'] = velocities(bdata)
                    
                    print("Calculating vector field")
                    _, res[size][col]['VF'] = VF(bdata, basis='umap', pot_curl_div=False, cores=CORES, MaxIter=100)
                    
                    print("Calculating fates")
                    _, res[size][col]['fate'] = fate(bdata, init_cells, basis='umap',
                                                     # cores are not yet implemented
                                                     direction='forward', cores=1)

                    print("Calculating fate bias")
                    _, res[size][col]['fate_bias'] = fate_bias(bdata, "louvain", inds=None, dist_threshold=10, cores=CORES)
                    
                    if False:  # don't need these
                        print("Calculating topography")
                        _, res[size][col]['topo'] = topo(bdata, basis='umap')

                        print("Calculating ddhodge")
                        _, res[size][col]['ddhodge'] = ddhodge(bdata, basis='umap', cores=CORES)

                        func = bdata.uns["VecFld"]['VecFld2D'].func
                        x_lim, y_lim = bdata.uns["VecFld"]['xlim'], bdata.uns["VecFld"]['ylim']

                        try:
                            print("Calculating potential (Ao)")
                            _, res[size][col]['Pot_Ao'] = Pot_Ao(bdata, Function=func,
                                                                 x_lim=bdata.uns["VecFld"]['xlim'],
                                                                 y_lim=bdata.uns["VecFld"]['ylim'])
                        except Exception as e:
                            print(f"Failed: {e}")
                            res[size][col]['Pot_Ao'] = np.nan

                        try:
                            print("Calculating potential (Bhattacharya)")
                            _, res[size][col]['Pot_bhatt'] = Pot_bhatt(bdata, Function=func,
                                                                       x_lim=bdata.uns["VecFld"]['xlim'],
                                                                       y_lim=bdata.uns["VecFld"]['ylim'])
                        except Exception as e:
                            print(f"Failed: {e}")
                            res[size][col]['Pot_bhatt'] = np.nan
                else:
                    raise RuntimeError(f"Invalid Estimator: `{estimator}`.")
                    
            except Exception as exc:
                print(f"Unable to run `{Estimator}` estimator, size `{size}`, split `{col}`. Reason: `{exc}`.")
                print(traceback.format_exc())
            
            save_results(res, path)
                
            del bdata, ixs, k, e
            gc.collect()
            
    return res
    
    
def benchmark_gpcca(adata: AnnData, dfs: dict, path: str):
    path = str(path)
    res_gpcca = _benchmark_cellrank_or_dynamo(adata, dfs, cr.tl.estimators.GPCCA, path=path)
    save_results(res_gpcca, path)

    
def benchmark_gpcca_bwd(adata: AnnData, dfs: dict, path: str):
    path = str(path)
    res_gpcca = _benchmark_cellrank_or_dynamo(adata, dfs, cr.tl.estimators.GPCCA, path=path, backward=True)
    save_results(res_gpcca, path)

    
def benchmark_dynamo(adata: AnnData, dfs: dict, path: str, dynamo_roots):
    path = str(path)
    res_dynamo = _benchmark_cellrank_or_dynamo(adata, dfs, "dynamo", path=path, dynamo_roots=dynamo_roots)
    save_results(res_dynamo, path)
    
    
def save_results(data: dict, path: str):
    data = {k1: {k2: {k3: v3 for k3, v3 in v2.items()} for k2, v2 in v1.items()} for k1, v1 in data.items()}
    with open(path, 'wb') as fout:
        pickle.dump(data, fout)
    
    
# CellRank functions
velocity_graph = timeit(scv.tl.velocity_graph)
create_kernel = timeit(create_kernel)


try:
    import dynamo as dyn
    
    moments = timeit(dyn.tl.moments)
    dynamics = timeit(dyn.tl.dynamics)
    velocities = timeit(dyn.tl.cell_velocities)
    VF = timeit(dyn.vf.VectorField)
    fate = timeit(dyn.pd.fate)
    fate_bias = timeit(dyn.pd.fate_bias)

    # unused dynamo functions
    topo = timeit(dyn.vf.topography)
    ddhodge = timeit(dyn.ext.ddhodge)
    Pot_Ao = timeit(partial(dyn.vf.Potential, method='Ao'))
    Pot_bhatt = timeit(partial(dyn.vf.Potential, method='Bhattacharya'))
except ImportError:
    print("No dynamo version found")