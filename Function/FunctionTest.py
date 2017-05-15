def func(x = 5, y = 5):
    return x, y
print(func(1,2))
print(func())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print(calc(1,2,3))
print(calc())
nums = [1,2,3]
print(calc(*nums))
print(*nums)
