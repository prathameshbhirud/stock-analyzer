from utils.swing_points import (
    get_swing_highs,
    get_swing_lows
)


class AscendingTriangleDetector:

    def detect(self, df):

        highs = get_swing_highs(df)
        lows = get_swing_lows(df)

        if len(highs) < 3:
            return None

        resistance = (
            df.iloc[highs[-3:]]
            ["High"]
            .mean()
        )

        resistance_range = (
            df.iloc[highs[-3:]]
            ["High"]
            .max()
            -
            df.iloc[highs[-3:]]
            ["High"]
            .min()
        )

        if resistance_range / resistance > 0.02:
            return None

        return {
            "pattern":
            "Ascending Triangle",
            "confidence": 80
        }