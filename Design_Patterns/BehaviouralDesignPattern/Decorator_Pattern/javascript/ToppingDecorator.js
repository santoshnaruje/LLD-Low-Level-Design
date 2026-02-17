/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Decorator: ToppingDecorator
 * 
 * This module defines the abstract decorator class.
 * Key concept: The decorator both "is-a" BasePizza (inheritance) 
 * and "has-a" BasePizza (composition).
 */

const BasePizza = require('./BasePizza');

/**
 * Abstract decorator class for pizza toppings.
 * 
 * This class demonstrates the core of the Decorator pattern:
 * - IS-A relationship: Extends BasePizza
 * - HAS-A relationship: Contains a BasePizza reference
 * 
 * This allows decorators to wrap other pizzas (or decorated pizzas)
 * and add their own cost on top.
 */
class ToppingDecorator extends BasePizza {
    /**
     * Initialize the decorator with a pizza to wrap.
     * 
     * @param {BasePizza} basePizza - The pizza (or decorated pizza) to wrap
     */
    constructor(basePizza) {
        super();
        this.basePizza = basePizza;
    }
}

module.exports = ToppingDecorator;
