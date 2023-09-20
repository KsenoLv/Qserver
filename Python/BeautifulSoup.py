# Detailed description you can read in my blog: 
# https://psql.pro/market-data-with-python-and-beautifulsoup/

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
from tqdm import tqdm
import os
import time

def date_to_unix_timestamp(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return int(date.timestamp())

def scrape_yahoo_finance_data(ticker, start_date, end_date):
    start_timestamp = date_to_unix_timestamp(start_date)
    end_timestamp = date_to_unix_timestamp(end_date)

    url = f"https://finance.yahoo.com/quote/{ticker}/history"
    params = {
        "period1": start_timestamp,
        "period2": end_timestamp,
        "interval": "1d",
        "filter": "history",
        "frequency": "1d",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        "Referer": f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    if len(tables) == 0:
        print(f"No tables found for ticker {ticker}")
        return None
    elif len(tables) > 1:
        print(f"Multiple tables found for ticker {ticker}")
        return None

    table = tables[0]
    rows = table.find_all("tr")
    if len(rows) == 0:
        print(f"No rows found for ticker {ticker}")
        return None

    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    headers = ["Ticker", "Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    data = [[ticker] + row for row in data if len(row) == 7]
    data.insert(0, headers)

    return data

def save_data_to_csv(data, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == "__main__":
    ticker_file = r"/YOUR_FOLDER_PATH/WITH_NECESSARY_TICKER_LIST.txt"
    start_date = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d") # Yesterday's date (Year-month-day)
    end_date = datetime.now().strftime("%Y-%m-%d") # Current date (Year-month-day)
    folder_path = r"/YOUR_FOLDER_PATH_FOR_NEW_DATA/"

    with open(ticker_file, "r") as f:
        tickers = [line.strip() for line in f]

    for ticker in tqdm(tickers):
        data = scrape_yahoo_finance_data(ticker, start_date, end_date)
        if data is not None:
            filepath = os.path.join(folder_path, f"{ticker}.csv")
            save_data_to_csv(data, filepath)
        time.sleep(2) # Pause for 1 second after processing each ticker

        # Check if this is the last ticker in the list
        if ticker == tickers[-1]:
            break  # Stop the script after processing the last ticker
        
# Add this line to stop execution after running in cron
raise SystemExit
