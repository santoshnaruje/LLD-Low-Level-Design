/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Component: FarmHouse
 * 
 * Farm House Pizza - A premium pizza with farm-fresh ingredients.
 * Base cost: ₹200
 */

public class FarmHouse extends BasePizza {
    /**
     * Return the cost of Farm House pizza.
     * 
     * @return Cost in rupees
     */
    @Override
    public int cost() {
        return 200;
    }
}
