class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60
print(s.score)


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

def outerFunction(func):
    def innerFunction(*args, **kwargs):
        func(*args, **kwargs)
        print("%s" % func.__name__)
    return innerFunction

@outerFunction # now = outerFunction(now) = innerFunction
def now():
    print("5/16")
now()
