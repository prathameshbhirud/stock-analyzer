from patterns.double_bottom import DoubleBottomDetector

from patterns.bull_flag import BullFlagDetector

from patterns.ascending_triangle import AscendingTriangleDetector

from patterns.breakout import BreakoutDetector


class PatternAgent:

    def __init__(self):

        self.detectors = [
            DoubleBottomDetector(),
            BullFlagDetector(),
            AscendingTriangleDetector(),
            BreakoutDetector()
        ]

    def scan(self, df):

        results = []

        for detector in self.detectors:

            pattern = detector.detect(df)

            if pattern:
                results.append(pattern)

        return results