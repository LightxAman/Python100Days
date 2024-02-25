# Functions
# A function is a block of code that performs a specific task whenever it is called.
# In bigger programs, where we have large amount of code, it is advisable to create or use existing functions that make
# program flow organized and neat.

# There are two types of functions:
# 1) Built-in function.
# 2) User-defined functions

# Built inn functions:
# These functions are defined and pre-coded in python.
# eg - min(), max(), sum(), type(), range(), print()

print("Basic example: ")

a = 9
b = 8
gmean1 = (a * b) / (a + b)
print("\nGmean1 = ", gmean1)

c = 8
d = 7
gmean2 = (c * d) / (c + d)
print("\nGmean2 = ", gmean2)


# User-defined functions:
# we can create functions to perform specific tasks as per our needs.
# Syntax:
# def <function_name(parameters)>:
# function body


def calGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


# now we can do:
print("\nUsing functions: ")

calGmean(a, b)
calGmean(c, d)


# Now no need to repeat same lines of code

def isGreater(a, b):
    if a > b:
        print("A is greater!")
    else:
        print("B is greater!")


isGreater(a, b)


# what if we wish to define the function at a later time

def isLesser(a, b):
    pass
# here pass keyword is used else it will throw error.

# Thanks ^-^
