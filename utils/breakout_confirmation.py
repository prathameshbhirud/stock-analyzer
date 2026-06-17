def confirmed_breakout(close_price, resistance, volume_ratio, rs):

    if resistance is None:
        return False

    if close_price <= resistance:
        return False

    if volume_ratio < 1.5:
        return False

    if rs <= 0:
        return False

    return True