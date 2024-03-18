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


# Python Comments vs Docstrings

# Python comments
# They are descriptions that help programmers better understand the intent & functionality of code.
# They are completely ignored by the python interpreter.

# Python docstrings
# As mentioned at the start, Python docstrings are strings used right after the definition of a f(), classs, module.
# we can access these docstrings using the doc attribute.

def my_function():
    """ ' 'Demonstrates triple double quotes docstrings and does nothing really' ' """

    return None


print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)


def multiply_numbers(a, b):
    """
	Multiplies two numbers and returns the result.

	Args:
		a (int): The first number.
		b (int): The second number.

	Returns:
		int: The product of a and b.
	"""
    return a * b


print(multiply_numbers(3, 5))
