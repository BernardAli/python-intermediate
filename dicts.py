myDict = {
    "name": "Ben",
    "age": 30,
    "city": "Kumasi"
}

myDict2 = dict(name="Muna", age=28, city="Kumasi")

print(myDict)
print(myDict["name"])
print(myDict["city"])

myDict["email"] = "ali@gmail.com"
myDict["email"] = "ali.92@gmail.com"

del myDict["email"]

myDict.pop('name')
print(myDict)

if "name" in myDict:
    print(myDict["name"])
else:
    print("No name available")

try:
    myDict["email"]
except:
    print("Error")

for key in myDict.keys():
    print(key)

for key in myDict:
    print(key)

for values in myDict.values():
    print(values)

for values, keys in myDict.items():
    print(values, keys)

myDict_cp = myDict.copy()
myDict_cp['email'] = 'ali@xyz.com'
print(myDict_cp)
print(myDict)

newDict = myDict.update(myDict2)
print(newDict)

