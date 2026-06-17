def volume_breakout(df):

    latest = df.iloc[-1]

    return (
        latest["Volume"]
        > latest["VolumeAvg20"] * 1.5
    )

def volume_score(df):

    latest_volume = (df["Volume"].iloc[-1])

    avg_volume = (df["Volume"].rolling(20).mean().iloc[-1])

    ratio = (latest_volume / avg_volume)

    return round(ratio, 2)