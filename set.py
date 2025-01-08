import sys
#concept of the set and the concept reated to the set 

#{} or set()--- Duplicate elements are not allowed    famous of the set is this  order is not preserved

# a={1,2,3,4,5}
# print(type(a))


# mutablity of the set   ---mutable hunxa

my_set={1,2,3,4,5}
my_set.add(6)
print(my_set)

# 3. Memory Usage of Sets
my_set={1,2,3,4,5}
print(sys.getsizeof(my_set))

print( 3 in my_set)    #hash table table



