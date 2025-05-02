# Data Folder

This folder contains the original data files used throughout the project.

## Structure

All files are currently stored directly in this folder and all generated files will be added alongside them without the usage of `raw/` or `processed` subfolders as we are currently not following this structure.

## Original Datasets

The following files are the original datasets used in this project:

- `filtered_data.csv`
- `fraud_detect.csv`
- `sms_spam.csv`
- `spam.csv`
- `telegram_spam.csv`

These files were manually downloaded and renamed following the instructions in the data ingestion notebook (see below).

## Data Ingestion

For detailed instructions on how to manually download the original datasets from their sources, please refer to the ingestion notebook:

[`Notebooks/Data Ingestion/01_data_download.ipynb`](../Notebooks/Data%20Ingestion/01_data_download.ipynb)

This notebook includes:
- Links to data sources
- Download instructions
- Renaming instructions

## Notes

- The final merged dataset is generated during preprocessing but is **not included** in the repository. You can recreate it by running the notebook [`Notebooks/Data Ingestion/02_explore_and_merge.ipynb`](../Notebooks/Data%20Ingestion/02_explore_and_merge.ipynb).

