# Recursion in Python

# Recursion is the process of defining something in terms of itself
# A physical world example would be to place two parallel mirrors facing each other.
# Any object in between them would be reflecting recursively.

# Python recursive function

# Example 1 : Factorial
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
