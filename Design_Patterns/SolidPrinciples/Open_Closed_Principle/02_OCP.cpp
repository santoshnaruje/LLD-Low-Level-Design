#include <iostream>

// TITLE: Open/Closed Principle (OCP) - InvoiceDao Example

class Invoice {
public:
    double amount;
    Invoice(double amt) : amount(amt) {}
};

// ========================================
// THE PROBLEM (VIOLATION):
// To add MongoDB, we must MODIFY this class
// ========================================

class InvoiceDaoBad {
public:
    void saveToDB(Invoice inv) {
        std::cout << "Saving to MySQL DB" << std::endl;
    }
    
    void saveToFile(Invoice inv) {
        std::cout << "Saving to File" << std::endl;
    }
    
    // Adding new method = MODIFYING class (violates OCP!)
    void saveToMongoDB(Invoice inv) {
        std::cout << "Saving to MongoDB" << std::endl;
    }
};

// ========================================
// THE SOLUTION:
// Use interface - extend via NEW classes
// ========================================

class InvoiceDao {
public:
    virtual void save(Invoice inv) = 0;
    virtual ~InvoiceDao() {}
};

class DatabaseInvoiceDao : public InvoiceDao {
public:
    void save(Invoice inv) override {
        std::cout << "Saving to MySQL Database" << std::endl;
    }
};

class FileInvoiceDao : public InvoiceDao {
public:
    void save(Invoice inv) override {
        std::cout << "Saving to File System" << std::endl;
    }
};

// Adding MongoDB doesn't modify existing code!
class MongoDBInvoiceDao : public InvoiceDao {
public:
    void save(Invoice inv) override {
        std::cout << "Saving to MongoDB" << std::endl;
    }
};

int main() {
    Invoice inv(100.0);
    
    std::cout << "=== PROBLEM (OCP Violation) ===" << std::endl;
    InvoiceDaoBad badDao;
    badDao.saveToDB(inv);
    badDao.saveToFile(inv);
    badDao.saveToMongoDB(inv);
    
    std::cout << "\n=== SOLUTION (OCP Compliant) ===" << std::endl;
    InvoiceDao* dbDao = new DatabaseInvoiceDao();
    dbDao->save(inv);
    
    InvoiceDao* fileDao = new FileInvoiceDao();
    fileDao->save(inv);
    
    InvoiceDao* mongoDao = new MongoDBInvoiceDao();
    mongoDao->save(inv);
    
    delete dbDao;
    delete fileDao;
    delete mongoDao;
    
    return 0;
}
