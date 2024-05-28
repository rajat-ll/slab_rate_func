

from factory import SingleSlabRateCalculatorFactory

def calculate_slab_based_commission_rate(aum: float, ifa_category: int) -> float:
    if not isinstance(aum, float):
        raise TypeError("aum must be a float.")

    if not isinstance(ifa_category, int):
        raise TypeError("ifa_category must be an int.")

    if aum < 0:
        raise ValueError("The value of aum must be non-negative.")

    factory = SingleSlabRateCalculatorFactory()
    calculator = factory.get_calculator(ifa_category)
    return calculator.calculate_rate(aum)

if __name__ == "__main__":
    aum = 20000000.0
    ifa_category = 1
    rate = calculate_slab_based_commission_rate(aum, ifa_category)
    print(f"The commission rate for AUM {aum} in IFA category {ifa_category} is {rate}")
