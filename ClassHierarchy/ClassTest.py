class Student(object):
    __slots__ = ("__name", "__score")

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def __str__(self):
        return "your father"
    __repr__ = __str__


qiming = Student("qiming", 100)
qiming.name = "yiming"
print(qiming.name)
# qiming.__age = 1
# 单下划线可以这么做
print(qiming)

class Cls(object):
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x


cls = Cls(1)
print(cls.x)
