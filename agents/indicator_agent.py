import ta


class IndicatorAgent:

    def enrich(self, df):

        df["SMA20"] = (df["Close"].rolling(20).mean())

        df["SMA50"] = (df["Close"].rolling(50).mean())

        df["SMA200"] = (df["Close"].rolling(200).mean())

        df["RSI"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()

        df["VolumeAvg20"] = (df["Volume"].rolling(20).mean())

        df["EMA10"] = df["Close"].ewm(span=10, adjust=False).mean()

        df["EMA200"] = df["Close"].ewm(span=200, adjust=False).mean()

        df = df.dropna()

        return df