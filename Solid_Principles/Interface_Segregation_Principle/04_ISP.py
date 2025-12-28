from abc import ABC, abstractmethod

# TITLE: Interface Segregation Principle (ISP) - Waiter Example

# ========================================
# THE PROBLEM (VIOLATION):
# Fat interface forces unnecessary methods
# ========================================

class RestaurantEmployeeBad(ABC):
    @abstractmethod
    def wash_dishes(self): pass
    @abstractmethod
    def serve_customer(self): pass
    @abstractmethod
    def cook_food(self): pass

class WaiterBad(RestaurantEmployeeBad):
    def wash_dishes(self):
        # Not my job!
        print("Waiter: Not my job to wash dishes")
    def serve_customer(self):
        print("Serving customer")
    def cook_food(self):
        # Not my job!
        print("Waiter: Not my job to cook")

# ========================================
# THE SOLUTION:
# Segregate interfaces
# ========================================

class WaiterInterface(ABC):
    @abstractmethod
    def serve_customer(self): pass
    @abstractmethod
    def take_order(self): pass

class ChefInterface(ABC):
    @abstractmethod
    def cook_food(self): pass
    @abstractmethod
    def decide_menu(self): pass

class Waiter(WaiterInterface):
    def serve_customer(self):
        print("Serving customer")
    def take_order(self):
        print("Taking order")

class Chef(ChefInterface):
    def cook_food(self):
        print("Cooking food")
    def decide_menu(self):
        print("Deciding menu")

if __name__ == "__main__":
    print("=== PROBLEM (ISP Violation) ===")
    waiter_bad = WaiterBad()
    waiter_bad.serve_customer()
    waiter_bad.cook_food()  # Forced to implement!
    waiter_bad.wash_dishes()  # Forced to implement!
    
    print("\n=== SOLUTION (ISP Compliant) ===")
    waiter = Waiter()
    waiter.serve_customer()
    waiter.take_order()
    
    chef = Chef()
    chef.cook_food()
    chef.decide_menu()
