# slab_calculator/calculators/calculator10.py

from base import SlabRateCalculator

class SlabRateCalculator10(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 25000000:
            return 0.01
        elif aum < 50000000:
            return 0.011
        elif aum < 100000000:
            return 0.012
        elif aum < 250000000:
            return 0.013
        elif aum < 500000000:
            return 0.014
        else:
            return 0.015
