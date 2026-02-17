/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Decorators: ExtraCheese, Mushroom
 * 
 * This header defines concrete topping decorators.
 * Each decorator wraps a pizza and adds its own cost.
 */

#ifndef CONCRETE_DECORATORS_H
#define CONCRETE_DECORATORS_H

#include "ToppingDecorator.h"

/**
 * Extra Cheese topping decorator.
 * Adds ₹10 to the wrapped pizza's cost.
 */
class ExtraCheese : public ToppingDecorator {
public:
    /**
     * Constructor: Initialize Extra Cheese topping.
     * 
     * @param pizza Pointer to the pizza to add extra cheese to
     */
    ExtraCheese(BasePizza* pizza) : ToppingDecorator(pizza) {}
    
    /**
     * Calculate total cost: base pizza cost + extra cheese cost.
     * 
     * @return Total cost in rupees
     */
    int cost() override;
};

/**
 * Mushroom topping decorator.
 * Adds ₹15 to the wrapped pizza's cost.
 */
class Mushroom : public ToppingDecorator {
public:
    /**
     * Constructor: Initialize Mushroom topping.
     * 
     * @param pizza Pointer to the pizza to add mushrooms to
     */
    Mushroom(BasePizza* pizza) : ToppingDecorator(pizza) {}
    
    /**
     * Calculate total cost: base pizza cost + mushroom cost.
     * 
     * @return Total cost in rupees
     */
    int cost() override;
};

#endif // CONCRETE_DECORATORS_H
