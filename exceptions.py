# Exceptions

# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.


# Example 1
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:   # Triggered when dividing by zero(0)
    print("Divided by zero")
# Triggered when a value of an inappropriate type | when a value of the correct type, but with an inappropriate value.
except (ValueError, TypeError):
    print("Error occurred")


# Example 2
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:  # To ensure some code runs no matter what errors occur, you can use a finally statement.
    print("This code will run no matter what")


# Example 3
print(1)
raise ValueError  # raise can also be used to raise exceptions
print(2)


# Example 4
name = "123"
raise NameError("Invalid name!")  # exception raised with details


# Example 5
# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
try:
    num = 5 / 0
except:
    print("An error occurred")
    raise
