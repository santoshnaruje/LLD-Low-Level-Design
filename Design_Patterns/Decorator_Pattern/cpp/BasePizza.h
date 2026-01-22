/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Component: BasePizza
 * 
 * This header defines the abstract base class for all pizzas.
 * The Decorator pattern allows us to add toppings dynamically without creating
 * a separate class for every combination of pizza and toppings.
 */

#ifndef BASE_PIZZA_H
#define BASE_PIZZA_H

/**
 * Abstract base class for all pizzas.
 * This is the Component in the Decorator pattern.
 */
class BasePizza {
public:
    /**
     * Virtual destructor for proper cleanup of derived classes.
     */
    virtual ~BasePizza() {}
    
    /**
     * Calculate and return the cost of the pizza.
     * Pure virtual function - must be implemented by derived classes.
     * 
     * @return Cost of the pizza in rupees
     */
    virtual int cost() = 0;
};

#endif // BASE_PIZZA_H
