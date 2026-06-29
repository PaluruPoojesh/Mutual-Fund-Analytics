import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw/live_nav", exist_ok=True)

# AMFI Codes
funds = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 80)
print("LIVE NAV DATA DOWNLOAD")
print("=" * 80)

for fund_name, code in funds.items():

    print(f"\nDownloading: {fund_name}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if "data" in data:

            df = pd.DataFrame(data["data"])

            output_file = f"data/raw/live_nav/{fund_name}.csv"

            df.to_csv(output_file, index=False)

            print(f"Saved -> {output_file}")

        else:

            print("No NAV data found.")

    else:

        print("Failed:", response.status_code)

print("\nAll downloads completed.")