How to run the memory benchmarks
--------------------------------

From the current directory, simply run
```bash
bash run_all.shape <METHOD> <NUMBER_OF_JOBS>
```

Where `<MEHOD>` is one of: gpcca, palanir, fateid, stemnet.
Note that `<NUMBER_OF_JOBS>` only affects CellRank and Palantir.
It was set to either `32` for multi-core benchmark or `1` for single-core.