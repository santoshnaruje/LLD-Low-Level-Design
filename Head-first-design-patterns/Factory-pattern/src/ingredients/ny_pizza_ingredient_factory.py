"""Concrete Factory: produces New York–style pizza ingredients.

NY pizza is characterised by a thin, hand-tossed crust, tangy marinara
sauce, sharp Reggiano cheese, fresh Long Island clams, and a vibrant mix
of classic Italian-American veggies.

This class implements every method in PizzaIngredientFactory, guaranteeing
that all ingredients returned form a *coherent* NY-style family.  The pizza
classes that receive this factory never need to import any ingredient class
directly — they only depend on the abstract factory interface.
"""

from typing import List

from src.ingredients.ingredient import (
    ThinCrustDough,
    MarinaraSauce,
    ReggianoCheese,
    Garlic, Onion, Mushroom, RedPepper,
    SlicedPepperoni,
    FreshClam,
)
from src.ingredients.pizza_ingredient_factory import PizzaIngredientFactory


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """Concrete Factory: New York–style ingredient family."""

    def create_dough(self) -> ThinCrustDough:
        print("  Tossing thin crust dough...")
        return ThinCrustDough()

    def create_sauce(self) -> MarinaraSauce:
        print("  Adding marinara sauce...")
        return MarinaraSauce()

    def create_cheese(self) -> ReggianoCheese:
        print("  Adding Reggiano cheese...")
        return ReggianoCheese()

    def create_veggies(self) -> List:
        print("  Tossing on garlic, onion, mushroom, red pepper...")
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self) -> SlicedPepperoni:
        print("  Adding sliced pepperoni...")
        return SlicedPepperoni()

    def create_clam(self) -> FreshClam:
        print("  Adding fresh Long Island clams...")
        return FreshClam()
