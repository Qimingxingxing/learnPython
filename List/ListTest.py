# http://www.cnblogs.com/linjiqin/p/3608541.html
# cmd + Y delete line

L = [1,2,3,4,5]
print(L)
del L[1]
print(L)
L.pop(1)
print(L)
L.append(5)
print(L)
L.insert(1, 10)
print(L)
L.sort()
print(L)
listComprehension = [i for i in range(10) if i % 2 == 0]
print(listComprehension)
print(L)
listMultiply = [10] * 10
print(listMultiply)
# listSubstract = [1] - []
# print(listSubstract)
print(L)
print(L)
print(L)
print(L)
L = [5 for i in range(5)]
L[0] = 1
print(L.index(5)) #FIRST POINT
L1 = [1,2,3]
L2 = L1
L3 = L1[:]
L1.reverse()
L += L1
print(L2)
print(L3)
sum = 10
if sum == 5:
    print("sum is %d" % 5)
elif sum < 5:
    print("sum is less than %d" % 5)
else:
    print("sum is greater than {}".format(5))
