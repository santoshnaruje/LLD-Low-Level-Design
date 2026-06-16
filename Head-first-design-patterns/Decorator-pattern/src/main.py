from src.beverage.beverages import HouseBlend, DarkRoast, Decaf, Espresso
from src.condiments.condiments import Milk, Mocha, Soy, Whip


def print_order(beverage) -> None:
    """Helper: print a beverage's description and cost in Starbuzz receipt style."""
    print(f"{beverage.get_description()} ${beverage.cost():.2f}")


if __name__ == "__main__":
    print("=== Starbuzz Coffee — Decorator Pattern Demo ===\n")

    # --- Order 1: plain Espresso ---
    espresso = Espresso()
    print_order(espresso)

    # --- Order 2: DarkRoast + double Mocha + Whip ---
    dark_roast = DarkRoast()
    dark_roast = Mocha(dark_roast)   # first shot of mocha
    dark_roast = Mocha(dark_roast)   # second shot of mocha
    dark_roast = Whip(dark_roast)    # topped with whip
    print_order(dark_roast)

    # --- Order 3: HouseBlend + Soy + Mocha + Whip ---
    house_blend = HouseBlend()
    house_blend = Soy(house_blend)
    house_blend = Mocha(house_blend)
    house_blend = Whip(house_blend)
    print_order(house_blend)

    # --- Order 4: Decaf + Milk ---
    decaf = Decaf()
    decaf = Milk(decaf)
    print_order(decaf)
