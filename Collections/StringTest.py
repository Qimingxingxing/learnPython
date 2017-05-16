for i, s in enumerate("hello"):
    print(i, s)

def removePrime(x):
    if x == 1 :
        return True
    for i in range(2, x):
        if x % i == 0:
            return True
    return False
print(list(filter(removePrime, range(1,101))))

