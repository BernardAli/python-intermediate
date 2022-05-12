mytuple = ('Max', 28, 'Boston')
print(mytuple)
print(type(mytuple))

item = mytuple[2]
print(item)

p = ('b', 'a', 'n', 'a', 'n', 'a')
print(p.count('a'))
print(p.count('m'))
print(p.index('n'))

m = list(p)
print(m)
print(type(m))

p = tuple(m)
print(type(p))

name, age, city = mytuple
print(name)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
n1, *n2, n3 = numbers
print(n3)
print(n2)
