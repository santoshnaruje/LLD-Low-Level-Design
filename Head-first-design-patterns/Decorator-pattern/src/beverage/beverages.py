from src.beverage.beverage import Beverage


class HouseBlend(Beverage):
    """Concrete Component: Starbuzz House Blend coffee."""

    def __init__(self) -> None:
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    """Concrete Component: Starbuzz Dark Roast coffee."""

    def __init__(self) -> None:
        super().__init__()
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    """Concrete Component: Starbuzz Decaf coffee."""

    def __init__(self) -> None:
        super().__init__()
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05


class Espresso(Beverage):
    """Concrete Component: a single shot of Starbuzz Espresso."""

    def __init__(self) -> None:
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
