import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\nTotal Fund Houses:", fund_master["fund_house"].nunique())
print("Total Categories:", fund_master["category"].nunique())
print("Total Sub Categories:", fund_master["sub_category"].nunique())
print("Total Risk Categories:", fund_master["risk_category"].nunique())

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master exist in nav_history.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print("\nDATA QUALITY SUMMARY")
print("-" * 40)
print(f"Total Fund Master Records : {len(fund_master)}")
print(f"Total NAV Records         : {len(nav_history)}")
print(f"Missing AMFI Codes        : {len(missing_codes)}")