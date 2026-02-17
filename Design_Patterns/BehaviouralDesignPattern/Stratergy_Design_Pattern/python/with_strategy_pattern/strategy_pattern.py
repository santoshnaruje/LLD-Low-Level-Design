"""
STRATEGY DESIGN PATTERN - Vehicle Example (Python)

Problem: Without Strategy Pattern
====================================
When using traditional inheritance, if multiple vehicle types need the same
special behavior (e.g., SportsCar and OffRoadVehicle both need sports drive),
we end up duplicating code in multiple classes.

Solution: Strategy Pattern
==========================
- Define a family of algorithms (drive strategies)
- Encapsulate each algorithm in a separate class
- Make them interchangeable through a common interface
- Use composition instead of inheritance

Benefits:
- No code duplication
- Easy to add new strategies
- Runtime flexibility to change behavior
"""

from abc import ABC, abstractmethod

# ============================================================================
# STRATEGY INTERFACE
# ============================================================================

class DriveStrategy(ABC):
    """
    Strategy Interface - Defines the contract for all drive strategies
    """
    
    @abstractmethod
    def drive(self):
        """Abstract method that must be implemented by concrete strategies"""
        pass


# ============================================================================
# CONCRETE STRATEGIES
# ============================================================================

class NormalDriveStrategy(DriveStrategy):
    """
    Normal Drive Strategy - Used by regular vehicles
    """
    
    def drive(self):
        print("Normal drive capability")


class SportsDriveStrategy(DriveStrategy):
    """
    Sports Drive Strategy - Used by high-performance vehicles
    """
    
    def drive(self):
        print("Sports drive capability - Special driving features!")


# ============================================================================
# CONTEXT - Vehicle Base Class
# ============================================================================

class Vehicle:
    """
    Vehicle class uses composition to delegate drive behavior to a strategy
    This is the key principle: "HAS-A" relationship instead of "IS-A"
    """
    
    def __init__(self, drive_strategy: DriveStrategy):
        """
        Constructor injection - allows setting strategy at creation time
        
        Args:
            drive_strategy: The drive strategy to use
        """
        self.drive_strategy = drive_strategy
    
    def drive(self):
        """Delegates to the strategy"""
        self.drive_strategy.drive()


# ============================================================================
# CONCRETE VEHICLES
# ============================================================================

class NormalVehicle(Vehicle):
    """
    Normal Vehicle - Uses normal drive strategy
    """
    
    def __init__(self):
        super().__init__(NormalDriveStrategy())


class SportsVehicle(Vehicle):
    """
    Sports Vehicle - Uses sports drive strategy
    """
    
    def __init__(self):
        super().__init__(SportsDriveStrategy())


class OffRoadVehicle(Vehicle):
    """
    OffRoad Vehicle - Also uses sports drive strategy
    Notice: No code duplication! Both SportsVehicle and OffRoadVehicle
    share the same SportsDriveStrategy behavior
    """
    
    def __init__(self):
        super().__init__(SportsDriveStrategy())


# ============================================================================
# DEMO
# ============================================================================

def main():
    print("=== Strategy Design Pattern Demo ===\n")
    
    # Create different vehicles
    normal_vehicle = NormalVehicle()
    sports_vehicle = SportsVehicle()
    offroad_vehicle = OffRoadVehicle()
    
    # Each vehicle uses its assigned strategy
    print("Normal Vehicle: ", end="")
    normal_vehicle.drive()
    
    print("Sports Vehicle: ", end="")
    sports_vehicle.drive()
    
    print("OffRoad Vehicle: ", end="")
    offroad_vehicle.drive()
    
    print("\n✓ Notice: Sports and OffRoad vehicles share the same strategy")
    print("✓ No code duplication!")


if __name__ == "__main__":
    main()
