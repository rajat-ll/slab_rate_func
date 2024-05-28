# slab_calculator/calculators/calculator9.py

from base import SlabRateCalculator

class SlabRateCalculator9(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 50000000:
            return 0.0075
        elif aum < 100000000:
            return 0.01
        elif aum < 250000000:
            return 0.0105
        elif aum < 500000000:
            return 0.011
        elif aum < 1000000000:
            return 0.0115
        else:
            return 0.0125
