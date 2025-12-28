# TITLE: Single Responsibility Principle (SRP) - Invoice Example

class Marker:
    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price

# ========================================
# THE PROBLEM (VIOLATION):
# Invoice class has 3 responsibilities!
# ========================================

class InvoiceBad:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity
    
    # Responsibility 1: Calculate total
    def calculate_total(self):
        return self.marker.price * self.quantity
    
    # Responsibility 2: Print invoice
    def print_invoice(self):
        print(f"Invoice: {self.marker.name} x{self.quantity} = ${self.calculate_total()}")
    
    # Responsibility 3: Save to database
    def save_to_db(self):
        print("Saving invoice to database...")

# ========================================
# THE SOLUTION:
# Separate responsibilities
# ========================================

class Invoice:
    def __init__(self, marker, quantity):
        self.marker = marker
        self.quantity = quantity
    
    def calculate_total(self):
        return self.marker.price * self.quantity

class InvoicePrinter:
    def print(self, invoice):
        print(f"Invoice: {invoice.marker.name} x{invoice.quantity} = ${invoice.calculate_total()}")

class InvoiceDao:
    def save_to_db(self, invoice):
        print("Saving invoice to database...")

if __name__ == "__main__":
    marker = Marker("Sharpie", "Blue", 2023, 2.5)
    
    print("=== PROBLEM (SRP Violation) ===")
    bad_invoice = InvoiceBad(marker, 10)
    bad_invoice.print_invoice()
    bad_invoice.save_to_db()
    
    print("\n=== SOLUTION (SRP Compliant) ===")
    invoice = Invoice(marker, 10)
    
    printer = InvoicePrinter()
    printer.print(invoice)
    
    dao = InvoiceDao()
    dao.save_to_db(invoice)
