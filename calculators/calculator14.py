# slab_calculator/calculators/calculator14.py

from base import SlabRateCalculator

class SlabRateCalculator14(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 49999999:
            return 0.012
        elif aum < 99999999:
            return 0.012
        elif aum < 249999999:
            return 0.012
        elif aum < 499999999:
            return 0.012
        elif aum < 999999999:
            return 0.0125
        elif aum < 4500000000:
            return 0.015
        else:
            return 0.0
