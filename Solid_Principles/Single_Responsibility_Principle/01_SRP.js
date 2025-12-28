// TITLE: Single Responsibility Principle (SRP) - Invoice Example

class Marker {
    constructor(name, color, year, price) {
        this.name = name;
        this.color = color;
        this.year = year;
        this.price = price;
    }
}

// ========================================
// THE PROBLEM (VIOLATION):
// Invoice class has 3 responsibilities!
// ========================================

class InvoiceBad {
    constructor(marker, quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    // Responsibility 1: Calculate total
    calculateTotal() {
        return this.marker.price * this.quantity;
    }

    // Responsibility 2: Print invoice
    printInvoice() {
        console.log(`Invoice: ${this.marker.name} x${this.quantity} = $${this.calculateTotal()}`);
    }

    // Responsibility 3: Save to database
    saveToDB() {
        console.log("Saving invoice to database...");
    }
}

// ========================================
// THE SOLUTION:
// Separate responsibilities
// ========================================

class Invoice {
    constructor(marker, quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    calculateTotal() {
        return this.marker.price * this.quantity;
    }
}

class InvoicePrinter {
    print(invoice) {
        console.log(`Invoice: ${invoice.marker.name} x${invoice.quantity} = $${invoice.calculateTotal()}`);
    }
}

class InvoiceDao {
    saveToDB(invoice) {
        console.log("Saving invoice to database...");
    }
}

// Usage
const marker = new Marker("Sharpie", "Blue", 2023, 2.5);

console.log("=== PROBLEM (SRP Violation) ===");
const badInvoice = new InvoiceBad(marker, 10);
badInvoice.printInvoice();
badInvoice.saveToDB();

console.log("\n=== SOLUTION (SRP Compliant) ===");
const invoice = new Invoice(marker, 10);

const printer = new InvoicePrinter();
printer.print(invoice);

const dao = new InvoiceDao();
dao.saveToDB(invoice);
