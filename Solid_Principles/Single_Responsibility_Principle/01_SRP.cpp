#include <iostream>
#include <string>

// TITLE: Single Responsibility Principle (SRP) - Invoice Example

class Marker {
public:
    std::string name;
    std::string color;
    int year;
    double price;
    
    Marker(std::string n, std::string c, int y, double p) 
        : name(n), color(c), year(y), price(p) {}
};

// ========================================
// THE PROBLEM (VIOLATION):
// Invoice class has 3 responsibilities!
// ========================================

class InvoiceBad {
    Marker marker;
    int quantity;
public:
    InvoiceBad(Marker m, int q) : marker(m), quantity(q) {}
    
    // Responsibility 1: Calculate total
    double calculateTotal() {
        return marker.price * quantity;
    }
    
    // Responsibility 2: Print invoice
    void printInvoice() {
        std::cout << "Invoice: " << marker.name << " x" << quantity 
                  << " = $" << calculateTotal() << std::endl;
    }
    
    // Responsibility 3: Save to database
    void saveToDB() {
        std::cout << "Saving invoice to database..." << std::endl;
    }
};

// ========================================
// THE SOLUTION:
// Separate responsibilities into different classes
// ========================================

class Invoice {
    Marker marker;
    int quantity;
public:
    Invoice(Marker m, int q) : marker(m), quantity(q) {}
    
    double calculateTotal() const {
        return marker.price * quantity;
    }
    
    Marker getMarker() const { return marker; }
    int getQuantity() const { return quantity; }
};

class InvoicePrinter {
public:
    void print(const Invoice& invoice) {
        std::cout << "Invoice: " << invoice.getMarker().name 
                  << " x" << invoice.getQuantity()
                  << " = $" << invoice.calculateTotal() << std::endl;
    }
};

class InvoiceDao {
public:
    void saveToDB(const Invoice& invoice) {
        std::cout << "Saving invoice to database..." << std::endl;
    }
};

int main() {
    Marker marker("Sharpie", "Blue", 2023, 2.5);
    
    std::cout << "=== PROBLEM (SRP Violation) ===" << std::endl;
    InvoiceBad badInvoice(marker, 10);
    badInvoice.printInvoice();
    badInvoice.saveToDB();
    
    std::cout << "\n=== SOLUTION (SRP Compliant) ===" << std::endl;
    Invoice invoice(marker, 10);
    
    InvoicePrinter printer;
    printer.print(invoice);
    
    InvoiceDao dao;
    dao.saveToDB(invoice);
    
    return 0;
}
