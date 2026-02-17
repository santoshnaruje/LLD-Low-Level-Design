#include <iostream>

// TITLE: Dependency Inversion Principle (DIP) - MacBook Example

// ========================================
// THE PROBLEM (VIOLATION):
// MacBook depends on concrete WiredKeyboard
// ========================================

class WiredKeyboard {
public:
    void type() { std::cout << "Typing on wired keyboard" << std::endl; }
};

class MacBookBad {
    WiredKeyboard keyboard; // Hard dependency!
public:
    MacBookBad() {
        // Forced to use WiredKeyboard - can't swap!
    }
    void useKeyboard() {
        keyboard.type();
    }
};

// ========================================
// THE SOLUTION:
// Depend on abstraction (Keyboard interface)
// ========================================

class Keyboard {
public:
    virtual void type() = 0;
    virtual ~Keyboard() {}
};

class WiredKeyboardGood : public Keyboard {
public:
    void type() override {
        std::cout << "Typing on wired keyboard" << std::endl;
    }
};

class BluetoothKeyboard : public Keyboard {
public:
    void type() override {
        std::cout << "Typing on Bluetooth keyboard" << std::endl;
    }
};

class MacBook {
    Keyboard* keyboard;
public:
    MacBook(Keyboard* kb) : keyboard(kb) {} // Dependency injection!
    
    void useKeyboard() {
        keyboard->type();
    }
};

int main() {
    std::cout << "=== PROBLEM (DIP Violation) ===" << std::endl;
    MacBookBad macbookBad;
    macbookBad.useKeyboard(); // Stuck with wired keyboard!
    
    std::cout << "\n=== SOLUTION (DIP Compliant) ===" << std::endl;
    WiredKeyboardGood wired;
    MacBook macbook1(&wired);
    macbook1.useKeyboard();
    
    BluetoothKeyboard bluetooth;
    MacBook macbook2(&bluetooth);
    macbook2.useKeyboard();
    
    return 0;
}
