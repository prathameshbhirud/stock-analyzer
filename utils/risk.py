def risk_rating(atr_percent):

    if atr_percent < 2:
        return "LOW"

    if atr_percent < 4:
        return "MEDIUM"

    return "HIGH"