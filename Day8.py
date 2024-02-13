# Type Casting

# Problem
a = "1"
b = "2"
print(
    a + b)  # this will show output as 12 because python is treating 1 and 2 as strings and implicitly converting them.

# TypeCasting : The conversion of one datatype into another type is known as type casting

print(int(a) + int(b))  # typecasting into INT

# Types : Explicit Conversion and Implicit Conversion

print(int(a) + int(b))  # Explicit typecasting into INT

# Implicit Typecasting

c = 1.9
d = 5

print(c + d)  # Python interpreter converts lower datatype into higher datatype automatically
