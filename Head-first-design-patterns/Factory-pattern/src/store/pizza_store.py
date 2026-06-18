"""Abstract Creator: PizzaStore defines the Factory Method contract.

The Factory Method pattern lives here.  PizzaStore provides the high-level
template for ordering any pizza (prepare → bake → cut → box), but it
deliberately leaves the step of *creating* the pizza abstract — that is
the Factory Method.

Each regional subclass (NYPizzaStore, ChicagoPizzaStore) overrides
create_pizza() to decide which concrete Pizza class to instantiate and
which ingredient factory to inject.  The ordering logic in order_pizza()
never needs to change.
"""

from abc import ABC, abstractmethod

from src.pizza.pizza import Pizza


class PizzaStore(ABC):
    """Abstract Creator in the Factory Method pattern.

    Design Principle — Dependency Inversion:
        order_pizza() depends only on the abstract Pizza type, never on any
        concrete pizza class.  The concrete class is chosen by the subclass
        through the factory method.
    """

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        """Factory Method: subclasses decide which Pizza to instantiate.

        This is the only method regional subclasses must override.  By making
        creation a method (rather than hardcoding it inline), we let subclasses
        vary the product independently of the ordering algorithm.

        Args:
            pizza_type: A string key — "cheese", "clam", "pepperoni", "veggie".

        Returns:
            A fully-named, but not-yet-prepared, Pizza object.
        """
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        """Template Method: orchestrates the complete pizza-making workflow.

        Calls the factory method to get the right pizza, then runs the standard
        lifecycle steps.  Clients (customers) only call this method; they never
        call create_pizza() directly.

        Args:
            pizza_type: The type of pizza to order.

        Returns:
            The finished, boxed Pizza object.
        """
        pizza = self.create_pizza(pizza_type)

        print(f"\n--- Making a {pizza.get_name()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
