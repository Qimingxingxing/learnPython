underscore = "_"
class Robot:
    """Represents a robot, with a name."""
    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.__name = name
        print("(Initializing {})".format(self.__name))
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1
        self._age = 1
    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.__name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.__name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))
    def say_hi(self):
        """Greeting by the robot.
Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.__name))
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))
'''
droid1 = Robot("R2-D2")
droid1.say_hi()
print(droid1._age)
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()

class Person:

   def __init__(self):
       self.name = 'haha'#私有属性
       self.age = 22

   def get_name(self):##私有方法
       return self.name

   def get_age(self):
       return self.age

person = Person()
# print person.get_age()
# print person.__get_name()

class Boy(Person):
    def __init__(self):
        self.name = 'qiming'
    def die(self):
        pass
qiming = Boy()
print(qiming.get_name())

'''
