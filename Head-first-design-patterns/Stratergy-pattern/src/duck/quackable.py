from abc import ABC, abstractmethod


class QuackableBehavior(ABC):

    @abstractmethod
    def quack(self) -> None:
        pass


class Quack(QuackableBehavior):
    def quack(self) -> None:
        print("Quack")


class Squackable(QuackableBehavior):
    def quack(self) -> None:
        print("Squeak")


class MuteQuack(QuackableBehavior):
    def quack(self) -> None:
        print("<< silence >>")
