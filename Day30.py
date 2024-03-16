# Docstrings in Python
# docstrings are the string literals that appear right agter the definition of a fuction,
# method, class, or module

def square(n):
    """Takes in a number n, returns the
    square of n"""
    print(n ** 2)


square(5)
# To see the docstring.
print(square.__doc__)
