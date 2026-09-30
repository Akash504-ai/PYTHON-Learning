class BankAccount:
    def __init__(self, name, balance):
        self.name = name                # Public
        self._account_type = "Savings"  # Protected (convention)
        self.__balance = balance        # Private (name-mangled)

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Public method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    # Public method to access private data
    def get_balance(self):
        return self.__balance

    def show_details(self):
        print(f"Account holder: {self.name}")
        print(f"Account type: {self._account_type}")
        print(f"Balance: ₹{self.__balance}")


account = BankAccount("Akash", 10000)

# Accessing public data
print(account.name)

# Accessing protected data (possible, but discouraged externally)
print(account._account_type)

# Accessing private data through a public method
print(account.get_balance())

# Modifying balance through controlled methods
account.deposit(2000)
account.withdraw(3000)
account.show_details()