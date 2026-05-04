from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self) -> None:
        pass


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!!")


class NoFlyBehaviour(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")
