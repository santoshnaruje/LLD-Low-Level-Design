"""Concrete Creator: Chicago-style (deep-dish) PizzaStore.

This class overrides create_pizza() to wire each pizza type to the
ChicagoPizzaIngredientFactory.  The pizza *types* (CheesePizza, ClamPizza, …)
are the same classes as NYPizzaStore uses — only the factory differs, and
that factory swap is what makes the pizza taste like Chicago deep dish.
"""

from src.ingredients.chicago_pizza_ingredient_factory import ChicagoPizzaIngredientFactory
from src.pizza.pizza import Pizza
from src.pizza.pizzas import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza
from src.store.pizza_store import PizzaStore


class ChicagoPizzaStore(PizzaStore):
    """Concrete Creator for Chicago-style (deep-dish) pizzas."""

    def create_pizza(self, pizza_type: str) -> Pizza:
        """Factory Method implementation: instantiate the right Chicago pizza.

        Injects ChicagoPizzaIngredientFactory into the pizza so it assembles
        with thick-crust, plum tomato sauce and mozzarella during prepare().
        """
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Deep Dish Cheese Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Deep Dish Clam Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Deep Dish Pepperoni Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Deep Dish Veggie Pizza")
        else:
            raise ValueError(
                f"ChicagoPizzaStore does not know how to make '{pizza_type}' pizza."
            )

        return pizza
