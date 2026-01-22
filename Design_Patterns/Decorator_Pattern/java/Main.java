/**
 * Decorator Design Pattern - Pizza Billing System
 * Main Demo Class
 * 
 * This demonstrates the Decorator pattern in action.
 * Shows how toppings can be added dynamically to pizzas without
 * creating separate classes for every combination.
 */

public class Main {
    /**
     * Helper method to print pizza order and cost.
     * 
     * @param description Description of the pizza order
     * @param pizza       The pizza object
     */
    private static void printOrder(String description, BasePizza pizza) {
        System.out.println(description + ": ₹" + pizza.cost());
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(50));
        System.out.println("DECORATOR PATTERN - PIZZA BILLING SYSTEM");
        System.out.println("=".repeat(50));
        System.out.println();

        // Example 1: Base pizzas without any toppings
        System.out.println("1. BASE PIZZAS (No Toppings)");
        System.out.println("-".repeat(50));
        BasePizza margherita = new Margherita();
        printOrder("Margherita Pizza", margherita);

        BasePizza vegDelight = new VegDelight();
        printOrder("Veg Delight Pizza", vegDelight);

        BasePizza farmHouse = new FarmHouse();
        printOrder("Farm House Pizza", farmHouse);
        System.out.println();

        // Example 2: Pizzas with single topping
        System.out.println("2. PIZZAS WITH SINGLE TOPPING");
        System.out.println("-".repeat(50));
        BasePizza margheritaWithCheese = new ExtraCheese(new Margherita());
        printOrder("Margherita + Extra Cheese", margheritaWithCheese);

        BasePizza vegDelightWithMushroom = new Mushroom(new VegDelight());
        printOrder("Veg Delight + Mushroom", vegDelightWithMushroom);
        System.out.println();

        // Example 3: Pizzas with multiple toppings (nested decorators)
        System.out.println("3. PIZZAS WITH MULTIPLE TOPPINGS");
        System.out.println("-".repeat(50));
        BasePizza margheritaDeluxe = new Mushroom(new ExtraCheese(new Margherita()));
        printOrder("Margherita + Extra Cheese + Mushroom", margheritaDeluxe);

        BasePizza vegDelightDeluxe = new ExtraCheese(new Mushroom(new VegDelight()));
        printOrder("Veg Delight + Mushroom + Extra Cheese", vegDelightDeluxe);

        BasePizza farmHouseDeluxe = new Mushroom(new ExtraCheese(new FarmHouse()));
        printOrder("Farm House + Extra Cheese + Mushroom", farmHouseDeluxe);
        System.out.println();

        // Example 4: Double toppings
        System.out.println("4. PIZZAS WITH DOUBLE TOPPINGS");
        System.out.println("-".repeat(50));
        BasePizza extraCheesy = new ExtraCheese(new ExtraCheese(new Margherita()));
        printOrder("Margherita + Double Extra Cheese", extraCheesy);

        BasePizza mushroomLover = new Mushroom(new Mushroom(new VegDelight()));
        printOrder("Veg Delight + Double Mushroom", mushroomLover);
        System.out.println();

        System.out.println("=".repeat(50));
        System.out.println("Pattern Benefits:");
        System.out.println("- No class explosion (no need for MargheritaWithCheese class)");
        System.out.println("- Flexible: Add toppings dynamically at runtime");
        System.out.println("- Open/Closed Principle: Open for extension, closed for modification");
        System.out.println("=".repeat(50));
    }
}
