# bankaccount.py
# by Tony Gaddis

"""The BankAccount class simulates a bank account"""

class BankAccount:

    def __init__(self, bal):
        self.balance = bal

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        # self.balance = self.balance + amount
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Error: Not enough money!")

    def __str__(self):
        return f"Your balance: ${self.balance:.2f}"






