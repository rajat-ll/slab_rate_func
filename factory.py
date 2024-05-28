# slab_calculator/factory.py

from base import SlabRateCalculator, SlabRateCalculatorFactory
from calculators.calculator1 import SlabRateCalculator1
from calculators.calculator2 import SlabRateCalculator2
from calculators.calculator3 import SlabRateCalculator3
from calculators.calculator4 import SlabRateCalculator4
from calculators.calculator5 import SlabRateCalculator5
from calculators.calculator6 import SlabRateCalculator6
from calculators.calculator7 import SlabRateCalculator7
from calculators.calculator8 import SlabRateCalculator8
from calculators.calculator9 import SlabRateCalculator9
from calculators.calculator10 import SlabRateCalculator10
from calculators.calculator11 import SlabRateCalculator11
from calculators.calculator12 import SlabRateCalculator12
from calculators.calculator13 import SlabRateCalculator13
from calculators.calculator14 import SlabRateCalculator14
from calculators.calculator15 import SlabRateCalculator15
from calculators.calculator16 import SlabRateCalculator16
from calculators.calculator17 import SlabRateCalculator17
from calculators.calculator18 import SlabRateCalculator18
from calculators.calculator19 import SlabRateCalculator19
from calculators.calculator20 import SlabRateCalculator20
 


class SingleSlabRateCalculatorFactory(SlabRateCalculatorFactory):
    def get_calculator(self, ifa_category: int) -> SlabRateCalculator:
        calculator_mapping = {
            1: SlabRateCalculator1,
            2: SlabRateCalculator2,
            3: SlabRateCalculator3,
            4: SlabRateCalculator4,
            5: SlabRateCalculator5,
            6: SlabRateCalculator6,
            7: SlabRateCalculator7,
            8: SlabRateCalculator8,
            9: SlabRateCalculator9,
            10: SlabRateCalculator10,
            11: SlabRateCalculator11,
            12: SlabRateCalculator12,
            13: SlabRateCalculator13,
            14: SlabRateCalculator14,
            15: SlabRateCalculator15,
            16: SlabRateCalculator16,
            17: SlabRateCalculator17,
            18: SlabRateCalculator18,
            19: SlabRateCalculator19,
            20: SlabRateCalculator20,
        }

        if ifa_category not in calculator_mapping:
            raise ValueError("Invalid IFA category.")

        return calculator_mapping[ifa_category]()
