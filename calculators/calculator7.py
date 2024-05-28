# slab_calculator/calculators/calculator7.py

from base import SlabRateCalculator

class SlabRateCalculator7(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 10000000:
            return 0.0085
        elif aum < 25000000:
            return 0.011
        elif aum < 50000000:
            return 0.012
        elif aum < 100000000:
            return 0.0125
        elif aum < 250000000:
            return 0.0135
        elif aum < 500000000:
            return 0.014
        else:
            return 0.015
