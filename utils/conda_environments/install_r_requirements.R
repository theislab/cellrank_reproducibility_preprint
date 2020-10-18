#!/usr/bin/env Rscript

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

if (!requireNamespace("devtools", quietly = TRUE))
    install.packages("devtools")

# FateID
devtools::install_github("dgrun/FateID")
devtools::install_github("dgrun/RaceID")
BiocManager::install("destiny")

# STEMNET
devtools::install_git("https://git.embl.de/velten/STEMNET/")

# Utilities
install.packages("SparseM", repos="https://cloud.r-project.org")
install.packages("Matrix", repos="https://cloud.r-project.org")
install.packages("R.utils", repos="https://cloud.r-project.org")
install.packages("peakRAM", repos="https://cloud.r-project.org")
