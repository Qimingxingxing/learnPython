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

def keyword(a, b, **c):
    print("a", a, "b", b, "c", c)
keyword("hello","world")
keyword("hello","world", q = "q", m = "m")

d = {"qiming": 1,
    "yiming" : 2
    }
keyword("","",**d)

def addDigits(num):
        while num // 10 > 0:
            num = num % 10 + num // 10
        return num
print(addDigits(38))
