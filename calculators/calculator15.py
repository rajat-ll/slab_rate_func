# slab_calculator/calculators/calculator15.py

from base import SlabRateCalculator

class SlabRateCalculator15(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 10000000:
            return 0.01
        elif aum < 25000000:
            return 0.011
        elif aum < 75000000:
            return 0.0125
        elif aum < 150000000:
            return 0.014
        else:
            return 0.015
