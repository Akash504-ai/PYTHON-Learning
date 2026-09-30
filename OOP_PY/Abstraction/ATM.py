from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class SBI(ATM):
    def __init__(self, b):
        self.b = b

    def withdraw(self, a):
        if a<=0:
            print("Invalid")
        elif a>self.b:
            print("Insufficient")
        else:
            self.b-=a
            print(f"₹{a} withdrawn successfully")
            print(f"Remaining balance: ₹{self.b}")

s1 = SBI(10000)
s1.withdraw(200)