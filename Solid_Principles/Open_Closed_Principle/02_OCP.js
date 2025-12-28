// TITLE: Open/Closed Principle (OCP) - InvoiceDao Example

class Invoice {
    constructor(amount) {
        this.amount = amount;
    }
}

// ========================================
// THE PROBLEM (VIOLATION):
// To add MongoDB, we must MODIFY this class
// ========================================

class InvoiceDaoBad {
    saveToDB(invoice) {
        console.log("Saving to MySQL DB");
    }

    saveToFile(invoice) {
        console.log("Saving to File");
    }

    // Adding new method = MODIFYING class (violates OCP!)
    saveToMongoDB(invoice) {
        console.log("Saving to MongoDB");
    }
}

// ========================================
// THE SOLUTION:
// Use polymorphism - extend via NEW classes
// ========================================

class DatabaseInvoiceDao {
    save(invoice) {
        console.log("Saving to MySQL Database");
    }
}

class FileInvoiceDao {
    save(invoice) {
        console.log("Saving to File System");
    }
}

class MongoDBInvoiceDao {
    save(invoice) {
        console.log("Saving to MongoDB");
    }
}

// Usage
const inv = new Invoice(100.0);

console.log("=== PROBLEM (OCP Violation) ===");
const badDao = new InvoiceDaoBad();
badDao.saveToDB(inv);
badDao.saveToFile(inv);
badDao.saveToMongoDB(inv);

console.log("\n=== SOLUTION (OCP Compliant) ===");
const dbDao = new DatabaseInvoiceDao();
dbDao.save(inv);

const fileDao = new FileInvoiceDao();
fileDao.save(inv);

const mongoDao = new MongoDBInvoiceDao();
mongoDao.save(inv);
