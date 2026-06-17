class ScoringAgent:

    def score(self, patterns, df):

        score = 0

        if patterns:

            score += (sum(p["confidence"] for p in patterns) / len(patterns))

        latest = df.iloc[-1]

        if latest["RSI"] > 55:
            score += 10

        if (latest["SMA20"] > latest["SMA50"]):
            score += 10

        if (latest["SMA50"] > latest["SMA200"]):
            score += 10

        return round(min(score, 100))