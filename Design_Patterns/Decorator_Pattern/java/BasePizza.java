/**
 * Decorator Design Pattern - Pizza Billing System
 * Base Component: BasePizza
 * 
 * This class defines the abstract base class for all pizzas.
 * The Decorator pattern allows us to add toppings dynamically without creating
 * a separate class for every combination of pizza and toppings.
 */

public abstract class BasePizza {
    /**
     * Calculate and return the cost of the pizza.
     * This method must be implemented by all concrete pizza classes.
     * 
     * @return Cost of the pizza in rupees
     */
    public abstract int cost();
}
