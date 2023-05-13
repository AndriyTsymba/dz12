#4
class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_total_balance(self):
        total_balance = 0
        for customer in self.customers:
            total_balance += customer.balance
        return total_balance
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
bank = Bank()
customer1 = BankAccount("Slavik", 1500)
customer2 = BankAccount("Igor", 10000)
bank.add_customer(customer1)
bank.add_customer(customer2)
print(bank.get_total_balance())
