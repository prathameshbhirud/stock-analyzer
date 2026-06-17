from scipy.signal import find_peaks
import numpy as np


def get_resistance(df):

    highs = np.asarray(df["High"]).flatten()

    peaks, _ = find_peaks(highs, distance=10)

    if len(peaks) < 3:
        return None

    resistance = (df.iloc[peaks[-3:]]["High"].mean())

    return round(float(resistance), 2)


def get_support(df):

    lows = np.asarray(df["Low"]).flatten()

    valleys, _ = find_peaks(-lows, distance=10)

    if len(valleys) < 3:
        return None

    support = (df.iloc[valleys[-3:]]["Low"].mean())

    return round(float(support), 2)