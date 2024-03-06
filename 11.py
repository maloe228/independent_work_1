from random import *

b = [randint(-100, 100) for n in range(10)]

print(b)

c = 100

for i in b:
    if i >= 0:
        if i < c:
            c = i
print(c)
