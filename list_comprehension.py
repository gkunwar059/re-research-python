# {expression for item in iterable if condition}


# Example 1
#   1.  - expression operation will be done here      -- just a value

# Example 2
#   1.  - iterable operation will be done here


# Example 3
#   1.  - condition operation will be done here


example_list = {x**2 for x in range(1, 11) if x > 5}
print(example_list)


# exp={#expression}
# condition for the item if


# dict

# key value pair expression hunxa


squarei = {x: x**2 for x in range(1, 11)}
print(squarei)

# 1 square 2 , 3 square 9 etc


# 1. List Comprehensions
# Syntax
# [expression for item in iterable if condition]

# expression: A value or operation applied to each element.

# item: Each element in the iterable.
# iterable: A sequence or collection to iterate over (e.g., list, range, string).
# if condition (optional): A filter to include only elements that meet the condition.
# How it Works
# The iterable is looped through.
# The condition (if provided) is checked for each item.
# The expression is applied to each item that satisfies the condition.
# The resulting values are added to the new list.
# Example
# # List of squares of even numbers from 1 to 10
# result = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(result)  # Output: [4, 16, 36, 64, 100]


# simple  logic of the code

# debugging of the code of the comprehension is difficult as per the simple code and
# the comprehsntion is use when the logic is simple and can easily include in the single line and
# multiple line of the code will not be included into the comprehension this way you can use it ? think wisely and
#  handle the code of condut right ?
