# cellrank_reproducibility
Code to reproduce results from the CellRank manuscript

# Code of conduct
Let's establish a couple of guidelines that make sure this repo is clean and usable by others.

## Notebooks, data and figures
We split these three at the top level of the repository to have one `data`, one `figures` and one `notebooks` folder. These have sub-folders that relate to specific figures/datasets. 

### Notebooks
- save under `~/notebooks/fig_X_title/` or  `~/notebooks/suppl_fig_X_title/`
- naming conventions: call the notebook `DATE_INITIALS_fig_X_title` or`DATE_INITIALS_suppl_fig_X_title`
- structure notebooks by sections, give each section an imperative title (e.g. "Identify initial states", "Import data"), capitalize titles. 
- define a **data path** and a **figure path** at the beginning of each notebook. These define where the data is read from and where figures are written to
- use **relative paths**
- print **all relevant** package versions towards the beginning of each notebook
- make sure your notebok is runnable, **from top to bottom**, by someone who only has the information and **the explanations** given in the notebook. If external data is needed **than comment on this** and say where it is. 

### Data
Many notebooks will use the same data, so we **do not** spit up the data folder by figures.
- Save data under `~/data/pancreas/`, `~/data/lung`, `~/data/benchmarking` etc. 
- import the pancreas data using `cr.datasets`

### Figures
Figures are, as the name conveys, figure specific, so we save them in folders separated by the figure name
- Write figures to `~figures/fig_X_title/` or `~figures/suppl_fig_X_title/`
- If you are not sure about the **number of the figure you're producing** then check in the manuscript!

## Anything else?
Feel free to add. 


