# slab_calculator/calculators/calculator13.py

from base import SlabRateCalculator

class SlabRateCalculator13(SlabRateCalculator):
    def calculate_rate(self, aum: float) -> float:
        if aum < 49999999:
            return 0.01
        elif aum < 99999999:
            return 0.01
        elif aum < 249999999:
            return 0.0105
        elif aum < 499999999:
            return 0.0115
        elif aum < 999999999:
            return 0.0125
        elif aum < 4000000000:
            return 0.015
        else:
            return 0.0
