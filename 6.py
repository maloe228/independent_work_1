from random import *

b = [randint(-100, 100) for n in range(10)]

sk, sp = 0, 0

print(b)

for i in b:
    if i >= 0:
        sk += 1
        sp += i

print(sk, sp)
