class RankingAgent:

    def rank(self, technical_score, rs_score, trend_score, volume_ratio, risk, breakout_confirmed):

        score = technical_score

        # Relative Strength
        if rs_score > 10:
            score += 10

        elif rs_score > 5:
            score += 5

        # Trend
        score += (trend_score * 0.1)

        # Volume
        if volume_ratio > 2:
            score += 10

        elif volume_ratio > 1.5:
            score += 5

        # Risk
        if risk == "LOW":
            score += 5
        elif risk == "MEDIUM":
            score += 2

        # Breakout
        if breakout_confirmed:
            score += 15

        return round(min(score, 100))