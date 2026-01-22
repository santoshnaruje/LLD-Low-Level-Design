/**
 * Decorator Design Pattern - Pizza Billing System
 * Concrete Component: Margherita
 * 
 * Margherita Pizza - A classic pizza with tomato and cheese.
 * Base cost: ₹100
 */

public class Margherita extends BasePizza {
    /**
     * Return the cost of Margherita pizza.
     * 
     * @return Cost in rupees
     */
    @Override
    public int cost() {
        return 100;
    }
}
