from abc import ABC, abstractmethod


class Beverage(ABC):
    """Component: the abstract base for all beverages in the Starbuzz menu.

    Every concrete beverage (e.g. HouseBlend, DarkRoast) and every
    decorator (e.g. Milk, Mocha) extends this class, so the decorator
    can step in wherever a plain beverage is expected.
    """

    def __init__(self) -> None:
        self.description: str = "Unknown Beverage"

    def get_description(self) -> str:
        """Return a human-readable description of the beverage."""
        return self.description

    @abstractmethod
    def cost(self) -> float:
        """Return the price of the beverage (in USD)."""
        pass
