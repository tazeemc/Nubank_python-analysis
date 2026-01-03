import requests
import pandas as pd
import os
from datetime import datetime, timedelta

def fetch_brl_usd():
    if not os.path.exists('data'):
        os.makedirs('data')

    # Calculate date range (last 10 years)
    end_date = datetime.now().strftime('%d/%m/%Y')
    start_date = (datetime.now() - timedelta(days=365 * 10)).strftime('%d/%m/%Y')

    # Central Bank of Brazil API for BRL/USD with date range
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json&dataInicial={start_date}&dataFinal={end_date}"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains an error
    if "error" in data:
        print("API Error:", data["error"])
        print("Message:", data["message"])
        print("Syntax:", data["syntax"])
        return pd.DataFrame()

    # Process the data
    df = pd.DataFrame([{
        "date": item["data"],
        "brl_usd": float(item["valor"].replace(",", "."))
    } for item in data])
    df.to_csv("data/brl_usd.csv", index=False)
    print("BRL/USD data saved to data/brl_usd.csv")
    return df

def fetch_selic():
    if not os.path.exists('data'):
        os.makedirs('data')

    # Calculate date range (last 10 years)
    end_date = datetime.now().strftime('%d/%m/%Y')
    start_date = (datetime.now() - timedelta(days=365 * 10)).strftime('%d/%m/%Y')

    # Selic Rate (Brazil's benchmark interest rate) with date range
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={start_date}&dataFinal={end_date}"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains an error
    if "error" in data:
        print("API Error:", data["error"])
        print("Message:", data["message"])
        print("Syntax:", data["syntax"])
        return pd.DataFrame()

    # Process the data
    df = pd.DataFrame([{
        "date": item["data"],
        "selic": float(item["valor"].replace(",", "."))
    } for item in data])
    df.to_csv("data/selic.csv", index=False)
    print("Selic Rate data saved to data/selic.csv")
    return df

def fetch_ipca():
    if not os.path.exists('data'):
        os.makedirs('data')

    # Calculate date range (last 10 years)
    end_date = datetime.now().strftime('%d/%m/%Y')
    start_date = (datetime.now() - timedelta(days=365 * 10)).strftime('%d/%m/%Y')

    # IPCA Inflation (Brazil's consumer inflation) with date range
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={start_date}&dataFinal={end_date}"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains an error
    if "error" in data:
        print("API Error:", data["error"])
        print("Message:", data["message"])
        print("Syntax:", data["syntax"])
        return pd.DataFrame()

    # Process the data
    df = pd.DataFrame([{
        "date": item["data"],
        "ipca": float(item["valor"].replace(",", "."))
    } for item in data])
    df.to_csv("data/ipca.csv", index=False)
    print("IPCA Inflation data saved to data/ipca.csv")
    return df

if __name__ == "__main__":
    fetch_brl_usd()
    fetch_selic()
    fetch_ipca()
