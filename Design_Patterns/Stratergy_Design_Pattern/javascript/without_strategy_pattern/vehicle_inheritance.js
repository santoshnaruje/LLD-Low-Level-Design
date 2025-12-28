/**
 * WITHOUT STRATEGY PATTERN - The Problem (JavaScript)
 * ====================================================
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
    drive() {
        console.log("Normal drive capability");
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
    drive() {
        // ❌ DUPLICATED CODE - Same as OffRoadVehicle
        console.log("Sports drive capability - Special driving features!");
    }
}

/**
 * OffRoad Vehicle - Also needs special drive capability
 */
class OffRoadVehicle extends Vehicle {
    drive() {
        // ❌ DUPLICATED CODE - Same as SportsVehicle
        // If we need to change this, we have to change it in multiple places!
        console.log("Sports drive capability - Special driving features!");
    }
}

// ============================================================================
// DEMO - Shows the Problem
// ============================================================================

console.log("=== WITHOUT Strategy Pattern - The Problem ===\n");

const normalVehicle = new NormalVehicle();
const sportsVehicle = new SportsVehicle();
const offRoadVehicle = new OffRoadVehicle();

process.stdout.write("Normal Vehicle: ");
normalVehicle.drive();

process.stdout.write("Sports Vehicle: ");
sportsVehicle.drive();

process.stdout.write("OffRoad Vehicle: ");
offRoadVehicle.drive();

console.log("\n❌ PROBLEM: SportsVehicle and OffRoadVehicle have DUPLICATED code!");
console.log("❌ If we need to change the sports drive behavior, we have to change it in 2 places!");
console.log("❌ This violates the DRY (Don't Repeat Yourself) principle!");
