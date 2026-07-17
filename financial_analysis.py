import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("reports/charts", exist_ok=True)

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("="*80)
print("FINANCIAL ANALYSIS")
print("="*80)

print("\nTop 10 Funds by 5-Year Return")

top = df.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10)

print(top[[
    "scheme_name",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio"
]])

# -----------------------------
# Chart 1
# -----------------------------

plt.figure(figsize=(12,6))

plt.bar(
    top["scheme_name"],
    top["return_5yr_pct"]
)

plt.xticks(rotation=90)

plt.title("Top 10 Funds by 5-Year Return")

plt.tight_layout()

plt.savefig("reports/charts/top10_return.png")

plt.close()

print("Chart Saved")

# -----------------------------
# Average Metrics
# -----------------------------

print("\nAverage Financial Metrics")

metrics = df[[
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "expense_ratio_pct"
]].mean()

print(metrics)

# -----------------------------
# Top Sharpe Ratio
# -----------------------------

print("\nTop Sharpe Ratio")

sharpe = df.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10)

print(sharpe[[
    "scheme_name",
    "sharpe_ratio"
]])

plt.figure(figsize=(12,6))

plt.bar(
    sharpe["scheme_name"],
    sharpe["sharpe_ratio"]
)

plt.xticks(rotation=90)

plt.title("Top Sharpe Ratio Funds")

plt.tight_layout()

plt.savefig("reports/charts/top_sharpe.png")

plt.close()

print("\nAnalysis Completed")