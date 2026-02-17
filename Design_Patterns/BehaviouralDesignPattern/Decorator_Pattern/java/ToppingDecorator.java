/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Decorator: ToppingDecorator
 * 
 * This class defines the abstract decorator class.
 * Key concept: The decorator both "is-a" BasePizza (inheritance)
 * and "has-a" BasePizza (composition).
 */

public abstract class ToppingDecorator extends BasePizza {
    /**
     * The wrapped pizza object.
     * This demonstrates the "has-a" relationship.
     */
    protected BasePizza basePizza;

    /**
     * Constructor: Initialize the decorator with a pizza to wrap.
     * 
     * @param basePizza The pizza (or decorated pizza) to wrap
     */
    public ToppingDecorator(BasePizza basePizza) {
        this.basePizza = basePizza;
    }
}
