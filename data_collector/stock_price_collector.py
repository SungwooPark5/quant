import yfinance
import pandas as pd
import numpy as np


class StockPriceCollector:

    def __init__(
        self,
        tickers: list[str],
    ):
        self.tickers = tickers
        self.price_df = pd.DataFrame()

    def load_yfinance_data(self, start_date: str):
        df = yfinance.download(self.tickers, start=start_date)
        self.price_df = df["Close"]

    def save_price_data(self):
        pass


data_collector = StockPriceCollector(["BIL", "SPY", "TLT"])

data_collector.load_yfinance_data(start_date="1970-01-01")
print(data_collector.price_df)
