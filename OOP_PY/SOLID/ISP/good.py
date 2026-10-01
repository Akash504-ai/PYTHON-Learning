class Workable:
    def work(self):
        pass


class Eatable:
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class Robot(Workable):
    def work(self):
        print("Robot is working")


# Creating objects
human = Human()
robot = Robot()

human.work()
human.eat()

robot.work()