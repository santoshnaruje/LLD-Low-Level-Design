// TITLE: Interface Segregation Principle (ISP) - Waiter Example

// ========================================
// THE PROBLEM (VIOLATION):
// Fat interface forces unnecessary methods
// ========================================

interface RestaurantEmployeeBad {
    void washDishes();

    void serveCustomer();

    void cookFood();
}

class WaiterBad implements RestaurantEmployeeBad {
    public void washDishes() {
        // Not my job!
        System.out.println("Waiter: Not my job to wash dishes");
    }

    public void serveCustomer() {
        System.out.println("Serving customer");
    }

    public void cookFood() {
        // Not my job!
        System.out.println("Waiter: Not my job to cook");
    }
}

// ========================================
// THE SOLUTION:
// Segregate interfaces
// ========================================

interface WaiterInterface {
    void serveCustomer();

    void takeOrder();
}

interface ChefInterface {
    void cookFood();

    void decideMenu();
}

class Waiter implements WaiterInterface {
    public void serveCustomer() {
        System.out.println("Serving customer");
    }

    public void takeOrder() {
        System.out.println("Taking order");
    }
}

class Chef implements ChefInterface {
    public void cookFood() {
        System.out.println("Cooking food");
    }

    public void decideMenu() {
        System.out.println("Deciding menu");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== PROBLEM (ISP Violation) ===");
        WaiterBad waiterBad = new WaiterBad();
        waiterBad.serveCustomer();
        waiterBad.cookFood(); // Forced to implement!
        waiterBad.washDishes(); // Forced to implement!

        System.out.println("\n=== SOLUTION (ISP Compliant) ===");
        Waiter waiter = new Waiter();
        waiter.serveCustomer();
        waiter.takeOrder();

        Chef chef = new Chef();
        chef.cookFood();
        chef.decideMenu();
    }
}
