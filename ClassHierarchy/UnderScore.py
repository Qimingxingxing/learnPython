class Fib(object):
    def __init__(self):
        self.a, self.b = 0 ,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, slice):
            return [1,2,3]
        return item

for n in Fib():
    print(n)
print(Fib()[5:6])

