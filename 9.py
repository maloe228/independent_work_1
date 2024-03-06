from random import *

b = [randint(-100, 100) for n in range(10)]

print(b)

for i in b:
    if i < 0:
        print('0')
    elif i > 0:
        print('1')
    elif i == 0:
        print('0')


