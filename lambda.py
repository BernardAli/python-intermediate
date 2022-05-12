# lambda arguments: expression
from functools import reduce

po = lambda x, y: x ** y
print(po(2, 3))

point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_sorted = sorted(point2D, key=lambda x: x[0] + x[1])
print(point2D)
print(point2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
c = [x * 2 for x in a]
print(list(b))
print(c)

# filter(func, seq)
d = filter(lambda x: x % 2 == 0, a)
e = [x for x in a if x % 2 == 0]
print(list(d))
print(e)

# reduce(func, seq)
prod = reduce(lambda x, y: x * y, a)
print(prod)
