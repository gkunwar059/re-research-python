# Q.N :- mutable the memory location is change and immutable it takes the memory location reference it means ? the location is not changed right ? yes or no ?

"""'

Yes, you are correct!
Immutable objects (e.g., strings, tuples, integers) do not change their memory location when modified because modifications create a new object entirely. The original memory location remains unchanged, and a new location is assigned for the new object.
Mutable objects (e.g., lists, dictionaries) allow modifications in place, meaning the memory location remains the same even after the object's contents are changed.
So, immutable objects do not change the original memory location, while mutable objects allow in-place changes without changing the memory location.

"""

# list
list1 = [1, 2, 3]
print(type(list1))


# function
def func(value):
    X=10
    return X
print(type(func))
