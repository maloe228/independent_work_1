from random import *

b = [randint(-100, 100) for n in range(11)]

print(b)

i = max(b)
d = min(b)

a1 = (b.index(max(b)))
a2 = (b.index(min(b)))

b.insert(a1, d)
b.insert(a2, i)

b.pop(a2 + 1)
b.pop(a1 + 1)

print(b)
