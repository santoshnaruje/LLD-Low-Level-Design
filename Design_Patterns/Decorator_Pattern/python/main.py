"""
Decorator Design Pattern - Pizza Billing System
Main Demo File

This demonstrates the Decorator pattern in action.
Shows how toppings can be added dynamically to pizzas without
creating separate classes for every combination.
"""

from concrete_pizzas import Margherita, VegDelight, FarmHouse
from concrete_decorators import ExtraCheese, Mushroom


def print_order(description: str, pizza):
    """Helper function to print pizza order and cost."""
    print(f"{description}: ₹{pizza.cost()}")


def main():
    print("=" * 50)
    print("DECORATOR PATTERN - PIZZA BILLING SYSTEM")
    print("=" * 50)
    print()
    
    # Example 1: Base pizzas without any toppings
    print("1. BASE PIZZAS (No Toppings)")
    print("-" * 50)
    margherita = Margherita()
    print_order("Margherita Pizza", margherita)
    
    veg_delight = VegDelight()
    print_order("Veg Delight Pizza", veg_delight)
    
    farm_house = FarmHouse()
    print_order("Farm House Pizza", farm_house)
    print()
    
    # Example 2: Pizzas with single topping
    print("2. PIZZAS WITH SINGLE TOPPING")
    print("-" * 50)
    margherita_with_cheese = ExtraCheese(Margherita())
    print_order("Margherita + Extra Cheese", margherita_with_cheese)
    
    veg_delight_with_mushroom = Mushroom(VegDelight())
    print_order("Veg Delight + Mushroom", veg_delight_with_mushroom)
    print()
    
    # Example 3: Pizzas with multiple toppings (nested decorators)
    print("3. PIZZAS WITH MULTIPLE TOPPINGS")
    print("-" * 50)
    margherita_deluxe = Mushroom(ExtraCheese(Margherita()))
    print_order("Margherita + Extra Cheese + Mushroom", margherita_deluxe)
    
    veg_delight_deluxe = ExtraCheese(Mushroom(VegDelight()))
    print_order("Veg Delight + Mushroom + Extra Cheese", veg_delight_deluxe)
    
    farm_house_deluxe = Mushroom(ExtraCheese(FarmHouse()))
    print_order("Farm House + Extra Cheese + Mushroom", farm_house_deluxe)
    print()
    
    # Example 4: Double toppings
    print("4. PIZZAS WITH DOUBLE TOPPINGS")
    print("-" * 50)
    extra_cheesy = ExtraCheese(ExtraCheese(Margherita()))
    print_order("Margherita + Double Extra Cheese", extra_cheesy)
    
    mushroom_lover = Mushroom(Mushroom(VegDelight()))
    print_order("Veg Delight + Double Mushroom", mushroom_lover)
    print()
    
    print("=" * 50)
    print("Pattern Benefits:")
    print("- No class explosion (no need for MargheritaWithCheese class)")
    print("- Flexible: Add toppings dynamically at runtime")
    print("- Open/Closed Principle: Open for extension, closed for modification")
    print("=" * 50)


if __name__ == "__main__":
    main()
