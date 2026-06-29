import os
import sqlite3
import pandas as pd

DATABASE_NAME = "mutual_funds.db"
DATA_FOLDER = "data/raw"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

print("=" * 80)
print("DATABASE CREATED SUCCESSFULLY")
print("=" * 80)

csv_files = sorted(
    [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]
)

for file in csv_files:
    file_path = os.path.join(DATA_FOLDER, file)
    table_name = file.replace(".csv", "")

    print(f"\nLoading {file}")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )

    print(f"Table Created : {table_name}")

print("\n")
print("=" * 80)
print("DATABASE VERIFICATION")
print("=" * 80)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')

    count = cursor.fetchone()[0]

    print(f"{table_name:<35} {count:>10} rows")

connection.close()

print("\nDatabase Closed Successfully")