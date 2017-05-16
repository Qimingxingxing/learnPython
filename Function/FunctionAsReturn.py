def lazy_factor(*args):
    def factor():
        result = 1
        for i in args:
            result *= i
        return result
    return factor

f = lazy_factor(1,2,3,4,5)
print(f())
