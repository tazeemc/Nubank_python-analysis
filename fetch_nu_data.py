import yfinance as yf
import pandas as pd
import os

def fetch_nu_data():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Download $NU data (5-year history)
    nu = yf.Ticker("NU")
    df = nu.history(period="5y")
    df.to_csv("data/nu_stock.csv")
    print("$NU stock data saved to data/nu_stock.csv")
    return df

if __name__ == "__main__":
    fetch_nu_data()
