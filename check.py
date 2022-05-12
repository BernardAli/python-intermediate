import sys
import timeit

mylist = list(range(0, 11))
mytuple = tuple(range(0, 11))

print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

print(timeit.timeit(stmt=f"{mylist}", number=10000000))
print(timeit.timeit(stmt=f"{mytuple}", number=10000000))



