// TITLE: Dependency Inversion Principle (DIP) - MacBook Example

// ========================================
// THE PROBLEM (VIOLATION):
// MacBook depends on concrete WiredKeyboard
// ========================================

class WiredKeyboardBad {
    type() {
        console.log("Typing on wired keyboard");
    }
}

class MacBookBad {
    constructor() {
        // Hard dependency!
        this.keyboard = new WiredKeyboardBad();
    }

    useKeyboard() {
        this.keyboard.type();
    }
}

// ========================================
// THE SOLUTION:
// Depend on abstraction (via dependency injection)
// ========================================

class WiredKeyboard {
    type() {
        console.log("Typing on wired keyboard");
    }
}

class BluetoothKeyboard {
    type() {
        console.log("Typing on Bluetooth keyboard");
    }
}

class MacBook {
    constructor(keyboard) { // Dependency injection!
        this.keyboard = keyboard;
    }

    useKeyboard() {
        this.keyboard.type();
    }
}

// Usage
console.log("=== PROBLEM (DIP Violation) ===");
const macbookBad = new MacBookBad();
macbookBad.useKeyboard(); // Stuck with wired keyboard!

console.log("\n=== SOLUTION (DIP Compliant) ===");
const wired = new WiredKeyboard();
const macbook1 = new MacBook(wired);
macbook1.useKeyboard();

const bluetooth = new BluetoothKeyboard();
const macbook2 = new MacBook(bluetooth);
macbook2.useKeyboard();
