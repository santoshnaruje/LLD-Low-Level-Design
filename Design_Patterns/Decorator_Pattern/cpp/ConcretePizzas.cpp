/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Components Implementation
 * 
 * This file implements the concrete pizza classes.
 */

#include "ConcretePizzas.h"

// Margherita Pizza Implementation
int Margherita::cost() {
    return 100;
}

// Veg Delight Pizza Implementation
int VegDelight::cost() {
    return 120;
}

// Farm House Pizza Implementation
int FarmHouse::cost() {
    return 200;
}
