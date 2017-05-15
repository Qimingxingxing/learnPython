def my_abs(x):
    print(1)
print(my_abs(-1))
def varParameter(a, *b):
    print(b[-2:-1])
varParameter(5, 1,2,3)
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)

func(c=50, a=100)

# VarArgs parameters
def total( *numbers, a = 5, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
    #iterate through all the items
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
l = ['A', 'B','C', ' ', '']
l = list(filter(lambda x: x and x.strip(), l))
print(l)
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True )
