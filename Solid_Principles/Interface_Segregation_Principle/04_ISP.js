// TITLE: Interface Segregation Principle (ISP) - Waiter Example

// ========================================
// THE PROBLEM (VIOLATION):
// Fat interface forces unnecessary methods
// ========================================

class WaiterBad {
    washDishes() {
        // Not my job!
        console.log("Waiter: Not my job to wash dishes");
    }
    serveCustomer() {
        console.log("Serving customer");
    }
    cookFood() {
        // Not my job!
        console.log("Waiter: Not my job to cook");
    }
}

// ========================================
// THE SOLUTION:
// Segregate interfaces (via separate classes in JS)
// ========================================

class Waiter {
    serveCustomer() {
        console.log("Serving customer");
    }
    takeOrder() {
        console.log("Taking order");
    }
}

class Chef {
    cookFood() {
        console.log("Cooking food");
    }
    decideMenu() {
        console.log("Deciding menu");
    }
}

// Usage
console.log("=== PROBLEM (ISP Violation) ===");
const waiterBad = new WaiterBad();
waiterBad.serveCustomer();
waiterBad.cookFood(); // Forced to implement!
waiterBad.washDishes(); // Forced to implement!

console.log("\n=== SOLUTION (ISP Compliant) ===");
const waiter = new Waiter();
waiter.serveCustomer();
waiter.takeOrder();

const chef = new Chef();
chef.cookFood();
chef.decideMenu();
