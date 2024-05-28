

from abc import ABC, abstractmethod

class SlabRateCalculator(ABC):
    @abstractmethod
    def calculate_rate(self, aum: float) -> float:
        pass

class SlabRateCalculatorFactory(ABC):
    @abstractmethod
    def get_calculator(self, ifa_category: int) -> SlabRateCalculator:
        pass  
