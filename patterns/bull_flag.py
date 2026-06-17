class BullFlagDetector:

    def detect(self, df):

        recent = df.tail(30)

        low = recent["Low"].min()
        high = recent["High"].max()

        rally_pct = (
            (high - low)
            / low
        ) * 100

        if rally_pct < 15:
            return None

        current = recent["Close"].iloc[-1]

        pullback = (
            (high - current)
            / high
        ) * 100

        if pullback > 8:
            return None

        return {
            "pattern": "Bull Flag",
            "confidence": 75
        }