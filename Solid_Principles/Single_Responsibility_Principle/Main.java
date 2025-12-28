// TITLE: Single Responsibility Principle (SRP) - Invoice Example

class Marker {
    String name;
    String color;
    int year;
    double price;

    Marker(String name, String color, int year, double price) {
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
    private Marker marker;
    private int quantity;

    InvoiceBad(Marker marker, int quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    // Responsibility 1: Calculate total
    public double calculateTotal() {
        return marker.price * quantity;
    }

    // Responsibility 2: Print invoice
    public void printInvoice() {
        System.out.println("Invoice: " + marker.name + " x" + quantity + " = $" + calculateTotal());
    }

    // Responsibility 3: Save to database
    public void saveToDB() {
        System.out.println("Saving invoice to database...");
    }
}

// ========================================
// THE SOLUTION:
// Separate responsibilities
// ========================================

class Invoice {
    private Marker marker;
    private int quantity;

    Invoice(Marker marker, int quantity) {
        this.marker = marker;
        this.quantity = quantity;
    }

    public double calculateTotal() {
        return marker.price * quantity;
    }

    public Marker getMarker() {
        return marker;
    }

    public int getQuantity() {
        return quantity;
    }
}

class InvoicePrinter {
    public void print(Invoice invoice) {
        System.out.println("Invoice: " + invoice.getMarker().name +
                " x" + invoice.getQuantity() +
                " = $" + invoice.calculateTotal());
    }
}

class InvoiceDao {
    public void saveToDB(Invoice invoice) {
        System.out.println("Saving invoice to database...");
    }
}

public class Main {
    public static void main(String[] args) {
        Marker marker = new Marker("Sharpie", "Blue", 2023, 2.5);

        System.out.println("=== PROBLEM (SRP Violation) ===");
        InvoiceBad badInvoice = new InvoiceBad(marker, 10);
        badInvoice.printInvoice();
        badInvoice.saveToDB();

        System.out.println("\n=== SOLUTION (SRP Compliant) ===");
        Invoice invoice = new Invoice(marker, 10);

        InvoicePrinter printer = new InvoicePrinter();
        printer.print(invoice);

        InvoiceDao dao = new InvoiceDao();
        dao.saveToDB(invoice);
    }
}
