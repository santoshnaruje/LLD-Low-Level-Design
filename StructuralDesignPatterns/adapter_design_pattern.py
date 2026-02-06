# Indian plug → US socket
# Use adapter

class OldPayment:
    def __init__(self, amount):
        self.amount = amount

    def pay_now(self):
        return self.amount


class NewPayment:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        return self.amount


class AdapterPayment:
    def __init__(self, new_payment):
        self.new_payment = new_payment

    def pay_now(self):
        print(self.new_payment.make_payment())


if __name__ == '__main__':
    payment = AdapterPayment(NewPayment(100))
    payment.pay_now()
