import os
import pandas as pd

# Folder containing all CSV files
DATA_FOLDER = "data/raw"

# Get all CSV files
csv_files = sorted([file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")])

print("=" * 80)
print("DATA INGESTION STARTED")
print("=" * 80)

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 80)
    print(f"FILE : {file}")
    print("=" * 80)

    df = pd.read_csv(file_path)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

print("\n")
print("=" * 80)
print("ALL FILES LOADED SUCCESSFULLY")
print("=" * 80)
print("\n")
print("="*80)
print("FUND MASTER EXPLORATION")
print("="*80)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses")
print(fund_master["fund_house"].unique())

print("\nUnique Categories")
print(fund_master["category"].unique())

print("\nUnique Sub Categories")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories")
print(fund_master["risk_category"].unique())

print("\nTotal Fund Houses :", fund_master["fund_house"].nunique())
print("Total Categories :", fund_master["category"].nunique())
print("Total Sub Categories :", fund_master["sub_category"].nunique())
print("Total Risk Categories :", fund_master["risk_category"].nunique())