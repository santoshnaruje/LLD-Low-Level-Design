// TITLE: Liskov Substitution Principle (LSP) - Vehicle Example

// THE PROBLEM (VIOLATION):
abstract class Vehicle {
    abstract int getNumberOfWheels();

    abstract boolean hasEngine(); // Problem: Not all vehicles have engines!
}

class MotorCycle extends Vehicle {
    int getNumberOfWheels() {
        return 2;
    }

    boolean hasEngine() {
        return true;
    }
}

class Car extends Vehicle {
    int getNumberOfWheels() {
        return 4;
    }

    boolean hasEngine() {
        return true;
    }
}

class Bicycle extends Vehicle {
    int getNumberOfWheels() {
        return 2;
    }

    boolean hasEngine() {
        // Violation! Bicycle doesn't have an engine
        return false; // Misleading!
    }
}

// THE SOLUTION:
abstract class VehicleGood {
    abstract int getNumberOfWheels();
}

abstract class EngineVehicle extends VehicleGood {
    boolean hasEngine() {
        return true;
    }
}

class MotorCycleGood extends EngineVehicle {
    int getNumberOfWheels() {
        return 2;
    }
}

class CarGood extends EngineVehicle {
    int getNumberOfWheels() {
        return 4;
    }
}

class BicycleGood extends VehicleGood {
    int getNumberOfWheels() {
        return 2;
    }
    // No hasEngine() method - doesn't apply!
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== PROBLEM (LSP Violation) ===");
        Bicycle bicycle = new Bicycle();
        System.out.println("Bicycle wheels: " + bicycle.getNumberOfWheels());
        System.out.println("Bicycle has engine: " + bicycle.hasEngine() + " (Misleading!)");

        System.out.println("\n=== SOLUTION (LSP Compliant) ===");
        BicycleGood bicycleGood = new BicycleGood();
        System.out.println("Bicycle wheels: " + bicycleGood.getNumberOfWheels());
        System.out.println("Bicycle doesn't need hasEngine() method!");

        CarGood car = new CarGood();
        System.out.println("Car wheels: " + car.getNumberOfWheels());
        System.out.println("Car has engine: " + car.hasEngine());
    }
}
