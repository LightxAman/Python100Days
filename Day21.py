# Function Arguments and return statement

# There are four types of arguments that we can provide in a function
# Default Arguments
# Keyword Arguments
# Variable length arguments
# Required Arguments

# Default Arguments
def average(a=10, b=1):
    print("The average is :", (a + b) / 2)


print("Arguments passed")
average(4, 6)

print("only one Arguments passed")
average(6)

# Keyword Arguments
print("no order req Arguments passed")
average(b=10, a=12)


# Required Arguments
def average1(a, b, c=10):
    print("The average is :", (a + b + c) / 2)


print("\nRequired Arguments passed")
average1(b=10, a=12)


# Variable length arguments Examples

def average2(*numbers):  # Tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))


print("\nVariable length argumments ")
average2(5, 6, 7, 7)


def name(**name):  # Dictionary
def name(**name):  # Dictionary
    print("Hello", name["fname"], name["mname"], name["lname"])


name(mname="X", lname="Dark", fname="Light")
