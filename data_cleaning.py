import os
import pandas as pd

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

csv_files = sorted(
    [file for file in os.listdir(RAW_FOLDER) if file.endswith(".csv")]
)

print("=" * 80)
print("DATA CLEANING STARTED")
print("=" * 80)

summary = []

for file in csv_files:

    file_path = os.path.join(RAW_FOLDER, file)

    df = pd.read_csv(file_path)

    original_rows = len(df)

    duplicates = df.duplicated().sum()

    missing = df.isnull().sum().sum()

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill numeric missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Fill text missing values
    text_cols = df.select_dtypes(include=["object", "string"]).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    cleaned_rows = len(df)

    output_path = os.path.join(PROCESSED_FOLDER, file)

    df.to_csv(output_path, index=False)

    summary.append([
        file,
        original_rows,
        cleaned_rows,
        duplicates,
        missing
    ])

summary_df = pd.DataFrame(
    summary,
    columns=[
        "Dataset",
        "Original Rows",
        "Cleaned Rows",
        "Duplicate Rows Removed",
        "Missing Values"
    ]
)

print("\n")
print(summary_df)

summary_df.to_csv(
    os.path.join(PROCESSED_FOLDER, "cleaning_summary.csv"),
    index=False
)

print("\nCleaning Completed Successfully")