# Title : Datatypes, A basic overview

# What is variable?
# A variable is like a container that holds the data.

a = 1  # Integer datatype
print(a)

b = "Light"  # String datatype
print(b)

c = True  # Boolean datatype
print(c)

d = None  # None-type datatype
print(d)

# print(a + b)
# This will throw an error since one variable is int and other string

# type() function tells us about the variable datatype
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))

# Builtin datatypes in python
# 1) Numeric - INT, Float, Complex

# Int Datatype
N1 = 5
print(N1, ", The type: ", type(N1))

# Float Datatype
N2 = 6.9
print(N2, ", The type: ", type(N2))

# Complex Datatype
N3 = complex(6, 9)
print(N3, ", The type: ", type(N3))

# Text Datatype - String
S1 = "Light"
print(S1, ",The type: ", type(S1))

S2 = "Light is a good boi"
print(S2, ",The type: ", type(S2))

# Boolean Datatype
B1 = True
B2 = False
print(B1, "&", B2, ", The types: ", type(B1), "&", type(B2))

# Sequenced Datatype - List and Tuple

# List datatype
# simply list is collection of different datatype and are mutable or changeable
list1 = [8, 2, 4, [-4, 5], ["Light", "Dark"]]
print(list1, ", The type: ", type(list1))

# Tuple datatype
# Same a list but these are immutable
tuple1 = (("Light", "Dark"), ("Code", "Coding"))
print(tuple1, ", The Type: ", type(tuple1))

# Mapped Datatype - dict
# dict - a dictionary is an unordered collection of data containing a key:value pair.
# The key:value pairs are enclosed within curly{} brackets

dict1 = {"name": "Light", "age": 20, "canVote": True}
print(dict1, ", The type: ", type(dict1))

# Interesting fact : Everything in python is an 'Object'
