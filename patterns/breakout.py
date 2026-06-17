from utils.support_resistance import (
    get_resistance
)


class BreakoutDetector:

    def detect(self, df):

        resistance = (get_resistance(df))

        if resistance is None:
            return None

        close = (float(df["Close"].iloc[-1]))

        breakout_pct = ((close - resistance) / resistance) * 100

        if breakout_pct > 2:
            return {
                "pattern": "Breakout",
                "confidence": 90
            }

        return None