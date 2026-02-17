/**
 * STRATEGY DESIGN PATTERN - Vehicle Example (C++)
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

#include <iostream>
#include <memory>
using namespace std;

// ============================================================================
// STRATEGY INTERFACE
// ============================================================================

/**
 * Strategy Interface - Defines the contract for all drive strategies
 */
class DriveStrategy {
public:
    virtual void drive() = 0;  // Pure virtual function
    virtual ~DriveStrategy() {}  // Virtual destructor for proper cleanup
};

// ============================================================================
// CONCRETE STRATEGIES
// ============================================================================

/**
 * Normal Drive Strategy - Used by regular vehicles
 */
class NormalDriveStrategy : public DriveStrategy {
public:
    void drive() override {
        cout << "Normal drive capability" << endl;
    }
};

/**
 * Sports Drive Strategy - Used by high-performance vehicles
 */
class SportsDriveStrategy : public DriveStrategy {
public:
    void drive() override {
        cout << "Sports drive capability - Special driving features!" << endl;
    }
};

// ============================================================================
// CONTEXT - Vehicle Base Class
// ============================================================================

/**
 * Vehicle class uses composition to delegate drive behavior to a strategy
 * This is the key principle: "HAS-A" relationship instead of "IS-A"
 */
class Vehicle {
protected:
    DriveStrategy* driveStrategy;  // Strategy object - composition
    
public:
    // Constructor injection - allows setting strategy at creation time
    Vehicle(DriveStrategy* strategy) : driveStrategy(strategy) {}
    
    // Delegates to the strategy
    virtual void drive() {
        driveStrategy->drive();
    }
    
    // Virtual destructor
    virtual ~Vehicle() {
        delete driveStrategy;
    }
};

// ============================================================================
// CONCRETE VEHICLES
// ============================================================================

/**
 * Normal Vehicle - Uses normal drive strategy
 */
class NormalVehicle : public Vehicle {
public:
    NormalVehicle() : Vehicle(new NormalDriveStrategy()) {}
};

/**
 * Sports Vehicle - Uses sports drive strategy
 */
class SportsVehicle : public Vehicle {
public:
    SportsVehicle() : Vehicle(new SportsDriveStrategy()) {}
};

/**
 * OffRoad Vehicle - Also uses sports drive strategy
 * Notice: No code duplication! Both SportsVehicle and OffRoadVehicle
 * share the same SportsDriveStrategy behavior
 */
class OffRoadVehicle : public Vehicle {
public:
    OffRoadVehicle() : Vehicle(new SportsDriveStrategy()) {}
};

// ============================================================================
// DEMO
// ============================================================================

int main() {
    cout << "=== Strategy Design Pattern Demo ===" << endl << endl;
    
    // Create different vehicles
    Vehicle* normalVehicle = new NormalVehicle();
    Vehicle* sportsVehicle = new SportsVehicle();
    Vehicle* offRoadVehicle = new OffRoadVehicle();
    
    // Each vehicle uses its assigned strategy
    cout << "Normal Vehicle: ";
    normalVehicle->drive();
    
    cout << "Sports Vehicle: ";
    sportsVehicle->drive();
    
    cout << "OffRoad Vehicle: ";
    offRoadVehicle->drive();
    
    cout << endl;
    cout << "✓ Notice: Sports and OffRoad vehicles share the same strategy" << endl;
    cout << "✓ No code duplication!" << endl;
    
    // Cleanup
    delete normalVehicle;
    delete sportsVehicle;
    delete offRoadVehicle;
    
    return 0;
}
