from random import *

b = [randint(1, 100) for n in range(10)]

k = int(input())

s = 0

print(b)

for i in b:
    if i % k == 0:
        s += i

print(s)
