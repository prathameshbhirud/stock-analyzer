import yfinance as yf
import pandas as pd


class BenchmarkAgent:

    def fetch_nifty(self):

        df = yf.download(
            "^NSEI",
            period="1y",
            interval="1d",
            progress=False,
            auto_adjust=True
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = (df.columns.get_level_values(0))

        return df