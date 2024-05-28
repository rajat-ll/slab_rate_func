# slab_calculator/calculators/calculator2.py

from base import SlabRateCalculator

class SlabRateCalculator2(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 10000000:
            return 0.0075
        elif aum < 25000000:
            return 0.01
        elif aum < 75000000:
            return 0.011
        elif aum < 250000000:
            return 0.0125
        elif aum < 500000000:
            return 0.014
        elif aum < 1000000000:
            return 0.015
        else:
            return 0.0175
