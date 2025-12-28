from abc import ABC, abstractmethod

# TITLE: Liskov Substitution Principle (LSP) - Vehicle Example
# Source: Shrayansh Jain's video (129QkkXUHeQ)

# THE PROBLEM (VIOLATION):
class Vehicle(ABC):
    @abstractmethod
    def get_number_of_wheels(self): pass
    
    @abstractmethod
    def has_engine(self): pass  # Problem: Not all vehicles have engines!

class MotorCycle(Vehicle):
    def get_number_of_wheels(self): return 2
    def has_engine(self): return True

class Car(Vehicle):
    def get_number_of_wheels(self): return 4
    def has_engine(self): return True

class Bicycle(Vehicle):
    def get_number_of_wheels(self): return 2
    def has_engine(self):
        # Violation! Bicycle doesn't have an engine
        return False  # Misleading!

# THE SOLUTION:
class VehicleGood(ABC):
    @abstractmethod
    def get_number_of_wheels(self): pass

class EngineVehicle(VehicleGood):
    def has_engine(self): return True

class MotorCycleGood(EngineVehicle):
    def get_number_of_wheels(self): return 2

class CarGood(EngineVehicle):
    def get_number_of_wheels(self): return 4

class BicycleGood(VehicleGood):
    def get_number_of_wheels(self): return 2
    # No has_engine() method - doesn't apply!

if __name__ == "__main__":
    print("=== PROBLEM (LSP Violation) ===")
    bicycle = Bicycle()
    print(f"Bicycle wheels: {bicycle.get_number_of_wheels()}")
    print(f"Bicycle has engine: {bicycle.has_engine()} (Misleading!)")
    
    print("\n=== SOLUTION (LSP Compliant) ===")
    bicycle_good = BicycleGood()
    print(f"Bicycle wheels: {bicycle_good.get_number_of_wheels()}")
    print("Bicycle doesn't need has_engine() method!")
    
    car = CarGood()
    print(f"Car wheels: {car.get_number_of_wheels()}")
    print(f"Car has engine: {car.has_engine()}")
