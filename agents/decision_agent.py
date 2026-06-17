class DecisionAgent:

    def decide(self, score):

        if score >= 85:
            return "STRONG BUY"

        if score >= 70:
            return "BUY"

        if score >= 55:
            return "WATCH"

        return "AVOID"