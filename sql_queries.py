import sqlite3
import pandas as pd

conn = sqlite3.connect("mutual_funds.db")

queries = {

    "Total Mutual Fund Schemes":
    """
    SELECT COUNT(*) AS Total_Funds
    FROM "01_fund_master";
    """,

    "Fund House Distribution":
    """
    SELECT
        fund_house,
        COUNT(*) AS Total_Schemes
    FROM "01_fund_master"
    GROUP BY fund_house
    ORDER BY Total_Schemes DESC;
    """,

    "Average Expense Ratio":
    """
    SELECT
        ROUND(AVG(expense_ratio_pct),2) AS Avg_Expense_Ratio
    FROM "01_fund_master";
    """,

    "Risk Category Distribution":
    """
    SELECT
        risk_category,
        COUNT(*) AS Total
    FROM "01_fund_master"
    GROUP BY risk_category;
    """,

    "Category Distribution":
    """
    SELECT
        category,
        COUNT(*) AS Total
    FROM "01_fund_master"
    GROUP BY category;
    """,

    "Top 10 Fund Houses by AUM":
    """
    SELECT
        fund_house,
        aum_lakh_crore
    FROM "03_aum_by_fund_house"
    ORDER BY aum_lakh_crore DESC
    LIMIT 10;
    """,

    "Top 10 Performing Schemes (5 Year Return)":
    """
    SELECT
        scheme_name,
        return_5yr_pct,
        alpha,
        sharpe_ratio
    FROM "07_scheme_performance"
    ORDER BY return_5yr_pct DESC
    LIMIT 10;
    """,

    "Average Alpha Beta Sharpe":
    """
    SELECT
        ROUND(AVG(alpha),2) AS Avg_Alpha,
        ROUND(AVG(beta),2) AS Avg_Beta,
        ROUND(AVG(sharpe_ratio),2) AS Avg_Sharpe
    FROM "07_scheme_performance";
    """,

    "Top 10 Stocks by Portfolio Weight":
    """
    SELECT
        stock_name,
        sector,
        weight_pct
    FROM "09_portfolio_holdings"
    ORDER BY weight_pct DESC
    LIMIT 10;
    """,

    "Benchmark Index Summary":
    """
    SELECT
        index_name,
        ROUND(AVG(close_value),2) AS Avg_Close
    FROM "10_benchmark_indices"
    GROUP BY index_name;
    """
}

print("="*90)
print("SQL ANALYSIS REPORT")
print("="*90)

for title, query in queries.items():

    print("\n")
    print("="*90)
    print(title)
    print("="*90)

    df = pd.read_sql_query(query, conn)

    print(df)

conn.close()

print("\n")
print("="*90)
print("SQL ANALYSIS COMPLETED SUCCESSFULLY")
print("="*90)