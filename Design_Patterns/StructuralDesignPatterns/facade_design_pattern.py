from Design_Patterns.StructuralDesignPatterns.bridge_design_pattern import Device
from Design_Patterns.StructuralDesignPatterns.composite_design_pattern import FileSystem


class Inventory:
    def update(self):
        print('Inventory updated')


class Payment:
    def pay(self):
        print('Payment paid')


class shipping:
    def ship(self):
        print('Item shipping started')

class OrderFacade:

    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.ship = shipping()

    def make_order(self):
        self.payment.pay()
        self.ship.ship()
        self.inventory.update()

if __name__ == '__main__':
    order = OrderFacade()
    order.make_order()