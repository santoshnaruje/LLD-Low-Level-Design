/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Decorators Implementation
 * 
 * This file implements the concrete topping decorators.
 */

#include "ConcreteDecorators.h"

// Extra Cheese Implementation
int ExtraCheese::cost() {
    return basePizza->cost() + 10;
}

// Mushroom Implementation
int Mushroom::cost() {
    return basePizza->cost() + 15;
}
