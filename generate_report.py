import os
import pandas as pd

os.makedirs("reports", exist_ok=True)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

report = []

report.append("MUTUAL FUND ANALYTICS - EDA REPORT")
report.append("="*60)

report.append(f"\nTotal Mutual Funds : {len(fund_master)}")

report.append(f"Total Fund Houses : {fund_master['fund_house'].nunique()}")

report.append(f"Total Categories : {fund_master['category'].nunique()}")

report.append(f"Total Sub Categories : {fund_master['sub_category'].nunique()}")

report.append(f"Average Expense Ratio : {round(fund_master['expense_ratio_pct'].mean(),2)} %")

report.append("\nTop Performing Fund")

top = performance.sort_values(
    "return_5yr_pct",
    ascending=False
).iloc[0]

report.append(f"Scheme : {top['scheme_name']}")

report.append(f"5 Year Return : {top['return_5yr_pct']} %")

report.append(f"Fund House : {top['fund_house']}")

report.append("\nHighest Portfolio Allocation Sector")

sector = portfolio.groupby("sector")["weight_pct"].sum()

sector = sector.sort_values(ascending=False)

report.append(sector.head(5).to_string())

with open("reports/EDA_Report.txt","w") as f:

    for line in report:

        f.write(str(line))

        f.write("\n")

print("="*70)
print("EDA REPORT GENERATED")
print("="*70)