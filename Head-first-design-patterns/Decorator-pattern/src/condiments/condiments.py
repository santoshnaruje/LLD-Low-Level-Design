from src.beverage.beverage import Beverage
from src.condiments.condiment_decorator import CondimentDecorator


class Milk(CondimentDecorator):
    """Concrete Decorator: adds steamed Milk to a beverage (+$0.10)."""

    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Milk"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    """Concrete Decorator: adds a shot of Mocha (chocolate) to a beverage (+$0.20)."""

    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20


class Soy(CondimentDecorator):
    """Concrete Decorator: swaps milk for Soy in a beverage (+$0.15)."""

    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self._beverage.cost() + 0.15


class Whip(CondimentDecorator):
    """Concrete Decorator: adds whipped cream to a beverage (+$0.10)."""

    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10
