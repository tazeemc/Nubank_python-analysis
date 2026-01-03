import pandas as pd
import os

def merge_data():
    if not os.path.exists('data'):
        os.makedirs('data')

    # Load all datasets
    nu_stock = pd.read_csv("data/nu_stock.csv", index_col=0, parse_dates=True)
    brl_usd = pd.read_csv("data/brl_usd.csv", parse_dates=True)
    selic = pd.read_csv("data/selic.csv", parse_dates=True)
    ipca = pd.read_csv("data/ipca.csv", parse_dates=True)

    # Merge stock and macro data
    merged = nu_stock.join(brl_usd.set_index("date"), how="left")
    merged = merged.join(selic.set_index("date"), how="left")
    merged = merged.join(ipca.set_index("date"), how="left")

    # Calculate metrics
    merged["NU_MA_50"] = merged["Close"].rolling(50).mean()
    merged["NU_MA_200"] = merged["Close"].rolling(200).mean()
    merged["NU_Return"] = merged["Close"].pct_change()
    merged["BRL_USD_MA_30"] = merged["brl_usd"].rolling(30).mean()

    # Save merged data
    merged.to_csv("data/nu_brazil_merged.csv")
    print("Merged data saved to data/nu_brazil_merged.csv")
    return merged

if __name__ == "__main__":
    merge_data()
