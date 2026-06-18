from patterns.flag_pole import (
    FlagPoleDetector
)


class EMA200ReclaimStrategy:

    def __init__(self):
        self.flag_detector = FlagPoleDetector()

    def evaluate(self, df, volume_ratio):
        if len(df) < 220:
            return self.empty_result()

        latest = df.iloc[-1]

        # --------------------------------
        # Below EMA200 recently
        # --------------------------------

        last_20 = df.tail(20)

        below_ema200_days = (last_20["Close"] < last_20["EMA200"]).sum()

        recently_below_ema200 = below_ema200_days >= 10 #TODO: 15

        # --------------------------------
        # Current breakout above EMA200
        # --------------------------------

        # ema200_breakout = latest["Close"] > latest["EMA200"]
        # TODO Close
        ema200_breakout = latest["High"] > latest["EMA200"]

        # --------------------------------
        # Flag Pole Pattern
        # --------------------------------

        flag_result = self.flag_detector.detect(df)

        pattern_detected = flag_result["detected"]

        # --------------------------------
        # Breakout above pattern
        # --------------------------------

        pattern_breakout = latest["Close"] > flag_result["resistance"]

        # --------------------------------
        # Volume confirmation
        # --------------------------------
        # TODO: 1.5
        volume_confirmed = volume_ratio > 1.2

        # --------------------------------
        # Final match
        # --------------------------------

        matched = recently_below_ema200 and pattern_detected and ema200_breakout and pattern_breakout and volume_confirmed

        return {
            "matched": matched,
            "pattern": "Flag & Pole",
            "recently_below_ema200": recently_below_ema200,
            "ema200_breakout": ema200_breakout,
            "pattern_breakout": pattern_breakout,
            "volume_confirmed": volume_confirmed,
            "entry": round(latest["Close"], 2),
            "stoploss": flag_result["flag_low"],
            "trail_ema": round(latest["EMA10"], 2),
            "ema200": round(latest["EMA200"], 2),
            "volume_ratio": round(volume_ratio, 2),
            "pole_move": flag_result["pole_move"],
            "flag_depth":flag_result["flag_depth"]
        }
    

    def empty_result(self):
        return {
            "matched": False,
            "pattern": "",
            "recently_below_ema200": False,
            "ema200_breakout": False,
            "pattern_breakout": False,
            "volume_confirmed": False,
            "entry": 0,
            "stoploss": 0,
            "trail_ema": 0,
            "ema200": 0,
            "volume_ratio": 0,
            "pole_move": 0,
            "flag_depth": 0
        }