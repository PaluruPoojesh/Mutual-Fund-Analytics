import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder
os.makedirs("reports/charts", exist_ok=True)

# -----------------------------
# Load Data
# -----------------------------

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

print("="*80)
print("EDA STARTED")
print("="*80)

# -----------------------------
# Chart 1
# Fund House Distribution
# -----------------------------

fund_counts = fund_master["fund_house"].value_counts()

plt.figure(figsize=(10,6))

fund_counts.plot(kind="bar")

plt.title("Fund House Distribution")

plt.xlabel("Fund House")

plt.ylabel("Number of Schemes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/charts/fund_house_distribution.png")

plt.close()

print("Chart 1 Saved")

# -----------------------------
# Chart 2
# Risk Category
# -----------------------------

risk = fund_master["risk_category"].value_counts()

plt.figure(figsize=(7,7))

risk.plot(kind="pie",autopct="%1.1f%%")

plt.ylabel("")

plt.title("Risk Category Distribution")

plt.savefig("reports/charts/risk_distribution.png")

plt.close()

print("Chart 2 Saved")

# -----------------------------
# Chart 3
# SIP Trend
# -----------------------------

plt.figure(figsize=(12,6))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"]
)

plt.xticks(rotation=90)

plt.title("Monthly SIP Inflow")

plt.tight_layout()

plt.savefig("reports/charts/sip_trend.png")

plt.close()

print("Chart 3 Saved")

# -----------------------------
# Chart 4
# AUM Trend
# -----------------------------

latest = aum.groupby("fund_house")["aum_lakh_crore"].max()

plt.figure(figsize=(10,6))

latest.sort_values().plot(kind="barh")

plt.title("Fund House AUM")

plt.tight_layout()

plt.savefig("reports/charts/aum_distribution.png")

plt.close()

print("Chart 4 Saved")

print("="*80)
print("EDA COMPLETED")
print("="*80)