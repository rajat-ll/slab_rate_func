# slab_calculator/calculators/calculator20.py

from base import SlabRateCalculator

class SlabRateCalculator20(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 100000000:
            return 0.01
        elif aum < 500000000:
            return 0.0115
        elif aum < 1000000000:
            return 0.012
        elif aum < 2500000000:
            return 0.0127
        else:
            return 0.0127
