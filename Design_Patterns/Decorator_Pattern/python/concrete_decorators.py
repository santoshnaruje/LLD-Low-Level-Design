"""
Decorator Design Pattern - Pizza Billing System
Concrete Decorators: ExtraCheese, Mushroom

This module defines concrete topping decorators.
Each decorator wraps a pizza and adds its own cost.
"""

from topping_decorator import ToppingDecorator
from base_pizza import BasePizza


class ExtraCheese(ToppingDecorator):
    """
    Extra Cheese topping decorator.
    Adds ₹10 to the wrapped pizza's cost.
    """
    
    def __init__(self, base_pizza: BasePizza):
        """
        Initialize Extra Cheese topping.
        
        Args:
            base_pizza: The pizza to add extra cheese to
        """
        super().__init__(base_pizza)
    
    def cost(self) -> int:
        """
        Calculate total cost: base pizza cost + extra cheese cost.
        
        Returns:
            int: Total cost in rupees
        """
        return self.base_pizza.cost() + 10


class Mushroom(ToppingDecorator):
    """
    Mushroom topping decorator.
    Adds ₹15 to the wrapped pizza's cost.
    """
    
    def __init__(self, base_pizza: BasePizza):
        """
        Initialize Mushroom topping.
        
        Args:
            base_pizza: The pizza to add mushrooms to
        """
        super().__init__(base_pizza)
    
    def cost(self) -> int:
        """
        Calculate total cost: base pizza cost + mushroom cost.
        
        Returns:
            int: Total cost in rupees
        """
        return self.base_pizza.cost() + 15
