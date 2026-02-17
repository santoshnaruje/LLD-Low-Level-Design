/**
 * Decorator Design Pattern - Pizza Billing System
 * Main Demo File
 * 
 * This demonstrates the Decorator pattern in action.
 * Shows how toppings can be added dynamically to pizzas without
 * creating separate classes for every combination.
 */

#include <iostream>
#include <string>
#include "ConcretePizzas.h"
#include "ConcreteDecorators.h"

using namespace std;

/**
 * Helper function to print pizza order and cost.
 * @param description Description of the pizza order
 * @param pizza Pointer to the pizza object
 */
void printOrder(const string& description, BasePizza* pizza) {
    cout << description << ": ₹" << pizza->cost() << endl;
}

int main() {
    cout << string(50, '=') << endl;
    cout << "DECORATOR PATTERN - PIZZA BILLING SYSTEM" << endl;
    cout << string(50, '=') << endl;
    cout << endl;
    
    // Example 1: Base pizzas without any toppings
    cout << "1. BASE PIZZAS (No Toppings)" << endl;
    cout << string(50, '-') << endl;
    BasePizza* margherita = new Margherita();
    printOrder("Margherita Pizza", margherita);
    
    BasePizza* vegDelight = new VegDelight();
    printOrder("Veg Delight Pizza", vegDelight);
    
    BasePizza* farmHouse = new FarmHouse();
    printOrder("Farm House Pizza", farmHouse);
    cout << endl;
    
    // Clean up base pizzas
    delete margherita;
    delete vegDelight;
    delete farmHouse;
    
    // Example 2: Pizzas with single topping
    cout << "2. PIZZAS WITH SINGLE TOPPING" << endl;
    cout << string(50, '-') << endl;
    BasePizza* margheritaWithCheese = new ExtraCheese(new Margherita());
    printOrder("Margherita + Extra Cheese", margheritaWithCheese);
    
    BasePizza* vegDelightWithMushroom = new Mushroom(new VegDelight());
    printOrder("Veg Delight + Mushroom", vegDelightWithMushroom);
    cout << endl;
    
    // Clean up
    delete margheritaWithCheese;
    delete vegDelightWithMushroom;
    
    // Example 3: Pizzas with multiple toppings (nested decorators)
    cout << "3. PIZZAS WITH MULTIPLE TOPPINGS" << endl;
    cout << string(50, '-') << endl;
    BasePizza* margheritaDeluxe = new Mushroom(new ExtraCheese(new Margherita()));
    printOrder("Margherita + Extra Cheese + Mushroom", margheritaDeluxe);
    
    BasePizza* vegDelightDeluxe = new ExtraCheese(new Mushroom(new VegDelight()));
    printOrder("Veg Delight + Mushroom + Extra Cheese", vegDelightDeluxe);
    
    BasePizza* farmHouseDeluxe = new Mushroom(new ExtraCheese(new FarmHouse()));
    printOrder("Farm House + Extra Cheese + Mushroom", farmHouseDeluxe);
    cout << endl;
    
    // Clean up
    delete margheritaDeluxe;
    delete vegDelightDeluxe;
    delete farmHouseDeluxe;
    
    // Example 4: Double toppings
    cout << "4. PIZZAS WITH DOUBLE TOPPINGS" << endl;
    cout << string(50, '-') << endl;
    BasePizza* extraCheesy = new ExtraCheese(new ExtraCheese(new Margherita()));
    printOrder("Margherita + Double Extra Cheese", extraCheesy);
    
    BasePizza* mushroomLover = new Mushroom(new Mushroom(new VegDelight()));
    printOrder("Veg Delight + Double Mushroom", mushroomLover);
    cout << endl;
    
    // Clean up
    delete extraCheesy;
    delete mushroomLover;
    
    cout << string(50, '=') << endl;
    cout << "Pattern Benefits:" << endl;
    cout << "- No class explosion (no need for MargheritaWithCheese class)" << endl;
    cout << "- Flexible: Add toppings dynamically at runtime" << endl;
    cout << "- Open/Closed Principle: Open for extension, closed for modification" << endl;
    cout << string(50, '=') << endl;
    
    return 0;
}
