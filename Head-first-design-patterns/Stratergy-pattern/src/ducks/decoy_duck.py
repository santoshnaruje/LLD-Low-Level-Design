from src.duck.duck import Duck
from src.duck.flyble import NoFlyBehaviour
from src.duck.quackable import MuteQuack


class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__(NoFlyBehaviour(), MuteQuack())

    def display(self) -> None:
        print("Wooden decoy")
