def add(x, y, f):
    return f(x) + f(y)
print(add(5, -1, abs))

def powReverse(x, y, f):
    return f(y, x)
print(powReverse(5, 1, pow))
def reverseSorted(x, y):
    if x < y :
        return 1
    elif x > y:
        return -1
    return 0
L = ("b","a")

sorted([1,2,3,4,5], reverse = True)
print(sorted(L, key = str.upper))
print(L)

