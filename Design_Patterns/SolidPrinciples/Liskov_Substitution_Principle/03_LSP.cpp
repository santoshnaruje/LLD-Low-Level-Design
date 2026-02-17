#include <iostream>

// TITLE: Liskov Substitution Principle (LSP) - Vehicle Example

// THE PROBLEM (VIOLATION):
// Vehicle base class with hasEngine() method
// Bicycle doesn't have an engine, violating the contract

class Vehicle {
public:
    virtual int getNumberOfWheels() = 0;
    virtual bool hasEngine() = 0; // Problem: Not all vehicles have engines!
    virtual ~Vehicle() {}
};

class MotorCycle : public Vehicle {
public:
    int getNumberOfWheels() override { return 2; }
    bool hasEngine() override { return true; }
};

class Car : public Vehicle {
public:
    int getNumberOfWheels() override { return 4; }
    bool hasEngine() override { return true; }
};

class Bicycle : public Vehicle {
public:
    int getNumberOfWheels() override { return 2; }
    bool hasEngine() override {
        // Violation! Bicycle doesn't have an engine
        // Forced to return false or throw exception
        return false; // Misleading!
    }
};

// THE SOLUTION:
// Separate vehicles with engines from those without

class VehicleGood {
public:
    virtual int getNumberOfWheels() = 0;
    virtual ~VehicleGood() {}
};

class EngineVehicle : public VehicleGood {
public:
    virtual bool hasEngine() { return true; }
};

class MotorCycleGood : public EngineVehicle {
public:
    int getNumberOfWheels() override { return 2; }
};

class CarGood : public EngineVehicle {
public:
    int getNumberOfWheels() override { return 4; }
};

class BicycleGood : public VehicleGood {
public:
    int getNumberOfWheels() override { return 2; }
    // No hasEngine() method - doesn't apply!
};

int main() {
    std::cout << "=== PROBLEM (LSP Violation) ===" << std::endl;
    Bicycle bicycle;
    std::cout << "Bicycle wheels: " << bicycle.getNumberOfWheels() << std::endl;
    std::cout << "Bicycle has engine: " << (bicycle.hasEngine() ? "Yes" : "No") 
              << " (Misleading!)" << std::endl;
    
    std::cout << "\n=== SOLUTION (LSP Compliant) ===" << std::endl;
    BicycleGood bicycleGood;
    std::cout << "Bicycle wheels: " << bicycleGood.getNumberOfWheels() << std::endl;
    std::cout << "Bicycle doesn't need hasEngine() method!" << std::endl;
    
    CarGood car;
    std::cout << "Car wheels: " << car.getNumberOfWheels() << std::endl;
    std::cout << "Car has engine: " << (car.hasEngine() ? "Yes" : "No") << std::endl;
    
    return 0;
}
