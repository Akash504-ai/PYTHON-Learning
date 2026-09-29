class Student:
    def __init__(self, n:str, a:int, g:str) -> None:
        self.name = n
        self.age = a
        self. gender = g

    def disp(self) -> None:
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Student("Akash", 21, "Male")
s1.disp()