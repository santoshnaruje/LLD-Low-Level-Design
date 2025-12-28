/**
 * WITHOUT STRATEGY PATTERN - The Problem
 * ========================================
 * 
 * This example demonstrates the PROBLEM with traditional inheritance:
 * - Code duplication when multiple classes need the same behavior
 * - Difficult to maintain (changes need to be made in multiple places)
 * - Violates DRY (Don't Repeat Yourself) principle
 * 
 * Problem: Both SportsVehicle and OffRoadVehicle need the same "sports drive"
 * capability, but we have to duplicate the code in both classes!
 */

// ============================================================================
// BASE CLASS
// ============================================================================

/**
 * Vehicle base class with a drive method
 */
class Vehicle {
    public void drive() {
        System.out.println("Normal drive capability");
    }
}

// ============================================================================
// CONCRETE CLASSES - Notice the Code Duplication!
// ============================================================================

/**
 * Normal Vehicle - Uses the default drive from base class
 */
class NormalVehicle extends Vehicle {
    // Inherits normal drive - no override needed
}

/**
 * Sports Vehicle - Needs special drive capability
 */
class SportsVehicle extends Vehicle {
    @Override
    public void drive() {
        // ❌ DUPLICATED CODE - Same as OffRoadVehicle
        System.out.println("Sports drive capability - Special driving features!");
    }
}

/**
 * OffRoad Vehicle - Also needs special drive capability
 */
class OffRoadVehicle extends Vehicle {
    @Override
    public void drive() {
        // ❌ DUPLICATED CODE - Same as SportsVehicle
        // If we need to change this, we have to change it in multiple places!
        System.out.println("Sports drive capability - Special driving features!");
    }
}

// ============================================================================
// DEMO - Shows the Problem
// ============================================================================

public class VehicleInheritance {
    public static void main(String[] args) {
        System.out.println("=== WITHOUT Strategy Pattern - The Problem ===\n");

        Vehicle normalVehicle = new NormalVehicle();
        Vehicle sportsVehicle = new SportsVehicle();
        Vehicle offRoadVehicle = new OffRoadVehicle();

        System.out.print("Normal Vehicle: ");
        normalVehicle.drive();

        System.out.print("Sports Vehicle: ");
        sportsVehicle.drive();

        System.out.print("OffRoad Vehicle: ");
        offRoadVehicle.drive();

        System.out.println("\n❌ PROBLEM: SportsVehicle and OffRoadVehicle have DUPLICATED code!");
        System.out.println("❌ If we need to change the sports drive behavior, we have to change it in 2 places!");
        System.out.println("❌ This violates the DRY (Don't Repeat Yourself) principle!");
    }
}
