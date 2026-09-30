class Calculator:
    def add(self, a, b, c=0):
        print("Sum : ", a+b+c)

c1 = Calculator()
c1.add(10,20)
c1.add(10,20,30)