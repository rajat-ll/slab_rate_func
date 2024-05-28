# slab_calculator/calculators/calculator6.py

from base import SlabRateCalculator

class SlabRateCalculator6(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 10000000:
            return 0.005
        elif aum < 25000000:
            return 0.00575
        elif aum < 75000000:
            return 0.00625
        elif aum < 150000000:
            return 0.007
        else:
            return 0.0075
