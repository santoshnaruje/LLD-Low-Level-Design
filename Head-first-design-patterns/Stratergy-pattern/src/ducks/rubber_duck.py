from src.duck.duck import Duck
from src.duck.flyble import NoFlyBehaviour
from src.duck.quackable import Squackable


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__(NoFlyBehaviour(), Squackable())

    def display(self) -> None:
        print("Rubber duck")
