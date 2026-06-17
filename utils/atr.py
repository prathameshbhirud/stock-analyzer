import ta


def calculate_atr(df):

    atr = ta.volatility.AverageTrueRange(high=df["High"], low=df["Low"], close=df["Close"], window=14).average_true_range().iloc[-1]

    return round(float(atr), 2)


def atr_percent(df):

    atr = calculate_atr(df)

    close = float(df["Close"].iloc[-1])

    return round(atr / close * 100, 2)