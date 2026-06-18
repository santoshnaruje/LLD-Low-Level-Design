"""Abstract Product: the Pizza base class.

Every pizza in the PizzaStore menu — regardless of region or toppings —
extends this class.  The abstract *prepare()* method is the hook that each
concrete pizza overrides to pull the right ingredients from its injected
PizzaIngredientFactory.

The remaining lifecycle steps (bake, cut, box) are implemented here with
sensible defaults, following the Template Method pattern: the overall
algorithm is fixed; only the ingredient-assembly step varies.
"""

from abc import ABC, abstractmethod
from typing import List, Optional


class Pizza(ABC):
    """Abstract Component: every pizza on the PizzaStore menu.

    Fields set to None/[] initially; concrete pizza's prepare() fills them
    in by calling the ingredient factory.
    """

    def __init__(self) -> None:
        self.name: Optional[str] = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies: List = []
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self) -> None:
        """Pull ingredients from the factory and assemble the raw pizza.

        Each subclass calls its ingredient_factory.create_*() methods here.
        This is where the Abstract Factory is actually used.
        """
        pass

    # ── Shared lifecycle steps (Template Method) ───────────────────────────────

    def bake(self) -> None:
        """Bake the assembled pizza."""
        print("Bake for 25 minutes at 350°F")

    def cut(self) -> None:
        """Slice the baked pizza."""
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        """Box the finished pizza."""
        print("Place pizza in official PizzaStore box")

    # ── Name helpers ──────────────────────────────────────────────────────────

    def get_name(self) -> str:
        """Return the pizza's display name (set by the store after creation)."""
        return self.name

    def set_name(self, name: str) -> None:
        """Set the pizza's display name.  Called by the concrete PizzaStore."""
        self.name = name

    # ── Receipt-style string ──────────────────────────────────────────────────

    def __str__(self) -> str:
        """Render a receipt-style ingredient list for this pizza."""
        lines = [f"---- {self.name} ----"]
        if self.dough:
            lines.append(f"  Dough:     {self.dough}")
        if self.sauce:
            lines.append(f"  Sauce:     {self.sauce}")
        if self.cheese:
            lines.append(f"  Cheese:    {self.cheese}")
        if self.veggies:
            lines.append(f"  Veggies:   {', '.join(str(v) for v in self.veggies)}")
        if self.pepperoni:
            lines.append(f"  Pepperoni: {self.pepperoni}")
        if self.clam:
            lines.append(f"  Clam:      {self.clam}")
        return "\n".join(lines)
