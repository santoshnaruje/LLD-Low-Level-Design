from abc import ABC, abstractmethod


class Beverage(ABC):

    def prepare(self):
        self.add_milk()
        self.add_ingredients()
        self.add_water()
        self.pour_into_cup()

    def add_milk(self):
        print("Adding milk")

    @abstractmethod
    def add_ingredients(self):
        pass

    def add_water(self):
        print("Adding water")

    def pour_into_cup(self):
        print("Pouring into cup")

class Tea(Beverage):

    def __init__(self, tea_powder):
        self.tea_powder = tea_powder

    def add_ingredients(self):
        print(f"Adding {self.tea_powder} to Milk")

class Coffee(Beverage):

    def __init__(self, coffee_powder):
        self.coffee_powder = coffee_powder

    def add_ingredients(self):
        print(f"Adding {self.coffee_powder} to Milk")

if __name__ == "__main__":
    tea=Tea("Red Label")
    tea.prepare()

    coffee=Coffee("Coffee")
    coffee.prepare() 
