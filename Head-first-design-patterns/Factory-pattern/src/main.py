"""Factory Pattern demo — Pizza Store (Head First Design Patterns, Chapter 4).

This script demonstrates the three-stage progression the book teaches:

  Stage 1 — Simple Factory
      A static helper removes the big if/elif from the client code.
      Easy to understand, but the factory itself is not swappable and violates
      the Open/Closed Principle when new types are added.

  Stage 2 — Factory Method Pattern
      PizzaStore.order_pizza() is the stable, high-level algorithm.
      PizzaStore.create_pizza() is the abstract factory method.
      NYPizzaStore and ChicagoPizzaStore each override create_pizza() to
      decide which concrete Pizza class to instantiate.
      Result: subclasses decide what to create; the creator never imports
      concrete product classes directly.

  Stage 3 — Abstract Factory Pattern
      Each concrete pizza is injected with a PizzaIngredientFactory.
      NYPizzaIngredientFactory and ChicagoPizzaIngredientFactory each return
      a full, regionally-coherent *family* of ingredients.
      Result: the same CheesePizza class produces an NY or Chicago pie purely
      based on which factory was given to it — no conditional logic anywhere.
"""

from src.store.ny_pizza_store import NYPizzaStore
from src.store.chicago_pizza_store import ChicagoPizzaStore


def separator(title: str) -> None:
    width = 58
    print(f"\n{'═' * width}")
    print(f"  {title}")
    print(f"{'═' * width}")


if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════╗")
    print("║   Pizza Store — Factory Pattern Demo                ║")
    print("║   Head First Design Patterns, Chapter 4             ║")
    print("╚══════════════════════════════════════════════════════╝")

    # ── New York Pizza Store ───────────────────────────────────────────────────
    separator("NEW YORK PIZZA STORE")
    ny_store = NYPizzaStore()

    ny_cheese = ny_store.order_pizza("cheese")
    print(f"\n{ny_cheese}\n")

    ny_clam = ny_store.order_pizza("clam")
    print(f"\n{ny_clam}\n")

    ny_veggie = ny_store.order_pizza("veggie")
    print(f"\n{ny_veggie}\n")

    ny_pepperoni = ny_store.order_pizza("pepperoni")
    print(f"\n{ny_pepperoni}\n")

    # ── Chicago Pizza Store ────────────────────────────────────────────────────
    separator("CHICAGO PIZZA STORE  (Deep Dish)")
    chicago_store = ChicagoPizzaStore()

    chi_cheese = chicago_store.order_pizza("cheese")
    print(f"\n{chi_cheese}\n")

    chi_clam = chicago_store.order_pizza("clam")
    print(f"\n{chi_clam}\n")

    chi_veggie = chicago_store.order_pizza("veggie")
    print(f"\n{chi_veggie}\n")

    chi_pepperoni = chicago_store.order_pizza("pepperoni")
    print(f"\n{chi_pepperoni}\n")

    # ── Pattern summary ────────────────────────────────────────────────────────
    separator("PATTERN SUMMARY")
    print("  Factory Method  : NYPizzaStore / ChicagoPizzaStore")
    print("                    override create_pizza() to choose")
    print("                    which concrete Pizza to instantiate.")
    print()
    print("  Abstract Factory: NYPizzaIngredientFactory /")
    print("                    ChicagoPizzaIngredientFactory produce")
    print("                    a coherent regional ingredient family.")
    print()
    print("  Design Principle: Depend on abstractions, not concretions.")
    print("                    (Dependency Inversion Principle)")
    print(f"\n{'═' * 58}\n")
