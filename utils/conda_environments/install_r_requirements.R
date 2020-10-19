#!/usr/bin/env Rscript

REPOS = "https://cloud.r-project.org"


if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos=REPOS)

if (!requireNamespace("devtools", quietly = TRUE))
    install.packages("devtools", repos=REPOS)

library(devtools)
library(BiocManager)

# FateID
devtools::install_github("dgrun/FateID")
devtools::install_github("dgrun/RaceID")
BiocManager::install("destiny")

# STEMNET
devtools::install_git("https://git.embl.de/velten/STEMNET/")

# Utilities
install.packages("mgcv", repos=REPOS)
install.packages("SparseM", repos=REPOS)
install.packages("Matrix", repos=REPOS)
install.packages("R.utils", repos=REPOS)
install.packages("peakRAM", repos=REPOS)
