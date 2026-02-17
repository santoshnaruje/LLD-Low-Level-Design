/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Component: VegDelight
 * 
 * Veg Delight Pizza - A vegetarian pizza with assorted vegetables.
 * Base cost: ₹120
 */

public class VegDelight extends BasePizza {
    /**
     * Return the cost of Veg Delight pizza.
     * 
     * @return Cost in rupees
     */
    @Override
    public int cost() {
        return 120;
    }
}
