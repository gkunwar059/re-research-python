# is instancce is used to check if an object is an instance of a class
"""is_instance() this func will return True if the object is an instance of the class, otherwise it will return False."""

""""
examples:
"""


# class TestObj:
#     name = "ganesh"


# obj = TestObj()
# print(obj.name)
# print(
#     isinstance(obj, TestObj)
# )   baneko object chai class ko ho ke haina if xa vane chai true otherwise false return gareko

#Mutable vs. Immutable Objects

# immutable: it will location change hunxa , new location create hunxa (id()) id()location sadhai same hunxa 
# mutable: it will location change hunxa , new location  create hhudaina(id()) tara teslai modify garna sakinna


# immutable :int ,str,float,bool,tuple

#mutable: list,dict,set,byte,array,user-defined class

# Is it the same object?

# jasko modify garda location change hunxa , new location create hunxa

# jasko modify garda location change hudaina chai , immutable location create hunxa


# is  helps to check the yehi object ho ke na vanera 


# a=[1,2,3]
# b=[1,2,4]
# print(a)
# print(b)

# a=b
# print(a)
# print(a is b)


# c=[1,2,9]
# print(a is c)



#check the mutablity and the immutablity of python


# a=89
# print(id(a))
# a=89+1
# print(id(a))


#for immmutablity 
# L=[1,2,3]
# print(id(L))       #append last ma element jogdxa so new location create hudaina
# L.extend[4]
# print(L)
# print(id(L))


# a=[1,2,3]
# print(a)
# print(id(a))
# a.append([1,2,3,4,5])
# print(a)
# print(id(a))

# a.extend([1,2,3,4,9])
# print(a)
# print(id(a))



#tricky example


y=10
x=y
print(y)
print(x)

x=20
print(x)
print(y)

