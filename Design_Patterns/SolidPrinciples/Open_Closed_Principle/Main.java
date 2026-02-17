// TITLE: Open/Closed Principle (OCP) - InvoiceDao Example

class Invoice {
    double amount;

    Invoice(double amount) {
        this.amount = amount;
    }
}

// ========================================
// THE PROBLEM (VIOLATION):
// To add MongoDB, we must MODIFY this class
// ========================================

class InvoiceDaoBad {
    public void saveToDB(Invoice invoice) {
        System.out.println("Saving to MySQL DB");
    }

    public void saveToFile(Invoice invoice) {
        System.out.println("Saving to File");
    }

    // Adding new method = MODIFYING class (violates OCP!)
    public void saveToMongoDB(Invoice invoice) {
        System.out.println("Saving to MongoDB");
    }
}

// ========================================
// THE SOLUTION:
// Use interface - extend via NEW classes
// ========================================

interface InvoiceDao {
    void save(Invoice invoice);
}

class DatabaseInvoiceDao implements InvoiceDao {
    public void save(Invoice invoice) {
        System.out.println("Saving to MySQL Database");
    }
}

class FileInvoiceDao implements InvoiceDao {
    public void save(Invoice invoice) {
        System.out.println("Saving to File System");
    }
}

class MongoDBInvoiceDao implements InvoiceDao {
    public void save(Invoice invoice) {
        System.out.println("Saving to MongoDB");
    }
}

public class Main {
    public static void main(String[] args) {
        Invoice inv = new Invoice(100.0);

        System.out.println("=== PROBLEM (OCP Violation) ===");
        InvoiceDaoBad badDao = new InvoiceDaoBad();
        badDao.saveToDB(inv);
        badDao.saveToFile(inv);
        badDao.saveToMongoDB(inv);

        System.out.println("\n=== SOLUTION (OCP Compliant) ===");
        InvoiceDao dbDao = new DatabaseInvoiceDao();
        dbDao.save(inv);

        InvoiceDao fileDao = new FileInvoiceDao();
        fileDao.save(inv);

        InvoiceDao mongoDao = new MongoDBInvoiceDao();
        mongoDao.save(inv);
    }
}
