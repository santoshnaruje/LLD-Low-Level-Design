/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Decorators: ExtraCheese, Mushroom
 * 
 * This module defines concrete topping decorators.
 * Each decorator wraps a pizza and adds its own cost.
 */

const ToppingDecorator = require('./ToppingDecorator');

/**
 * Extra Cheese topping decorator.
 * Adds ₹10 to the wrapped pizza's cost.
 */
class ExtraCheese extends ToppingDecorator {
    /**
     * Initialize Extra Cheese topping.
     * 
     * @param {BasePizza} basePizza - The pizza to add extra cheese to
     */
    constructor(basePizza) {
        super(basePizza);
    }

    /**
     * Calculate total cost: base pizza cost + extra cheese cost.
     * 
     * @returns {number} Total cost in rupees
     */
    cost() {
        return this.basePizza.cost() + 10;
    }
}

/**
 * Mushroom topping decorator.
 * Adds ₹15 to the wrapped pizza's cost.
 */
class Mushroom extends ToppingDecorator {
    /**
     * Initialize Mushroom topping.
     * 
     * @param {BasePizza} basePizza - The pizza to add mushrooms to
     */
    constructor(basePizza) {
        super(basePizza);
    }

    /**
     * Calculate total cost: base pizza cost + mushroom cost.
     * 
     * @returns {number} Total cost in rupees
     */
    cost() {
        return this.basePizza.cost() + 15;
    }
}

module.exports = { ExtraCheese, Mushroom };
