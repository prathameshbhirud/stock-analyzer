import json
import ollama


class AITechnicalAgent:

    def analyze(self, symbol, df, support, resistance, rs, atr_pct):

        recent = df.tail(120)

        candles = []

        for _, row in recent.iterrows():

            candles.append({
                "open": round(float(row["Open"]), 2),
                "high": round(float(row["High"]), 2),
                "low": round(float(row["Low"]), 2),
                "close": round(float(row["Close"]), 2),
                "volume": int(row["Volume"])
            })

        prompt = f"""
                    You are a professional stock market technical analyst.

                    Analyze the stock data below and identify the SINGLE MOST LIKELY chart pattern.

                    Available patterns:

                    - Cup & Handle
                    - Bull Flag
                    - Bear Flag
                    - Ascending Triangle
                    - Descending Triangle
                    - Double Bottom
                    - Double Top
                    - Head & Shoulders
                    - Inverse Head & Shoulders
                    - Breakout

                    Stock Symbol:
                    {symbol}

                    Support:
                    {support}

                    Resistance:
                    {resistance}

                    Relative Strength:
                    {rs}

                    ATR Percent:
                    {atr_pct}

                    Recent OHLCV Data:
                    {json.dumps(candles)}

                    Return ONLY valid JSON.

                    Rules:

                    1. Return exactly one primary pattern.
                    2. Confidence must be between 0 and 100.
                    3. Trend must be Bullish, Bearish, or Neutral.
                    4. Reasoning should be 1-2 sentences.
                    5. Do not return markdown.
                    6. Do not use ```json.
                    7. Do not include explanations outside JSON.

                    Example:

                    {{
                        "patterns": ["Ascending Triangle"],
                        "confidence": 85,
                        "trend": "Bullish",
                        "reasoning": "Price is forming higher lows beneath a relatively flat resistance level with strengthening momentum."
                    }}

                    If no clear pattern exists, return:

                    {{
                        "patterns": ["No Clear Pattern"],
                        "confidence": 30,
                        "trend": "Neutral",
                        "reasoning": "No high-confidence chart pattern detected."
                    }}
                """

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]