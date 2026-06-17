def is_uptrend(df):

    latest = df.iloc[-1]

    return (
        latest["Close"]
        > latest["SMA20"]
        > latest["SMA50"]
        > latest["SMA200"]
    )