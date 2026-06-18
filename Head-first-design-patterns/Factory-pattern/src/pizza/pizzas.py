"""Concrete Products: the pizza types that use the Abstract Factory.

This is the key insight of chapter 4's final design:

  CheesePizza, ClamPizza, PepperoniPizza and VeggiePizza are NOT
  region-specific classes.  The same four classes produce either a
  New York or a Chicago pizza depending on *which* ingredient factory
  was injected by the store.

  - NYPizzaStore injects NYPizzaIngredientFactory  → NY-style result
  - ChicagoPizzaStore injects ChicagoPizzaIngredientFactory → Chicago result

No existing pizza class needs to change when a new region is added.  You
just create a new factory.  This is the Open/Closed Principle in action.
"""

from src.ingredients.pizza_ingredient_factory import PizzaIngredientFactory
from src.pizza.pizza import Pizza


class CheesePizza(Pizza):
    """Concrete Product: classic cheese pizza.

    Uses dough, sauce, and cheese from whatever factory was provided.
    """

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    """Concrete Product: clam pizza.

    Adds regional clam on top of the cheese base.
    NY gets fresh Long Island clams; Chicago gets frozen Chesapeake Bay clams.
    """

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PepperoniPizza(Pizza):
    """Concrete Product: pepperoni pizza.

    Adds sliced pepperoni on top of the cheese base.
    Both regions share SlicedPepperoni, but crust and sauce still differ.
    """

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):
    """Concrete Product: veggie pizza.

    Loaded with regional vegetables — NY gets Garlic/Onion/Mushroom/RedPepper;
    Chicago gets Spinach/BlackOlives/EggPlant.
    """

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
