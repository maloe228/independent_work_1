from random import *

s = 0

b = [randint(-100, 100) for n in range(10)]

print(b)

for i in b:
    if i < 0:
        s += 1
print('*****', s, '*****')
