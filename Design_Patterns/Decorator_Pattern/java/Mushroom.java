/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Decorator: Mushroom
 * 
 * Mushroom topping decorator.
 * Adds ₹15 to the wrapped pizza's cost.
 */

public class Mushroom extends ToppingDecorator {
    /**
     * Constructor: Initialize Mushroom topping.
     * 
     * @param basePizza The pizza to add mushrooms to
     */
    public Mushroom(BasePizza basePizza) {
        super(basePizza);
    }

    /**
     * Calculate total cost: base pizza cost + mushroom cost.
     * 
     * @return Total cost in rupees
     */
    @Override
    public int cost() {
        return this.basePizza.cost() + 15;
    }
}
