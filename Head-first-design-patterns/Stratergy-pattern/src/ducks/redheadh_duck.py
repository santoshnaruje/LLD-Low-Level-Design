from src.duck.duck import Duck
from src.duck.flyble import FlyWithWings
from src.duck.quackable import Quack


class ReadHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> None:
        print("Redhead")
