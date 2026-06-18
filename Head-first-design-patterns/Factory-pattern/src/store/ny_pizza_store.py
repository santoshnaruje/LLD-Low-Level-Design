"""Concrete Creator: New York–style PizzaStore.

This class overrides create_pizza() — the Factory Method — to wire each
pizza type to the NYPizzaIngredientFactory.

The ingredient factory is what gives every NY pizza its thin-crust, marinara,
Reggiano character without the pizza classes themselves knowing anything about
New York.  That is the two-pattern combination the book demonstrates:

  Factory Method  → NYPizzaStore decides *which pizza type* to create.
  Abstract Factory → NYPizzaIngredientFactory decides *which ingredients* to use.
"""

from src.ingredients.ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from src.pizza.pizza import Pizza
from src.pizza.pizzas import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from src.store.pizza_store import PizzaStore


class NYPizzaStore(PizzaStore):
    """Concrete Creator for New York–style pizzas."""

    def create_pizza(self, pizza_type: str) -> Pizza:
        """Factory Method implementation: instantiate the right NY pizza.

        Injects NYPizzaIngredientFactory into the pizza so it assembles with
        NY-style ingredients during prepare().
        """
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        else:
            raise ValueError(
                f"NYPizzaStore does not know how to make '{pizza_type}' pizza."
            )

        return pizza
