class Pizza:

    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

class PizzaBuilder():
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.items.append('chesse')
        return self

    def add_olives(self):
        self.pizza.items.append('olives')
        return self

    def add_pepper(self):
        self.pizza.items.append('pepper')
        return self

    def build(self):
        return self.pizza

if __name__ == '__main__':
    builder=PizzaBuilder().add_cheese().add_olives().add_pepper().build()
    builder.show()






