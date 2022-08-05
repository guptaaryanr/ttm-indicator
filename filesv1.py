import os
import yfinance as yf
from datetime import date, timedelta

with open('symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start=date.today() - timedelta(days=150), end=date.today())
        data.to_csv("datasets/{}.csv".format(symbol))
