# slab_calculator/calculators/calculator12.py

from base import SlabRateCalculator

class SlabRateCalculator12(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 9999999:
            return 0.008
        elif aum < 24999999:
            return 0.0105
        elif aum < 74999999:
            return 0.012
        elif aum < 149999999:
            return 0.0135
        elif aum < 299999999:
            return 0.0145
        elif aum < 1500000000:
            return 0.015
        else:
            return 0.0
