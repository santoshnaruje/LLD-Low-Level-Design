"""Abstract Factory: interface for creating a coordinated family of ingredients.

This is the heart of the Abstract Factory pattern in chapter 4.

The key insight: PizzaIngredientFactory defines *what* ingredients a pizza
needs, without saying *which* concrete ingredient objects are returned.
Each concrete factory (NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory)
provides a regionally-coherent set of ingredients.

The pizza classes call these factory methods inside their prepare() step, so
they are completely decoupled from the concrete ingredient classes.
"""

from abc import ABC, abstractmethod
from typing import List


class PizzaIngredientFactory(ABC):
    """Abstract Factory that produces a coordinated family of pizza ingredients.

    Each concrete subclass must implement all six factory methods, guaranteeing
    that every ingredient returned belongs to the same regional style.

    Design Principle — Dependency Inversion:
        High-level components (Pizza, PizzaStore) depend on this abstraction,
        not on concrete ThinCrustDough or MarinaraSauce classes.
    """

    @abstractmethod
    def create_dough(self):
        """Return the regional dough ingredient."""
        pass

    @abstractmethod
    def create_sauce(self):
        """Return the regional sauce ingredient."""
        pass

    @abstractmethod
    def create_cheese(self):
        """Return the regional cheese ingredient."""
        pass

    @abstractmethod
    def create_veggies(self) -> List:
        """Return a list of regional veggie ingredients."""
        pass

    @abstractmethod
    def create_pepperoni(self):
        """Return the regional pepperoni ingredient."""
        pass

    @abstractmethod
    def create_clam(self):
        """Return the regional clam ingredient."""
        pass
