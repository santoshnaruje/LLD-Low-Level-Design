/**
 * WITHOUT STRATEGY PATTERN - The Problem (C++)
 * ==============================================
 * 
 * This example demonstrates the PROBLEM with traditional inheritance:
 * - Code duplication when multiple classes need the same behavior
 * - Difficult to maintain (changes need to be made in multiple places)
 * - Violates DRY (Don't Repeat Yourself) principle
 * 
 * Problem: Both SportsVehicle and OffRoadVehicle need the same "sports drive"
 * capability, but we have to duplicate the code in both classes!
 */

#include <iostream>
using namespace std;

// ============================================================================
// BASE CLASS
// ============================================================================

/**
 * Vehicle base class with a drive method
 */
class Vehicle {
public:
    virtual void drive() {
        cout << "Normal drive capability" << endl;
    }
    
    virtual ~Vehicle() {}
};

// ============================================================================
// CONCRETE CLASSES - Notice the Code Duplication!
// ============================================================================

/**
 * Normal Vehicle - Uses the default drive from base class
 */
class NormalVehicle : public Vehicle {
    // Inherits normal drive - no override needed
};

/**
 * Sports Vehicle - Needs special drive capability
 */
class SportsVehicle : public Vehicle {
public:
    void drive() override {
        // ❌ DUPLICATED CODE - Same as OffRoadVehicle
        cout << "Sports drive capability - Special driving features!" << endl;
    }
};

/**
 * OffRoad Vehicle - Also needs special drive capability
 */
class OffRoadVehicle : public Vehicle {
public:
    void drive() override {
        // ❌ DUPLICATED CODE - Same as SportsVehicle
        // If we need to change this, we have to change it in multiple places!
        cout << "Sports drive capability - Special driving features!" << endl;
    }
};

// ============================================================================
// DEMO - Shows the Problem
// ============================================================================

int main() {
    cout << "=== WITHOUT Strategy Pattern - The Problem ===" << endl << endl;
    
    Vehicle* normalVehicle = new NormalVehicle();
    Vehicle* sportsVehicle = new SportsVehicle();
    Vehicle* offRoadVehicle = new OffRoadVehicle();
    
    cout << "Normal Vehicle: ";
    normalVehicle->drive();
    
    cout << "Sports Vehicle: ";
    sportsVehicle->drive();
    
    cout << "OffRoad Vehicle: ";
    offRoadVehicle->drive();
    
    cout << endl;
    cout << "❌ PROBLEM: SportsVehicle and OffRoadVehicle have DUPLICATED code!" << endl;
    cout << "❌ If we need to change the sports drive behavior, we have to change it in 2 places!" << endl;
    cout << "❌ This violates the DRY (Don't Repeat Yourself) principle!" << endl;
    
    // Cleanup
    delete normalVehicle;
    delete sportsVehicle;
    delete offRoadVehicle;
    
    return 0;
}
