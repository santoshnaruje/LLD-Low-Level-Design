from abc import ABC, abstractmethod

from src.duck.flyble import FlyBehavior
from src.duck.quackable import QuackableBehavior


class Duck(ABC):
    """Context: delegates flying and quacking to composed strategy objects."""

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackableBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError("Subclasses must implement display()")

    def fly(self) -> None:
        self.fly_behavior.fly()

    def quack(self) -> None:
        self.quack_behavior.quack()

    def swim(self) -> None:
        print("All ducks float, even decoys!")

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackableBehavior) -> None:
        self.quack_behavior = quack_behavior
