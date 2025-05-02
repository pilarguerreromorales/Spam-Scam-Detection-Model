# Dataset Ingestion Notebooks

This folder contains two notebooks related to the ingestion and preparation of the original datasets used in the project. The output of this stage is a single cleaned and merged dataset that serves as the main dataset for subsequent stages in the project.

## Contents
### `01_datasets_download.ipynb`
- Lists the original data sources (including links).
- Provides instructions on how to manually download and rename each dataset.
- Datasets were downloaded, renamed, and saved manually into the [`data/`](../../data/) folder so they are ready to use.
- This process was done by hand so there is no automated code.

### `02_explore_and_merge_datasets.ipynb`
- Used to perform initial exploration and data checks on the raw datasets.
- Applies light cleaning (e.g., standardizing column names, removing unnecessary columns).
- Merges the cleaned datasets into a single file, removing duplicated entries.
- **The resulting merged dataset** is used in the project, but **is not included in the repository** due to file sizes.
- To reproduce it, run this notebook after downloading the original data files, which are included in the repository.

### Output
- A cleaned and merged dataset.
- The file should be called `final_spam_dataset.csv` and stored in the `../../data/` folder for it to work properly in the following notebooks.

### Notes
- If original files are downloaded from their respective websites, be sure to follow the renaming steps instructed in notebook 01 for notebook 02 to run properly.

