class Student:
    def __init__(self, n:str, a:int, g:str) -> None:
        self.name = n
        self.age = a
        self.gender = g

    def display(self) -> None:
        print("Hi!\n")
        print(f"My name is {self.name}, I am {self.age}yr. old and I am a {self.gender}")

s1 = Student("Akash",21,"Male")
s1.display()