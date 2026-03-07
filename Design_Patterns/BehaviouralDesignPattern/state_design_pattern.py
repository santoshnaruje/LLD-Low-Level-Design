# State Pattern allows an object to change its behavior when its internal state changes.

from abc import ABC, abstractmethod


# State interface
class ATMState(ABC):

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def withdraw_money(self):
        pass


class NoCardState(ATMState):

    def insert_card(self):
        print("Card inserted successfully")

    def withdraw_money(self):
        print("Insert card first")


class HasCardState(ATMState):
    def insert_card(self):
        print("Card inserted already")

    def withdraw_money(self):
        print("Enter pin first")

#Context
class ATM:
    def __init__(self):
        self.state = NoCardState()

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card()

    def withdraw_money(self):
        self.state.withdraw_money()


if __name__ == '__main__':
    atm = ATM()

    atm.withdraw_money()

    atm.insert_card()

    atm.set_state(HasCardState())

    atm.withdraw_money()



