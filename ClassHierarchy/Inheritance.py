class Animal(object):
    def say(self):
        print("I'm an animal")

    def eat(self):
        print("Animal is eating")

    def __len__(self):
        return 100

class Dog(Animal):
    def say(self):
        print("I'm a dog")

cat = Animal()
cat.say()
print(len(cat))
animal = Dog()
animal.say()
animal.eat()

def fn():
    pass
import types
print(type("abc") == str)
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(dir(""))
