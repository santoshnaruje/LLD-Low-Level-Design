from abc import abstractmethod
from src.beverage.beverage import Beverage


class CondimentDecorator(Beverage):
    """Abstract Decorator: wraps a Beverage and extends its behavior.

    By extending Beverage *and* holding a reference to a Beverage, every
    condiment can be layered around any other beverage (or another
    condiment), building up descriptions and costs dynamically at runtime.

    Design note: the book uses an abstract `get_description()` here to
    force every concrete condiment decorator to re-declare it (ensuring
    they always prepend themselves to the wrapped beverage's description).
    """

    def __init__(self, beverage: Beverage) -> None:
        super().__init__()
        self._beverage: Beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        """Concrete condiment decorators must override this."""
        pass
