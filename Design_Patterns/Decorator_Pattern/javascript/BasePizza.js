/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Component: BasePizza
 * 
 * This module defines the base class for all pizzas.
 * The Decorator pattern allows us to add toppings dynamically without creating
 * a separate class for every combination of pizza and toppings.
 */

class BasePizza {
    /**
     * Calculate and return the cost of the pizza.
     * This method should be overridden by subclasses.
     * 
     * @returns {number} Cost of the pizza in rupees
     * @throws {Error} If not implemented by subclass
     */
    cost() {
        throw new Error("cost() method must be implemented by subclass");
    }
}

module.exports = BasePizza;
