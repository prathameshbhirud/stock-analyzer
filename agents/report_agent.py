from datetime import datetime

import pandas as pd


class ReportAgent:

    def generate_summary(self, results_df):

        return {
            "scan_time": datetime.now(),
            "total": len(results_df),
            "strong_buy": len(results_df[results_df["Decision"] == "STRONG BUY"]),
            "buy": len(results_df[results_df["Decision"] == "BUY"]),
            "watch": len(results_df[results_df["Decision"] == "WATCH"]),
            "avoid": len(results_df[results_df["Decision"] == "AVOID"])
        }