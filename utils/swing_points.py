from scipy.signal import find_peaks
import numpy as np


def get_swing_highs(df):

    highs = np.asarray(df["High"]).flatten()

    peaks, _ = find_peaks(highs, distance=5)

    return peaks


def get_swing_lows(df):

    lows = np.asarray(df["Low"]).flatten()

    peaks, _ = find_peaks(-lows, distance=5)

    return peaks