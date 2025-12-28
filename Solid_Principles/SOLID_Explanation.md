# SOLID Principles in Low-Level Design (LLD)

This guide explains the SOLID principles using examples from **Shrayansh Jain's "Concept && Coding"** YouTube channel.

## Summary
SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.

1.  **S** - Single Responsibility Principle (SRP)
2.  **O** - Open/Closed Principle (OCP)
3.  **L** - Liskov Substitution Principle (LSP)
4.  **I** - Interface Segregation Principle (ISP)
5.  **D** - Dependency Inversion Principle (DIP)

---

## 1. Single Responsibility Principle (SRP)
**"A class should have only one reason to change."**

**The Problem**: An `Invoice` class calculates the total price (from `Marker` items), prints the invoice, AND saves it to a database. If the printing format changes, we modify Invoice. If the database changes, we modify Invoice. Too many reasons to change!

**The Solution**: Split responsibilities:
- `Invoice`: Holds data and calculates total.
- `InvoicePrinter`: Handles printing.
- `InvoiceDao`: Handles database persistence.

---

## 2. Open/Closed Principle (OCP)
**"Software entities should be open for extension, but closed for modification."**

**The Problem**: `InvoiceDao` class has methods `saveToDB()` and `saveToFile()`. To add MongoDB support, we must modify the class by adding `saveToMongoDB()`.

**The Solution**: Create an `InvoiceDao` interface. Implement `DatabaseInvoiceDao` and `FileInvoiceDao`. To add MongoDB, create `MongoDBInvoiceDao` without touching existing code.

---

## 3. Liskov Substitution Principle (LSP)
**"Subtypes must be substitutable for their base types."**

**The Problem**: We have a `Vehicle` base class with methods `getNumberOfWheels()` and `hasEngine()`. `MotorCycle` and `Car` implement both methods fine. However, `Bicycle` also inherits from `Vehicle` but doesn't have an engine. When forced to implement `hasEngine()`, it returns `false`, which is misleading and violates the expected behavior of the base class.

**The Solution**: Refactor the hierarchy. Create `Vehicle` (general) with only `getNumberOfWheels()`. Create `EngineVehicle` extending `Vehicle` with `hasEngine()`. `MotorCycle` and `Car` extend `EngineVehicle`. `Bicycle` extends only `Vehicle`.

**Source**: This example is from Shrayansh Jain's specific LSP video (ID: 129QkkXUHeQ).



---

## 4. Interface Segregation Principle (ISP)
**"Clients should not be forced to depend upon interfaces that they do not use."**

**The Problem**: A `RestaurantEmployee` interface has `washDishes()`, `serveCustomer()`, and `cookFood()`. A `Waiter` class must implement all three, but waiters don't cook food. They're forced to provide dummy implementations.

**The Solution**: Split into smaller interfaces: `WaiterInterface` (serveCustomer), `ChefInterface` (cookFood), `CleanerInterface` (washDishes). Each employee type implements only relevant interfaces.

---

## 5. Dependency Inversion Principle (DIP)
**"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

**The Problem**: `MacBook` class constructor creates `new WiredKeyboard()` directly. We can't easily swap to `BluetoothKeyboard` without modifying `MacBook`.

**The Solution**: `MacBook` depends on a `Keyboard` interface. Inject the specific keyboard type (`WiredKeyboard` or `BluetoothKeyboard`) through the constructor. Now `MacBook` is decoupled from concrete keyboard implementations.
