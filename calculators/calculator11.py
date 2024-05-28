# slab_calculator/calculators/calculator11.py

from base import SlabRateCalculator

class SlabRateCalculator11(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 1000000000:
            return 0.0125
        elif aum < 2500000000:
            return 0.015
        elif aum < 5000000000:
            return 0.02
        else:
            return 0.0
