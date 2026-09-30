"""
Bank Account Management

Create a class BankAccount with the following:

Attributes:

account_holder → name of the account holder

balance → initial account balance

account_number → account number

Methods:

deposit(amount) - adds the given amount to the balance. If the amount is invalid, display an appropriate message.

withdraw(amount) - withdraws the given amount if the balance is sufficient. Otherwise, display "Insufficient balance".

show_balance() - displays the account holder's name and current balance.
"""

class BankAccount:
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"After deposit your balance is {self.balance}\n")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"After withdraw your balance is {self.balance}\n")

    def show_balance(self):
        print(f"Account holder name is {self.account_holder} and curr balance is {self.balance}\n")

b1 = BankAccount("Akash", 6000, 123456789861745)
b1.show_balance()
b1.deposit(50000)
b1.show_balance()
b1.withdraw(2000)
b1.show_balance()