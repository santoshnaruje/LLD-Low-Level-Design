/**
 * Decorator Design Pattern - Pizza Billing System
 * Main Demo File
 * 
 * This demonstrates the Decorator pattern in action.
 * Shows how toppings can be added dynamically to pizzas without
 * creating separate classes for every combination.
 */

const { Margherita, VegDelight, FarmHouse } = require('./ConcretePizzas');
const { ExtraCheese, Mushroom } = require('./ConcreteDecorators');

/**
 * Helper function to print pizza order and cost.
 * @param {string} description - Description of the pizza order
 * @param {BasePizza} pizza - The pizza object
 */
function printOrder(description, pizza) {
    console.log(`${description}: ₹${pizza.cost()}`);
}

function main() {
    console.log("=".repeat(50));
    console.log("DECORATOR PATTERN - PIZZA BILLING SYSTEM");
    console.log("=".repeat(50));
    console.log();

    // Example 1: Base pizzas without any toppings
    console.log("1. BASE PIZZAS (No Toppings)");
    console.log("-".repeat(50));
    const margherita = new Margherita();
    printOrder("Margherita Pizza", margherita);

    const vegDelight = new VegDelight();
    printOrder("Veg Delight Pizza", vegDelight);

    const farmHouse = new FarmHouse();
    printOrder("Farm House Pizza", farmHouse);
    console.log();

    // Example 2: Pizzas with single topping
    console.log("2. PIZZAS WITH SINGLE TOPPING");
    console.log("-".repeat(50));
    const margheritaWithCheese = new ExtraCheese(new Margherita());
    printOrder("Margherita + Extra Cheese", margheritaWithCheese);

    const vegDelightWithMushroom = new Mushroom(new VegDelight());
    printOrder("Veg Delight + Mushroom", vegDelightWithMushroom);
    console.log();

    // Example 3: Pizzas with multiple toppings (nested decorators)
    console.log("3. PIZZAS WITH MULTIPLE TOPPINGS");
    console.log("-".repeat(50));
    const margheritaDeluxe = new Mushroom(new ExtraCheese(new Margherita()));
    printOrder("Margherita + Extra Cheese + Mushroom", margheritaDeluxe);

    const vegDelightDeluxe = new ExtraCheese(new Mushroom(new VegDelight()));
    printOrder("Veg Delight + Mushroom + Extra Cheese", vegDelightDeluxe);

    const farmHouseDeluxe = new Mushroom(new ExtraCheese(new FarmHouse()));
    printOrder("Farm House + Extra Cheese + Mushroom", farmHouseDeluxe);
    console.log();

    // Example 4: Double toppings
    console.log("4. PIZZAS WITH DOUBLE TOPPINGS");
    console.log("-".repeat(50));
    const extraCheesy = new ExtraCheese(new ExtraCheese(new Margherita()));
    printOrder("Margherita + Double Extra Cheese", extraCheesy);

    const mushroomLover = new Mushroom(new Mushroom(new VegDelight()));
    printOrder("Veg Delight + Double Mushroom", mushroomLover);
    console.log();

    console.log("=".repeat(50));
    console.log("Pattern Benefits:");
    console.log("- No class explosion (no need for MargheritaWithCheese class)");
    console.log("- Flexible: Add toppings dynamically at runtime");
    console.log("- Open/Closed Principle: Open for extension, closed for modification");
    console.log("=".repeat(50));
}

// Run the demo
main();
