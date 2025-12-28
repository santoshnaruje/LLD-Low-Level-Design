// TITLE: Dependency Inversion Principle (DIP) - MacBook Example

// ========================================
// THE PROBLEM (VIOLATION):
// MacBook depends on concrete WiredKeyboard
// ========================================

class WiredKeyboardBad {
    public void type() {
        System.out.println("Typing on wired keyboard");
    }
}

class MacBookBad {
    private WiredKeyboardBad keyboard; // Hard dependency!

    MacBookBad() {
        // Forced to use WiredKeyboard - can't swap!
        this.keyboard = new WiredKeyboardBad();
    }

    public void useKeyboard() {
        keyboard.type();
    }
}

// ========================================
// THE SOLUTION:
// Depend on abstraction
// ========================================

interface Keyboard {
    void type();
}

class WiredKeyboard implements Keyboard {
    public void type() {
        System.out.println("Typing on wired keyboard");
    }
}

class BluetoothKeyboard implements Keyboard {
    public void type() {
        System.out.println("Typing on Bluetooth keyboard");
    }
}

class MacBook {
    private Keyboard keyboard;

    MacBook(Keyboard keyboard) { // Dependency injection!
        this.keyboard = keyboard;
    }

    public void useKeyboard() {
        keyboard.type();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== PROBLEM (DIP Violation) ===");
        MacBookBad macbookBad = new MacBookBad();
        macbookBad.useKeyboard(); // Stuck with wired keyboard!

        System.out.println("\n=== SOLUTION (DIP Compliant) ===");
        Keyboard wired = new WiredKeyboard();
        MacBook macbook1 = new MacBook(wired);
        macbook1.useKeyboard();

        Keyboard bluetooth = new BluetoothKeyboard();
        MacBook macbook2 = new MacBook(bluetooth);
        macbook2.useKeyboard();
    }
}
