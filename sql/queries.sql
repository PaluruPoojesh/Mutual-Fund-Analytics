import sqlite3
import pandas as pd

DATABASE = "mutual_funds.db"

conn = sqlite3.connect(DATABASE)

queries = {
    "Total Funds":
        "SELECT COUNT(*) AS Total_Funds FROM '01_fund_master';",

    "Fund Houses":
        """
        SELECT fund_house,
               COUNT(*) AS Number_of_Funds
        FROM '01_fund_master'
        GROUP BY fund_house
        ORDER BY Number_of_Funds DESC;
        """,

    "Average Expense Ratio":
        """
        SELECT
        ROUND(AVG(expense_ratio),2)
        AS Average_Expense_Ratio
        FROM '01_fund_master';
        """,

    "Risk Distribution":
        """
        SELECT risk_category,
               COUNT(*) AS Count
        FROM '01_fund_master'
        GROUP BY risk_category;
        """,

    "Top 10 AUM":
        """
        SELECT *
        FROM '03_aum_by_fund_house'
        ORDER BY aum_cr DESC
        LIMIT 10;
        """
}

print("=" * 80)
print("SQL ANALYSIS")
print("=" * 80)

for title, query in queries.items():

    print("\n")
    print("=" * 50)
    print(title)
    print("=" * 50)

    df = pd.read_sql_query(query, conn)

    print(df)

conn.close()

print("\nSQL Analysis Completed")