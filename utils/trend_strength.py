def trend_score(df):

    latest = df.iloc[-1]

    score = 0

    if latest["Close"] > latest["SMA20"]:
        score += 25

    if latest["Close"] > latest["SMA50"]:
        score += 25

    if latest["Close"] > latest["SMA200"]:
        score += 25

    if latest["SMA20"] > latest["SMA50"]:
        score += 25

    return score