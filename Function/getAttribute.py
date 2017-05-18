class Student(object):
    def __init__(self):
        self.name = "Michael"
    def __getattr__(self, item):
        if item =="score":
            return 99
        if item == "age":
            return lambda :25
        raise AttributeError('has no attribute %s' % item)
s = Student()
print(s.score)
print(s.age())
print(s.ab)
