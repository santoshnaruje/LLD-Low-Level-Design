from abc import ABC, abstractmethod

# TITLE: Dependency Inversion Principle (DIP) - MacBook Example

# ========================================
# THE PROBLEM (VIOLATION):
# MacBook depends on concrete WiredKeyboard
# ========================================

class WiredKeyboardBad:
    def type(self):
        print("Typing on wired keyboard")

class MacBookBad:
    def __init__(self):
        # Hard dependency!
        self.keyboard = WiredKeyboardBad()
    
    def use_keyboard(self):
        self.keyboard.type()

# ========================================
# THE SOLUTION:
# Depend on abstraction
# ========================================

class Keyboard(ABC):
    @abstractmethod
    def type(self): pass

class WiredKeyboard(Keyboard):
    def type(self):
        print("Typing on wired keyboard")

class BluetoothKeyboard(Keyboard):
    def type(self):
        print("Typing on Bluetooth keyboard")

class MacBook:
    def __init__(self, keyboard: Keyboard): # Dependency injection!
        self.keyboard = keyboard
    
    def use_keyboard(self):
        self.keyboard.type()

if __name__ == "__main__":
    print("=== PROBLEM (DIP Violation) ===")
    macbook_bad = MacBookBad()
    macbook_bad.use_keyboard() # Stuck with wired keyboard!
    
    print("\n=== SOLUTION (DIP Compliant) ===")
    wired = WiredKeyboard()
    macbook1 = MacBook(wired)
    macbook1.use_keyboard()
    
    bluetooth = BluetoothKeyboard()
    macbook2 = MacBook(bluetooth)
    macbook2.use_keyboard()
