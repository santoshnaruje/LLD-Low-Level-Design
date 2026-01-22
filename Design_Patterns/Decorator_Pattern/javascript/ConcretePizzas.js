/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Components: Margherita, VegDelight, FarmHouse
 * 
 * This module defines concrete pizza classes that extend BasePizza.
 * Each pizza has a fixed base cost.
 */

const BasePizza = require('./BasePizza');

/**
 * Margherita Pizza - A classic pizza with tomato and cheese.
 * Base cost: ₹100
 */
class Margherita extends BasePizza {
    /**
     * Return the cost of Margherita pizza.
     * @returns {number} Cost in rupees
     */
    cost() {
        return 100;
    }
}

/**
 * Veg Delight Pizza - A vegetarian pizza with assorted vegetables.
 * Base cost: ₹120
 */
class VegDelight extends BasePizza {
    /**
     * Return the cost of Veg Delight pizza.
     * @returns {number} Cost in rupees
     */
    cost() {
        return 120;
    }
}

/**
 * Farm House Pizza - A premium pizza with farm-fresh ingredients.
 * Base cost: ₹200
 */
class FarmHouse extends BasePizza {
    /**
     * Return the cost of Farm House pizza.
     * @returns {number} Cost in rupees
     */
    cost() {
        return 200;
    }
}

module.exports = { Margherita, VegDelight, FarmHouse };
