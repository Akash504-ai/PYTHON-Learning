# Imagine we have a payment system that supports Credit Card and UPI payments.

class Payment:
    def pay(self, payment_type:str, amount:int):
        if payment_type == "Credit Card":
            print(f"{amount}$ paid through Credit Card")
        elif payment_type == "UPI":
            print(f"{amount}$ paid through UPI")

payment = Payment()
payment.pay("Credit Card", 5000)
payment.pay("UPI", 15000)

"""
Why is this bad?
Now imagine we want to add a new payment method, such as PayPal.
We must modify the existing Payment class and add another elif condition.
Every time we add a new payment method, we have to change the same class. As the number of payment methods increases, the code becomes harder to maintain.
Therefore, this design violates OCP.
"""