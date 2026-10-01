# We can use inheritance and method overriding to add new payment methods without modifying the existing payment classes.

class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class PayPal(Payment):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")

p1 = CreditCard()
p2 = UPI()
p3 = PayPal()

p1.pay(1000)
p2.pay(2000)
p3.pay(3000)

"""
Why is this good?
---> Suppose we want to add a new payment method, such as Net Banking.
We can simply create a new class.

That's it! We don't need to modify the existing CreditCard, UPI, or PayPal classes.
We extend the system by adding a new class instead of changing existing payment classes.
"""