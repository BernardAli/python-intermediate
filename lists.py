cars = ['nissan', 'opel', 'ford', 'tata', 'honda']
print(cars)

mylist = ['samsung', 'hitachi', 'toshiba', 'daewoo']
print(mylist[-1])
print(mylist)

for i in mylist:
    print(i)

if 'banana' in mylist:
    print('True')
else:
    print('No')

mylist.append("hyundai")
mylist.insert(2, "renault")
print(len(mylist))
print(mylist)

mylist.pop()
mylist.remove('renault')
mylist.sort()
mylist.reverse()
# mylist.clear()
print(mylist)

newList = [0] * 5
newList2 = list(range(1, 11))
print(newList)
print(newList + newList2)

# slicing
print(newList2)
a = newList2[1:5]
b = newList2[:5:2]
b = newList2[:5:-1]
print(a)
print(b)

fruits = ['banana', 'cherry', 'apple']
fruits_cp = fruits.copy()

fruits_cp.append('pawpaw')
print(fruits_cp)
print(fruits)

a = [1, 2, 3, 4, 5, 6]
b = [i ** 2 for i in a]
print(b)

