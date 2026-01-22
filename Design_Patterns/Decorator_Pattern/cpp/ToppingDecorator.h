/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Decorator: ToppingDecorator
 * 
 * This header defines the abstract decorator class.
 * Key concept: The decorator both "is-a" BasePizza (inheritance) 
 * and "has-a" BasePizza (composition).
 */

#ifndef TOPPING_DECORATOR_H
#define TOPPING_DECORATOR_H

#include "BasePizza.h"

/**
 * Abstract decorator class for pizza toppings.
 * 
 * This class demonstrates the core of the Decorator pattern:
 * - IS-A relationship: Inherits from BasePizza
 * - HAS-A relationship: Contains a BasePizza pointer
 * 
 * This allows decorators to wrap other pizzas (or decorated pizzas)
 * and add their own cost on top.
 */
class ToppingDecorator : public BasePizza {
protected:
    BasePizza* basePizza;  // The wrapped pizza object
    
public:
    /**
     * Constructor: Initialize the decorator with a pizza to wrap.
     * 
     * @param pizza Pointer to the pizza (or decorated pizza) to wrap
     */
    ToppingDecorator(BasePizza* pizza) : basePizza(pizza) {}
    
    /**
     * Destructor: Clean up the wrapped pizza.
     */
    virtual ~ToppingDecorator() {
        delete basePizza;
    }
};

#endif // TOPPING_DECORATOR_H
