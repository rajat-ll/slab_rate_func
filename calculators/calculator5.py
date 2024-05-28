# slab_calculator/calculators/calculator5.py

from base import SlabRateCalculator

class SlabRateCalculator5(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 10000000:
            return 0.00375
        elif aum < 25000000:
            return 0.005
        elif aum < 75000000:
            return 0.0055
        elif aum < 250000000:
            return 0.00625
        elif aum < 500000000:
            return 0.007
        elif aum < 1000000000:
            return 0.0075
        else:
            return 0.00875
