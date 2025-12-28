# Low-Level Design (LLD) - SOLID Principles & Design Patterns

A comprehensive repository demonstrating **SOLID Principles** and **Design Patterns** with implementations in **C++, Python, Java, and JavaScript**.


## 📚 Repository Structure

```
LLD/
├── Solid_Principles/          # SOLID Principles implementations
│   ├── Single_Responsibility_Principle/
│   ├── Open_Closed_Principle/
│   ├── Liskov_Substitution_Principle/
│   ├── Interface_Segregation_Principle/
│   └── Dependency_Inversion_Principle/
│
└── Design_Patterns/           # Design Pattern implementations
    ├── Stratergy_Design_Pattern/
    └── Observer_Design_pattern/
```

## 🎯 SOLID Principles

All SOLID principles are implemented with **clear problem/solution examples** to demonstrate violations and correct implementations.


### 1. Single Responsibility Principle (SRP)
**"A class should have only one reason to change."**

- **Example**: Invoice/Marker
- **Problem**: `Invoice` class handles calculation, printing, AND database saving
- **Solution**: Separated into `Invoice`, `InvoicePrinter`, and `InvoiceDao`

### 2. Open/Closed Principle (OCP)
**"Software entities should be open for extension, but closed for modification."**

- **Example**: InvoiceDao
- **Problem**: Adding MongoDB requires modifying the `InvoiceDao` class
- **Solution**: `InvoiceDao` interface with `DatabaseInvoiceDao`, `FileInvoiceDao`, `MongoDBInvoiceDao`

### 3. Liskov Substitution Principle (LSP)
**"Subtypes must be substitutable for their base types."**

- **Example**: Vehicle/Motorcycle/Bicycle
- **Problem**: `Bicycle` inherits from `Vehicle` but doesn't have an engine (`hasEngine()` returns false - misleading!)
- **Solution**: Separate `Vehicle` (general) from `EngineVehicle` (has engine)

### 4. Interface Segregation Principle (ISP)
**"Clients should not be forced to depend upon interfaces that they do not use."**

- **Example**: Restaurant Employee
- **Problem**: `RestaurantEmployee` interface forces `Waiter` to implement `cookFood()` and `washDishes()`
- **Solution**: Segregated into `WaiterInterface` and `ChefInterface`

### 5. Dependency Inversion Principle (DIP)
**"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

- **Example**: MacBook/Keyboard
- **Problem**: `MacBook` creates `new WiredKeyboard()` directly (tight coupling)
- **Solution**: `MacBook` depends on `Keyboard` interface with dependency injection

## 🎨 Design Patterns

### Strategy Design Pattern
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.

**Implementations**: C++, Python, Java, JavaScript

### Observer Design Pattern
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

**Implementations**: C++, Python, Java, JavaScript

## 🚀 How to Run

### C++ Examples
```bash
cd Solid_Principles/Single_Responsibility_Principle
g++ 01_SRP.cpp -o srp
./srp
```

### Python Examples
```bash
cd Solid_Principles/Single_Responsibility_Principle
python3 01_SRP.py
```

### Java Examples
```bash
cd Solid_Principles/Single_Responsibility_Principle
javac Main.java
java Main
```

### JavaScript Examples
```bash
cd Solid_Principles/Single_Responsibility_Principle
node 01_SRP.js
```

## 📖 About

This repository contains educational implementations of SOLID principles and design patterns for learning purposes.

## 🤝 Contributing


Feel free to contribute by:
- Adding more design patterns
- Improving existing examples
- Adding examples in other programming languages

## 📝 License

This project is for educational purposes.

---

**Happy Learning! 🎓**
