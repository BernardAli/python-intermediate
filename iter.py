from itertools import product, permutations, combinations, \
    combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product
a = [1, 2]
b = [2]
prod = product(a, b, repeat=2)
print(list(prod))

# permutation
c = [1, 2, 3, 4]
perm = permutations(c, 2)
print(list(perm))
print(len(c))

# combinations
comb = combinations(c, 2)
print(list(comb))

com_wr = combinations_with_replacement(c, 2)
print((list(com_wr)))

acc = accumulate(c, func=operator.mul)
print(c)
print(list(acc))

persons = [{'name': 'Ali', 'age': 29}, {'name': 'Isaac', 'age': 29}, {'name': 'Eddie', 'age': 27}]
print(persons)

def smaller_than_three(x):
    return x < 3


# groupby
d = [1, 2, 3, 4, 5]
group_obj = groupby(d, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

group_person = groupby(persons, key=lambda x: x['age'])
for key, value in group_person:
    print(key, list(value))


# count
for i in count(0):
    print(i)
    if i == 15:
        break

# cycle
# for i in cycle(d):
#     print(i)


# repeat
for i in repeat(1, 4):
    print(i)
