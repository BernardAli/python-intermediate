my_string = "Hello Ben"
# my_string2 = 'Hello Eddie'

char = my_string[0]
last_char = my_string[-1]

my_string_slice = my_string[:-2]

print(my_string)
print(char)
print(last_char)
print(my_string_slice)

for i in my_string:
    print(i)

if "m" in my_string:
    print("Yes")
else:
    print("No")

print(my_string.find("o"))
print(my_string.count("o"))
print(my_string.index("o"))
print(my_string.replace("Hello", "Hi"))
lists = my_string.split()
print(my_string.split())

new_string = " ".join(lists)
print(new_string)