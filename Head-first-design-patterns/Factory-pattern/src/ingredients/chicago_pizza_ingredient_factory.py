"""Concrete Factory: produces Chicago-style (deep-dish) pizza ingredients.

Chicago pizza is a completely different beast: a thick, pan-pressed crust,
slow-cooked plum tomato sauce, shredded mozzarella layered *under* the
toppings, hearty vegetables and frozen clams from Chesapeake Bay.

Importantly, the concrete pizza classes (CheesePizza, ClamPizza, etc.) are
the *same* classes used by the NY store.  They produce a Chicago-style result
here solely because they call this factory instead of NYPizzaIngredientFactory.
That is the payoff of the Abstract Factory pattern.
"""

from typing import List

from src.ingredients.ingredient import (
    ThickCrustDough,
    PlumTomatoSauce,
    MozzarellaCheese,
    Spinach, BlackOlives, EggPlant,
    SlicedPepperoni,
    FrozenClam,
)
from src.ingredients.pizza_ingredient_factory import PizzaIngredientFactory


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """Concrete Factory: Chicago-style (deep-dish) ingredient family."""

    def create_dough(self) -> ThickCrustDough:
        print("  Pressing thick crust dough into the pan...")
        return ThickCrustDough()

    def create_sauce(self) -> PlumTomatoSauce:
        print("  Ladling on plum tomato sauce...")
        return PlumTomatoSauce()

    def create_cheese(self) -> MozzarellaCheese:
        print("  Layering shredded mozzarella...")
        return MozzarellaCheese()

    def create_veggies(self) -> List:
        print("  Piling on spinach, black olives, eggplant...")
        return [Spinach(), BlackOlives(), EggPlant()]

    def create_pepperoni(self) -> SlicedPepperoni:
        print("  Adding sliced pepperoni...")
        return SlicedPepperoni()

    def create_clam(self) -> FrozenClam:
        print("  Adding frozen Chesapeake Bay clams...")
        return FrozenClam()
