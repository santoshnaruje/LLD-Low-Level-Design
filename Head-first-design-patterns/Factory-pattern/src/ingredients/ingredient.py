"""Concrete ingredient classes used by the PizzaIngredientFactory.

Each class is intentionally small — its entire job is to represent one
ingredient and provide a human-readable string so that Pizza.__str__()
can render a clean receipt.

The families are:
  Dough     — ThinCrustDough, ThickCrustDough
  Sauce     — MarinaraSauce, PlumTomatoSauce
  Cheese    — ReggianoCheese, MozzarellaCheese
  Veggies   — Garlic, Onion, Mushroom, RedPepper  (NY)
              Spinach, BlackOlives, EggPlant       (Chicago)
  Pepperoni — SlicedPepperoni (shared)
  Clam      — FreshClam, FrozenClam
"""


# ── Dough ─────────────────────────────────────────────────────────────────────

class ThinCrustDough:
    """NY-style thin, hand-tossed dough."""

    def __str__(self) -> str:
        return "Thin Crust Dough"


class ThickCrustDough:
    """Chicago deep-dish thick, pan-pressed dough."""

    def __str__(self) -> str:
        return "Thick Crust Dough"


# ── Sauce ─────────────────────────────────────────────────────────────────────

class MarinaraSauce:
    """Classic tangy marinara — the NY standard."""

    def __str__(self) -> str:
        return "Marinara Sauce"


class PlumTomatoSauce:
    """Rich, slow-cooked plum tomato sauce for Chicago deep dish."""

    def __str__(self) -> str:
        return "Plum Tomato Sauce"


# ── Cheese ────────────────────────────────────────────────────────────────────

class ReggianoCheese:
    """Sharp, aged Parmigiano-Reggiano used in NY-style pies."""

    def __str__(self) -> str:
        return "Reggiano Cheese"


class MozzarellaCheese:
    """Shredded low-moisture mozzarella — the Chicago deep-dish staple."""

    def __str__(self) -> str:
        return "Shredded Mozzarella"


# ── Veggies ───────────────────────────────────────────────────────────────────

class Garlic:
    def __str__(self) -> str:
        return "Garlic"


class Onion:
    def __str__(self) -> str:
        return "Onion"


class Mushroom:
    def __str__(self) -> str:
        return "Mushroom"


class RedPepper:
    def __str__(self) -> str:
        return "Red Pepper"


class Spinach:
    def __str__(self) -> str:
        return "Spinach"


class BlackOlives:
    def __str__(self) -> str:
        return "Black Olives"


class EggPlant:
    def __str__(self) -> str:
        return "Egg Plant"


# ── Pepperoni ─────────────────────────────────────────────────────────────────

class SlicedPepperoni:
    """Thinly sliced cured pepperoni — shared across both regions."""

    def __str__(self) -> str:
        return "Sliced Pepperoni"


# ── Clam ──────────────────────────────────────────────────────────────────────

class FreshClam:
    """Fresh clams sourced from Long Island Sound — the NY choice."""

    def __str__(self) -> str:
        return "Fresh Clams from Long Island Sound"


class FrozenClam:
    """Frozen clams from Chesapeake Bay — what Chicago has access to."""

    def __str__(self) -> str:
        return "Frozen Clams from Chesapeake Bay"
