"""
Decorator Design Pattern - Pizza Billing System
Base Component: BasePizza

This module defines the abstract base class for all pizzas.
The Decorator pattern allows us to add toppings dynamically without creating
a separate class for every combination of pizza and toppings.
"""

from abc import ABC, abstractmethod


class BasePizza(ABC):
    """
    Abstract base class for all pizzas.
    This is the Component in the Decorator pattern.
    """
    
    @abstractmethod
    def cost(self) -> int:
        """
        Calculate and return the cost of the pizza.
        
        Returns:
            int: Cost of the pizza in rupees
        """
        pass
