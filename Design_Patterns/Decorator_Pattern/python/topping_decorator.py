"""
Decorator Design Pattern - Pizza Billing System
Base Decorator: ToppingDecorator

This module defines the abstract decorator class.
Key concept: The decorator both "is-a" BasePizza (inheritance) 
and "has-a" BasePizza (composition).
"""

from abc import ABC
from base_pizza import BasePizza


class ToppingDecorator(BasePizza, ABC):
    """
    Abstract decorator class for pizza toppings.
    
    This class demonstrates the core of the Decorator pattern:
    - IS-A relationship: Inherits from BasePizza
    - HAS-A relationship: Contains a BasePizza reference
    
    This allows decorators to wrap other pizzas (or decorated pizzas)
    and add their own cost on top.
    """
    
    def __init__(self, base_pizza: BasePizza):
        """
        Initialize the decorator with a pizza to wrap.
        
        Args:
            base_pizza: The pizza (or decorated pizza) to wrap
        """
        self.base_pizza = base_pizza
