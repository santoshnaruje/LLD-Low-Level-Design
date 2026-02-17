/**
 * STRATEGY DESIGN PATTERN - Vehicle Example (JavaScript)
 * 
 * Problem: Without Strategy Pattern
 * ====================================
 * When using traditional inheritance, if multiple vehicle types need the same
 * special behavior (e.g., SportsCar and OffRoadVehicle both need sports drive),
 * we end up duplicating code in multiple classes.
 * 
 * Solution: Strategy Pattern
 * ==========================
 * - Define a family of algorithms (drive strategies)
 * - Encapsulate each algorithm in a separate class
 * - Make them interchangeable through a common interface
 * - Use composition instead of inheritance
 * 
 * Benefits:
 * - No code duplication
 * - Easy to add new strategies
 * - Runtime flexibility to change behavior
 */

// ============================================================================
// STRATEGY CLASSES (No interface needed in JavaScript)
// ============================================================================

/**
 * Normal Drive Strategy - Used by regular vehicles
 */
class NormalDriveStrategy {
    drive() {
        console.log("Normal drive capability");
    }
}

/**
 * Sports Drive Strategy - Used by high-performance vehicles
 */
class SportsDriveStrategy {
    drive() {
        console.log("Sports drive capability - Special driving features!");
    }
}

// ============================================================================
// CONTEXT - Vehicle Base Class
// ============================================================================

/**
 * Vehicle class uses composition to delegate drive behavior to a strategy
 * This is the key principle: "HAS-A" relationship instead of "IS-A"
 */
class Vehicle {
    /**
     * Constructor injection - allows setting strategy at creation time
     * @param {Object} driveStrategy - The drive strategy to use
     */
    constructor(driveStrategy) {
        this.driveStrategy = driveStrategy;
    }

    /**
     * Delegates to the strategy
     */
    drive() {
        this.driveStrategy.drive();
    }
}

// ============================================================================
// CONCRETE VEHICLES
// ============================================================================

/**
 * Normal Vehicle - Uses normal drive strategy
 */
class NormalVehicle extends Vehicle {
    constructor() {
        super(new NormalDriveStrategy());
    }
}

/**
 * Sports Vehicle - Uses sports drive strategy
 */
class SportsVehicle extends Vehicle {
    constructor() {
        super(new SportsDriveStrategy());
    }
}

/**
 * OffRoad Vehicle - Also uses sports drive strategy
 * Notice: No code duplication! Both SportsVehicle and OffRoadVehicle
 * share the same SportsDriveStrategy behavior
 */
class OffRoadVehicle extends Vehicle {
    constructor() {
        super(new SportsDriveStrategy());
    }
}

// ============================================================================
// DEMO
// ============================================================================

console.log("=== Strategy Design Pattern Demo ===\n");

// Create different vehicles
const normalVehicle = new NormalVehicle();
const sportsVehicle = new SportsVehicle();
const offRoadVehicle = new OffRoadVehicle();

// Each vehicle uses its assigned strategy
process.stdout.write("Normal Vehicle: ");
normalVehicle.drive();

process.stdout.write("Sports Vehicle: ");
sportsVehicle.drive();

process.stdout.write("OffRoad Vehicle: ");
offRoadVehicle.drive();

console.log("\n✓ Notice: Sports and OffRoad vehicles share the same strategy");
console.log("✓ No code duplication!");
