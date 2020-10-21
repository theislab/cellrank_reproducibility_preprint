# CellRank's reproducibility repository
Code to reproduce results from the CellRank manuscript. Please find the main CellRank website at [cellrank.org](https://cellrank.org) and the preprint at [bioRxiv](https://doi.org/10.1101/2020.10.19.345983).

## Where to find the data
Raw published data for the [pancreas](https://doi.org/10.1242/dev.173849), [lung](https://doi.org/10.1038/s41467-020-17358-3) and [reprogramming](https://doi.org/10.1038/s41586-018-0744-4) examples is available from the Gene Expression Omnibus (GEO) under accession codes [GSE132188](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE132188), [GSE141259](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141259) and [GSE99915](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99915), respectively. Processed data, including spliced and unspliced count abundances, is available from [figshare](https://doi.org/10.6084/m9.figshare.c.5172299). For convenience, the [pancreas](https://doi.org/10.1242/dev.173849) and [lung](https://doi.org/10.1038/s41467-020-17358-3) examples
are also available through `cellrank.datasets`.


## Where to find which analysis notebook
figure         | notebook path     
---------------| ---------------
| Fig. 1 | [notebooks/fig_1_concept/ML_2020-10-13_fig_1_concept.ipynb](notebooks/fig_1_concept/ML_2020-10-13_fig_1_concept.ipynb) |
| Fig. 2 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Fig. 3 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Fig. 4 | [notebooks/fig_4_uncertainty/ML-2020-10-17_fig_4_uncertainty.ipynb](notebooks/fig_4_uncertainty/ML-2020-10-17_fig_4_uncertainty.ipynb) and [notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb](notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb)|
| Fig. 5 | [notebooks/fig_5_benchmarking](notebooks/fig_5_benchmarking) |
| Fig. 6 | [notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb](notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb) |
| Suppl. Fig. 1 | [notebooks/suppl_fig_GPCCA/ML-2020-10-17_GPCCA_toy_example.ipynb](notebooks/suppl_fig_GPCCA/ML-2020-10-17_GPCCA_toy_example.ipynb) |
| Suppl. Fig. 2 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 3 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 4 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 5 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 6 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb)  and [notebooks/fig_5_benchmarking/palantir/ML-2020-10-17_palantir.ipynb](notebooks/fig_5_benchmarking/palantir/ML-2020-10-17_palantir.ipynb)|
| Suppl. Fig. 7 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb ) |
| Suppl. Fig. 8 | [notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb](notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb) |
| Suppl. Fig. 9 | [notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb](notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb) |
| Suppl. Fig. 10 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 11 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 12 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 13 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) |
| Suppl. Fig. 14 | [notebooks/fig_4_uncertainty/ML-2020-10-17_fig_4_uncertainty.ipynb](notebooks/fig_4_uncertainty/ML-2020-10-17_fig_4_uncertainty.ipynb) |
| Suppl. Fig. 15 | [notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb](notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb) |
| Suppl. Fig. 16 | [notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb](notebooks/suppl_fig_robustness/MK_2020-10-16_robustness.ipynb) |
| Suppl. Fig. 17 | [notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb](notebooks/fig_2_pancreas_main/ML-2020-10-14_fig_2_and_3_pancreas_main.ipynb) and [notebooks/fig_5_benchmarking/palantir/ML-2020-10-17_palantir.ipynb](notebooks/fig_5_benchmarking/palantir/ML-2020-10-17_palantir.ipynb)|
| Suppl. Fig. 18 | [notebooks/fig_5_benchmarking/fateid/MK_2020-10-17_plot_trends.ipynb](notebooks/fig_5_benchmarking/fateid/MK_2020-10-17_plot_trends.ipynb) |
| Suppl. Fig. 19 | [notebooks/fig_5_benchmarking/fateid/MK_2020-10-17_plot_trends.ipynb](notebooks/fig_5_benchmarking/fateid/MK_2020-10-17_plot_trends.ipynb) |
| Suppl. Fig. 20 | [notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_fig_memory_benchmark.ipynb](notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_fig_memory_benchmark.ipynb) |
| Suppl. Fig. 21 | [notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb](notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb) |
| Suppl. Fig. 22 | [notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb](notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb)  |
| Suppl. Fig. 23 | [notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb](notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb)  |
| Suppl. Fig. 24 | [notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb](notebooks/fig_6_lung/ML-2020-10-17_fig_6_lung.ipynb)  |
| Suppl. Fig. 25 | No notebook, microscopy results, see Online methods |
| Suppl. Table 1 | [notebooks/suppl_fig_time_benchmark/MK_2020-10-16_suppl_fig_time_benchmark.ipynb](notebooks/suppl_fig_time_benchmark/MK_2020-10-16_suppl_fig_time_benchmark.ipynb) |
| Suppl. Table 2 | [notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_fig_memory_benchmark.ipynb](notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_fig_memory_benchmark.ipynb) |
| Suppl. Table 3 | [notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_table_memory_benchmark_1_core.ipynb](notebooks/suppl_fig_memory_benchmark/MK_2020-10-16_suppl_table_memory_benchmark_1_core.ipynb) |
