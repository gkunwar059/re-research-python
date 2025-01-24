# Multiple Exception


# if you dont know which one to use please use the except Exception as e: and raise the e it will print the error message


# def divide(a, b):
#     try:
#         return a / b
#     except Exception:
#         raise ZeroDivisionError( "Cannot divide by zero.")

# result = divide(10, 0)
# print(result)



def fetch_data(data, key):
    try:
        return data[key]
    except KeyError:
        return f"Key '{key}' not found."

data = {"name": "Alice"}
print(fetch_data(data, "age"))  # Output: Key 'age' not found.
