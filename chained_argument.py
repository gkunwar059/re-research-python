a=b=c=5
print(c)
print(a)
print(b)


#mutable object like the list dict must be avoide the chaining argument


a = b = []  # Both `a` and `b` now reference the same list
a.append(1)
print(b)  # Output: [1], because `a` and `b` are the same list
print(a)

# chained operator chai use garna chai mutable object ma chai [] yesari sign garerako hunxa 