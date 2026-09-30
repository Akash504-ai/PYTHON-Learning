class Student:
    def __init__(self, n, a, g):
        self.a = a
        self.n = n
        self.g = g

    def displey(self):
        print(f"Hey there! My name is {self.n}, I am {self.a}yr old and I am a {self.g} cnadidate.")

s1 = Student("Akash", 21, "Male")
s1.displey()