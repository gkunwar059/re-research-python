""" "
* O(1):
    - constant time

    Each of the time algorithms process each element like loop it will check every element and will take time to get the value ?
    when i have to get the value of the 100th postiion it will filter from the  1 to 100th and will take time to get the value
    so this process will take extra time then other
"""

# EXAMPLE:
"""
1. yesle sabai kura scan garnu parne vayeko vayera chai yesle dherai nai time lagaunxa 
O(n)  ----> nth time lagaunxa yesle vanna khojeko ho 
2. Slow for the larger data and it will be depends upon the size of the input data

tara implementation ma depend garxa hai 
"""


def print_atrr(att):
    for i in att:
        print(i)


print_atrr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


"""
O(1):
jati nai thulo 5 or 5 million of data ma 1 time lagaunxa
like jun access garnu parne xa tehi access garxa , implmentation will be different as the searches

1. fast hunxa , list or indexing  for the larger project
2, indexing or the bool flag use hunxa 
"""


# Imagine you have a list of phone numbers, and you always look for the first number.
# It doesn’t matter if the list has 10 numbers or 1,000 numbers—it takes the same time to grab the first number.


"""
When to implement the this two topics depends on the project
1. O(n)--->  Used for operations that depend on the input size (e.g., searching, iterating).
2. O(1): Used for operations that are constant-time (e.g., direct access, fixed-step logic).


"""


