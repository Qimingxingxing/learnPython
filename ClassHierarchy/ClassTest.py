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

    @name.setter
    def score(self, score):
        self.__score = score


class GraduateStudent(Student):
    __slots__ = ("__age", "__name", "__score")
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__age = 1


qiming = Student("qiming", 100)
qiming.name = "yiming"
print(qiming.name)
qiming = GraduateStudent("qiming", 100)
# qiming.__age = 1
# 单下划线可以这么做
