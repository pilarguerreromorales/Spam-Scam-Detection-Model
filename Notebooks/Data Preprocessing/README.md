# Data Preprocessing

This folder contains the notebook used to apply additional transformations to the merged dataset to prepare it for model training.

## Purpose

The preprocessing step focuses on cleaning and normalizing textual data. This ensures consistency in the dataset before passing data into machine learning models.

## Notebook

`03_preprocess_merged_data.ipynb`  
This notebook performs various text normalization techniques on the merged dataset, including:

- Replacing URLs with `[URL]`
- Replacing email addresses with `[EMAIL]`
- Replacing phone numbers with `[PHONE]`
- Replacing monetary amounts with `[MONEY]`
- Replacing general numbers with `[NUM]`
- Replacing emojis and special characters with `[EMOJI]`
- Converting all text to lowercase
- Normalizing whitespace

## Output

The cleaned dataset generated here is the one used as input for the next part of the project, which is the Generation Model..

## Notes

- This notebook assumes that the merged dataset has already been generated through the ingestion pipeline and is both named and stored as specified in that notebook.
- If needed, rerun the ingestion notebooks first to recreate the input data for this step.

