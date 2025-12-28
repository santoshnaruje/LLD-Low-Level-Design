#include <iostream>

// TITLE: Interface Segregation Principle (ISP) - Waiter Example

// ========================================
// THE PROBLEM (VIOLATION):
// Fat interface forces unnecessary methods
// ========================================

class RestaurantEmployeeBad {
public:
    virtual void washDishes() = 0;
    virtual void serveCustomer() = 0;
    virtual void cookFood() = 0;
};

class WaiterBad : public RestaurantEmployeeBad {
public:
    void washDishes() override {
        // Not my job!
        std::cout << "Waiter: Not my job to wash dishes" << std::endl;
    }
    void serveCustomer() override {
        std::cout << "Serving customer" << std::endl;
    }
    void cookFood() override {
        // Not my job!
        std::cout << "Waiter: Not my job to cook" << std::endl;
    }
};

// ========================================
// THE SOLUTION:
// Segregate interfaces
// ========================================

class WaiterInterface {
public:
    virtual void serveCustomer() = 0;
    virtual void takeOrder() = 0;
};

class ChefInterface {
public:
    virtual void cookFood() = 0;
    virtual void decideMenu() = 0;
};

class Waiter : public WaiterInterface {
public:
    void serveCustomer() override {
        std::cout << "Serving customer" << std::endl;
    }
    void takeOrder() override {
        std::cout << "Taking order" << std::endl;
    }
};

class Chef : public ChefInterface {
public:
    void cookFood() override {
        std::cout << "Cooking food" << std::endl;
    }
    void decideMenu() override {
        std::cout << "Deciding menu" << std::endl;
    }
};

int main() {
    std::cout << "=== PROBLEM (ISP Violation) ===" << std::endl;
    WaiterBad waiterBad;
    waiterBad.serveCustomer();
    waiterBad.cookFood(); // Forced to implement!
    waiterBad.washDishes(); // Forced to implement!
    
    std::cout << "\n=== SOLUTION (ISP Compliant) ===" << std::endl;
    Waiter waiter;
    waiter.serveCustomer();
    waiter.takeOrder();
    
    Chef chef;
    chef.cookFood();
    chef.decideMenu();
    
    return 0;
}
