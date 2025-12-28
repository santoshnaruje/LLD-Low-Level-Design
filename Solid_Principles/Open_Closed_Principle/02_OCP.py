from abc import ABC, abstractmethod

# TITLE: Open/Closed Principle (OCP) - InvoiceDao Example

class Invoice:
    def __init__(self, amount):
        self.amount = amount

# ========================================
# THE PROBLEM (VIOLATION):
# To add MongoDB, we must MODIFY this class
# ========================================

class InvoiceDaoBad:
    def save_to_db(self, invoice):
        print("Saving to MySQL DB")
    
    def save_to_file(self, invoice):
        print("Saving to File")
    
    # Adding new method = MODIFYING class (violates OCP!)
    def save_to_mongodb(self, invoice):
        print("Saving to MongoDB")

# ========================================
# THE SOLUTION:
# Use abstraction - extend via NEW classes
# ========================================

class InvoiceDao(ABC):
    @abstractmethod
    def save(self, invoice):
        pass

class DatabaseInvoiceDao(InvoiceDao):
    def save(self, invoice):
        print("Saving to MySQL Database")

class FileInvoiceDao(InvoiceDao):
    def save(self, invoice):
        print("Saving to File System")

class MongoDBInvoiceDao(InvoiceDao):
    def save(self, invoice):
        print("Saving to MongoDB")

if __name__ == "__main__":
    inv = Invoice(100.0)
    
    print("=== PROBLEM (OCP Violation) ===")
    bad_dao = InvoiceDaoBad()
    bad_dao.save_to_db(inv)
    bad_dao.save_to_file(inv)
    bad_dao.save_to_mongodb(inv)
    
    print("\n=== SOLUTION (OCP Compliant) ===")
    db_dao = DatabaseInvoiceDao()
    db_dao.save(inv)
    
    file_dao = FileInvoiceDao()
    file_dao.save(inv)
    
    mongo_dao = MongoDBInvoiceDao()
    mongo_dao.save(inv)
