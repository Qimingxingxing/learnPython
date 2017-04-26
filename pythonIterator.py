from collections import Iterable
l = [1,2,3]
for i in range(len(l)):
    print(l[i])
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)
# judge if it is iterable
isinstance('abc', Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
l = [x * x for x in range(1, 11)]
print(l)
[x * x for x in range(1, 11) if x % 2 == 0]
