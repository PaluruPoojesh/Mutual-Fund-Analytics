import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

top = df.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10)

with open("reports/Financial_Report.txt","w") as f:

    f.write("FINANCIAL ANALYTICS REPORT\n")
    f.write("="*60+"\n\n")

    f.write(f"Total Schemes : {len(df)}\n")

    f.write(f"Average Alpha : {round(df['alpha'].mean(),2)}\n")

    f.write(f"Average Beta : {round(df['beta'].mean(),2)}\n")

    f.write(f"Average Sharpe : {round(df['sharpe_ratio'].mean(),2)}\n")

    f.write(f"Average Expense Ratio : {round(df['expense_ratio_pct'].mean(),2)}\n\n")

    f.write("Top 10 Performing Funds\n\n")

    f.write(
        top[[
            "scheme_name",
            "return_5yr_pct",
            "alpha",
            "beta"
        ]].to_string(index=False)
    )  





      -

print("Financial Report Generated Successfully")