class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Human(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        pass