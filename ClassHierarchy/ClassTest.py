class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

class Teacher(object):
    pass

qiming = Student("qiming", 100)
qiming.hello = "hello"
qiming.print_score()
print(qiming.get_name())
