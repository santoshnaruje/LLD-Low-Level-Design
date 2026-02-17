/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Decorator: ExtraCheese
 * 
 * Extra Cheese topping decorator.
 * Adds ₹10 to the wrapped pizza's cost.
 */

public class ExtraCheese extends ToppingDecorator {
    /**
     * Constructor: Initialize Extra Cheese topping.
     * 
     * @param basePizza The pizza to add extra cheese to
     */
    public ExtraCheese(BasePizza basePizza) {
        super(basePizza);
    }

    /**
     * Calculate total cost: base pizza cost + extra cheese cost.
     * 
     * @return Total cost in rupees
     */
    @Override
    public int cost() {
        return this.basePizza.cost() + 10;
    }
}
