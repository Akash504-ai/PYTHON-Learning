class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def __init__(self, name:str, age:int, breed:str):
        super().__init__(name, age)

        self.breed = breed

    def berk(self):
        print("I am barking")

    def info(self):
        print("[===Info===]")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Breed : {self.breed}")

dog = Dog("Golde",2,"German Sheparde")
dog.info()
dog.berk()
dog.eat()
dog.sleep()