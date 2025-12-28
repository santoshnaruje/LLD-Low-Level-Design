// TITLE: Liskov Substitution Principle (LSP) - Vehicle Example

// THE PROBLEM (VIOLATION):
class Vehicle {
    getNumberOfWheels() { throw new Error("Must implement"); }
    hasEngine() { throw new Error("Must implement"); } // Problem!
}

class MotorCycle extends Vehicle {
    getNumberOfWheels() { return 2; }
    hasEngine() { return true; }
}

class Car extends Vehicle {
    getNumberOfWheels() { return 4; }
    hasEngine() { return true; }
}

class Bicycle extends Vehicle {
    getNumberOfWheels() { return 2; }
    hasEngine() {
        // Violation! Bicycle doesn't have an engine
        return false; // Misleading!
    }
}

// THE SOLUTION:
class VehicleGood {
    getNumberOfWheels() { throw new Error("Must implement"); }
}

class EngineVehicle extends VehicleGood {
    hasEngine() { return true; }
}

class MotorCycleGood extends EngineVehicle {
    getNumberOfWheels() { return 2; }
}

class CarGood extends EngineVehicle {
    getNumberOfWheels() { return 4; }
}

class BicycleGood extends VehicleGood {
    getNumberOfWheels() { return 2; }
    // No hasEngine() method - doesn't apply!
}

// Usage
console.log("=== PROBLEM (LSP Violation) ===");
const bicycle = new Bicycle();
console.log(`Bicycle wheels: ${bicycle.getNumberOfWheels()}`);
console.log(`Bicycle has engine: ${bicycle.hasEngine()} (Misleading!)`);

console.log("\n=== SOLUTION (LSP Compliant) ===");
const bicycleGood = new BicycleGood();
console.log(`Bicycle wheels: ${bicycleGood.getNumberOfWheels()}`);
console.log("Bicycle doesn't need hasEngine() method!");

const car = new CarGood();
console.log(`Car wheels: ${car.getNumberOfWheels()}`);
console.log(`Car has engine: ${car.hasEngine()}`);
