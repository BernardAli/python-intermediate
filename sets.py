myset = { 1, 2, 3, 4, 5, 1, 2, 3, 8}
print(myset)
set1 = set(list(range(0, 10)))
print(set1)

myset.add(9)
myset.add(6)
myset.add(7)
print(myset)

myset.pop()
myset.discard(5)
print(myset)

for x in myset:
    print(x)

if 1 in myset:
    print('Yes')
else:
    print("No")

# Union
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {1, 2, 3, 5, 7}

print(odds.union(even))

# intersections
print(odds.intersection(even))
print(odds.intersection(prime))
print(odds.difference(prime))
print(odds.symmetric_difference(prime))

print(odds.issubset(even))
print(odds.issubset(numbers))
print(odds.issuperset(even))
print(numbers.issuperset(even))
print(numbers.isdisjoint(even))
print(odds.isdisjoint(even))

a = frozenset([1, 2, 3, 4, 5])
print(a)