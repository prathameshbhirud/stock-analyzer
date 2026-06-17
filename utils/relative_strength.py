def calculate_relative_strength(stock_df, benchmark_df):

    stock_return = (stock_df["Close"].iloc[-1] / stock_df["Close"].iloc[-21] - 1) * 100

    benchmark_return = (benchmark_df["Close"].iloc[-1] / benchmark_df["Close"].iloc[-21] - 1) * 100

    rs = (stock_return - benchmark_return)

    return round(rs, 2)