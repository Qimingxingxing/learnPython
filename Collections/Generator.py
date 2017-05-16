g = (x * x for x in range(5))
for i in g:
    print(i)
def func(max):
    while max > 0:
        yield max
        max -= 2
        yield max

for n in func(6):
    print(n)
print(list(func(6)))
