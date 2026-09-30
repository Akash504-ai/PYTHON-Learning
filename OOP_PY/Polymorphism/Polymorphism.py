class Creditcard:
    def pay(self):
        print("Payment through credit card")

class ATM:
    def pay(self):
        print("Payment through ATM")

class UPI:
    def pay(self):
        print("Payment through UPI")

c1 = Creditcard()
a1 = ATM()
u1 = UPI()

c1.pay()
a1.pay()
u1.pay()