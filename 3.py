from random import *

b = [randint(-25, 25) for n in range(5)]

p = 1

print(b)

for i in b:
    p *= i
print(p)
