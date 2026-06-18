class FlagPoleDetector:

    def detect(self, df):

        if len(df) < 60:
            return {
                "detected": False,
                "pole_move": 0,
                "flag_depth": 0,
                "resistance": 0,
                "flag_low": 0
            }

        # --------------------------------
        # Pole = previous 30 candles
        # --------------------------------

        pole_window = df.iloc[-40:-10]

        pole_low = pole_window["Low"].min()

        pole_high = pole_window["High"].max()

        pole_move = ((pole_high - pole_low) / pole_low) * 100

        pole_detected = pole_move >= 10
        # TODO: 15

        # --------------------------------
        # Flag = last 10 candles
        # --------------------------------

        flag_window = df.iloc[-11:-1]

        flag_resistance = flag_window["High"].max()

        latest = df.iloc[-1]

        pattern_breakout = latest["Close"] > flag_resistance

        flag_high = flag_window["High"].max()

        flag_low = flag_window["Low"].min()

        flag_depth = ((flag_high - flag_low) / flag_high) * 100

        flag_detected = flag_depth <= 15 #TODO: 10

        detected = pole_detected and flag_detected

        return {
            "detected": detected,
            "pole_move": round(pole_move, 2),
            "flag_depth": round(flag_depth, 2),
            "resistance": round(flag_high, 2),
            "flag_low": round(flag_low, 2)
        }