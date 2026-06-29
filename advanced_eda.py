import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder
os.makedirs("reports/charts", exist_ok=True)

# Load datasets
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("=" * 80)
print("ADVANCED EDA")
print("=" * 80)

# ---------------------------------------------------
# Chart 1 - Top 10 Performing Funds
# ---------------------------------------------------

top10 = performance.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top10["scheme_name"],
    top10["return_5yr_pct"]
)

plt.xticks(rotation=90)

plt.title("Top 10 Performing Funds (5 Year Return)")

plt.tight_layout()

plt.savefig("reports/charts/top10_funds.png")

plt.close()

print("Top 10 Funds Chart Saved")

# ---------------------------------------------------
# Chart 2 - Alpha Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,6))

plt.hist(
    performance["alpha"],
    bins=10
)

plt.title("Alpha Distribution")

plt.tight_layout()

plt.savefig("reports/charts/alpha_distribution.png")

plt.close()

print("Alpha Chart Saved")

# ---------------------------------------------------
# Chart 3 - Sector Allocation
# ---------------------------------------------------

sector = portfolio.groupby(
    "sector"
)["weight_pct"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,7))

sector.plot(kind="bar")

plt.title("Portfolio Sector Allocation")

plt.tight_layout()

plt.savefig("reports/charts/sector_allocation.png")

plt.close()

print("Sector Allocation Saved")

# ---------------------------------------------------
# Chart 4 - Benchmark Trend
# ---------------------------------------------------

benchmark["date"] = pd.to_datetime(benchmark["date"])

benchmark = benchmark.sort_values("date")

for index_name in benchmark["index_name"].unique():

    temp = benchmark[
        benchmark["index_name"] == index_name
    ]

    plt.figure(figsize=(12,6))

    plt.plot(
        temp["date"],
        temp["close_value"]
    )

    plt.title(index_name)

    plt.tight_layout()

    filename = index_name.replace(" ","_")

    plt.savefig(
        f"reports/charts/{filename}.png"
    )

    plt.close()

print("Benchmark Charts Saved")

print("="*80)
print("ADVANCED EDA COMPLETED")
print("="*80)