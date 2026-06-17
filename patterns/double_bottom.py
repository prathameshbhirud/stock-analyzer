from utils.swing_points import get_swing_lows


class DoubleBottomDetector:

    def detect(self, df):

        lows = get_swing_lows(df)

        if len(lows) < 2:
            return None

        low1 = df.iloc[lows[-2]]["Low"]
        low2 = df.iloc[lows[-1]]["Low"]

        difference = abs(low1 - low2)

        if difference / low1 <= 0.03:

            return {
                "pattern": "Double Bottom",
                "confidence": 80
            }

        return None