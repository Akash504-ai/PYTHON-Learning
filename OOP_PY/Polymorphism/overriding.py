class Payment:
    def pay(self):
        print("Processing payment")


class Creditcard(Payment):
    def pay(self):
        print("Payment through credit card")


class ATM(Payment):
    def pay(self):
        print("Payment through ATM")


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


c1 = Creditcard()
a1 = ATM()
u1 = UPI()

c1.pay()
a1.pay()
u1.pay()