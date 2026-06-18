"""Ingredients package — Abstract Factory and concrete ingredient families."""

from src.ingredients.ingredient import (
    ThinCrustDough, ThickCrustDough,
    MarinaraSauce, PlumTomatoSauce,
    ReggianoCheese, MozzarellaCheese,
    Garlic, Onion, Mushroom, RedPepper,
    Spinach, BlackOlives, EggPlant,
    SlicedPepperoni,
    FreshClam, FrozenClam,
)
from src.ingredients.pizza_ingredient_factory import PizzaIngredientFactory
from src.ingredients.ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from src.ingredients.chicago_pizza_ingredient_factory import ChicagoPizzaIngredientFactory

__all__ = [
    "ThinCrustDough", "ThickCrustDough",
    "MarinaraSauce", "PlumTomatoSauce",
    "ReggianoCheese", "MozzarellaCheese",
    "Garlic", "Onion", "Mushroom", "RedPepper",
    "Spinach", "BlackOlives", "EggPlant",
    "SlicedPepperoni",
    "FreshClam", "FrozenClam",
    "PizzaIngredientFactory",
    "NYPizzaIngredientFactory",
    "ChicagoPizzaIngredientFactory",
]
