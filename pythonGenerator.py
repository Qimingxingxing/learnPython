from collections import Iterator, Iterable
L = [x * x for x in range(10)]
# this is a generator
g = (x * x for x in range(10))

for i in g:
    print(i)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(7):
    print(i)
print(isinstance(L, Iterable))
print(isinstance(L, Iterator))
print(isinstance(g, Iterable))
print(isinstance(g, Iterator))

# convert a Collections to generator
gL = iter(L)
print(isinstance(gL,Iterator))
