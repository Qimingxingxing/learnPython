class Animal(object):
    def say(self):
        print("I'm an animal")

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def say(self):
        print("I'm a dog")

dog = Dog()
dog.say()
animal = Dog()
animal.say()
animal.eat()
