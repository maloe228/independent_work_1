from random import *

b = [randint(-100, 100) for n in range(10)]

sk = 0

n = int(input())

print(b)

for i in b:
    if i < n:
        sk += 1

print(sk)
