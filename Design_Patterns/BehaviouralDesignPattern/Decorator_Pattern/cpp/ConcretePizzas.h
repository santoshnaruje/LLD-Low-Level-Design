/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Components: Margherita, VegDelight, FarmHouse
 * 
 * This header defines concrete pizza classes that extend BasePizza.
 * Each pizza has a fixed base cost.
 */

#ifndef CONCRETE_PIZZAS_H
#define CONCRETE_PIZZAS_H

#include "BasePizza.h"

/**
 * Margherita Pizza - A classic pizza with tomato and cheese.
 * Base cost: ₹100
 */
class Margherita : public BasePizza {
public:
    /**
     * Return the cost of Margherita pizza.
     * @return Cost in rupees
     */
    int cost() override;
};

/**
 * Veg Delight Pizza - A vegetarian pizza with assorted vegetables.
 * Base cost: ₹120
 */
class VegDelight : public BasePizza {
public:
    /**
     * Return the cost of Veg Delight pizza.
     * @return Cost in rupees
     */
    int cost() override;
};

/**
 * Farm House Pizza - A premium pizza with farm-fresh ingredients.
 * Base cost: ₹200
 */
class FarmHouse : public BasePizza {
public:
    /**
     * Return the cost of Farm House pizza.
     * @return Cost in rupees
     */
    int cost() override;
};

#endif // CONCRETE_PIZZAS_H
