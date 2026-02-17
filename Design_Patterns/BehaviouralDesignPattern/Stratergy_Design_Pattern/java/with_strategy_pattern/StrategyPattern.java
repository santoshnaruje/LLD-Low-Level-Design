/**
 * STRATEGY DESIGN PATTERN - Vehicle Example
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
// STRATEGY INTERFACE
// ============================================================================

/**
 * Strategy Interface - Defines the contract for all drive strategies
 */
interface DriveStrategy {
    void drive();
}

// ============================================================================
// CONCRETE STRATEGIES
// ============================================================================

/**
 * Normal Drive Strategy - Used by regular vehicles
 */
class NormalDriveStrategy implements DriveStrategy {
    @Override
    public void drive() {
        System.out.println("Normal drive capability");
    }
}

/**
 * Sports Drive Strategy - Used by high-performance vehicles
 */
class SportsDriveStrategy implements DriveStrategy {
    @Override
    public void drive() {
        System.out.println("Sports drive capability - Special driving features!");
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
    // Strategy object - composition
    private DriveStrategy driveStrategy;
    
    // Constructor injection - allows setting strategy at creation time
    public Vehicle(DriveStrategy driveStrategy) {
        this.driveStrategy = driveStrategy;
    }
    
    // Delegates to the strategy
    public void drive() {
        driveStrategy.drive();
    }
}

// ============================================================================
// CONCRETE VEHICLES
// ============================================================================

/**
 * Normal Vehicle - Uses normal drive strategy
 */
class NormalVehicle extends Vehicle {
    public NormalVehicle() {
        super(new NormalDriveStrategy());
    }
}

/**
 * Sports Vehicle - Uses sports drive strategy
 */
class SportsVehicle extends Vehicle {
    public SportsVehicle() {
        super(new SportsDriveStrategy());
    }
}

/**
 * OffRoad Vehicle - Also uses sports drive strategy
 * Notice: No code duplication! Both SportsVehicle and OffRoadVehicle
 * share the same SportsDriveStrategy instance behavior
 */
class OffRoadVehicle extends Vehicle {
    public OffRoadVehicle() {
        super(new SportsDriveStrategy());
    }
}

// ============================================================================
// DEMO
// ============================================================================

public class StrategyPattern {
    public static void main(String[] args) {
        System.out.println("=== Strategy Design Pattern Demo ===\n");
        
        // Create different vehicles
        Vehicle normalVehicle = new NormalVehicle();
        Vehicle sportsVehicle = new SportsVehicle();
        Vehicle offRoadVehicle = new OffRoadVehicle();
        
        // Each vehicle uses its assigned strategy
        System.out.print("Normal Vehicle: ");
        normalVehicle.drive();
        
        System.out.print("Sports Vehicle: ");
        sportsVehicle.drive();
        
        System.out.print("OffRoad Vehicle: ");
        offRoadVehicle.drive();
        
        System.out.println("\n✓ Notice: Sports and OffRoad vehicles share the same strategy");
        System.out.println("✓ No code duplication!");
    }
}
