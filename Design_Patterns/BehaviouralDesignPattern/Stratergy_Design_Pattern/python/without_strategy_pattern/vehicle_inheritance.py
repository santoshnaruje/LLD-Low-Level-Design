"""
WITHOUT STRATEGY PATTERN - The Problem (Python)
================================================

This example demonstrates the PROBLEM with traditional inheritance:
- Code duplication when multiple classes need the same behavior
- Difficult to maintain (changes need to be made in multiple places)
- Violates DRY (Don't Repeat Yourself) principle

Problem: Both SportsVehicle and OffRoadVehicle need the same "sports drive"
capability, but we have to duplicate the code in both classes!
"""

# ============================================================================
# BASE CLASS
# ============================================================================

class Vehicle:
    """
    Vehicle base class with a drive method
    """
    
    def drive(self):
        print("Normal drive capability")


# ============================================================================
# CONCRETE CLASSES - Notice the Code Duplication!
# ============================================================================

class NormalVehicle(Vehicle):
    """
    Normal Vehicle - Uses the default drive from base class
    """
    # Inherits normal drive - no override needed
    pass


class SportsVehicle(Vehicle):
    """
    Sports Vehicle - Needs special drive capability
    """
    
    def drive(self):
        # ❌ DUPLICATED CODE - Same as OffRoadVehicle
        print("Sports drive capability - Special driving features!")


class OffRoadVehicle(Vehicle):
    """
    OffRoad Vehicle - Also needs special drive capability
    """
    
    def drive(self):
        # ❌ DUPLICATED CODE - Same as SportsVehicle
        # If we need to change this, we have to change it in multiple places!
        print("Sports drive capability - Special driving features!")


# ============================================================================
# DEMO - Shows the Problem
# ============================================================================

def main():
    print("=== WITHOUT Strategy Pattern - The Problem ===\n")
    
    normal_vehicle = NormalVehicle()
    sports_vehicle = SportsVehicle()
    offroad_vehicle = OffRoadVehicle()
    
    print("Normal Vehicle: ", end="")
    normal_vehicle.drive()
    
    print("Sports Vehicle: ", end="")
    sports_vehicle.drive()
    
    print("OffRoad Vehicle: ", end="")
    offroad_vehicle.drive()
    
    print("\n❌ PROBLEM: SportsVehicle and OffRoadVehicle have DUPLICATED code!")
    print("❌ If we need to change the sports drive behavior, we have to change it in 2 places!")
    print("❌ This violates the DRY (Don't Repeat Yourself) principle!")


if __name__ == "__main__":
    main()
