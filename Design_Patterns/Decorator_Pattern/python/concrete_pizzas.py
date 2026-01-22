"""
Decorator Design Pattern - Pizza Billing System
Concrete Components: Margherita, VegDelight, FarmHouse

This module defines concrete pizza classes that extend BasePizza.
Each pizza has a fixed base cost.
"""

from base_pizza import BasePizza


class Margherita(BasePizza):
    """
    Margherita Pizza - A classic pizza with tomato and cheese.
    Base cost: ₹100
    """
    
    def cost(self) -> int:
        """Return the cost of Margherita pizza."""
        return 100


class VegDelight(BasePizza):
    """
    Veg Delight Pizza - A vegetarian pizza with assorted vegetables.
    Base cost: ₹120
    """
    
    def cost(self) -> int:
        """Return the cost of Veg Delight pizza."""
        return 120


class FarmHouse(BasePizza):
    """
    Farm House Pizza - A premium pizza with farm-fresh ingredients.
    Base cost: ₹200
    """
    
    def cost(self) -> int:
        """Return the cost of Farm House pizza."""
        return 200
