# Strings
# Anything enclosed within " " or ' ' is a string
# A string is essentially a sequence of array of textual data.
# Strings are used when working with unicode characters

name = "Light"
print("Hello," + name)

# Multiline Strings by """ """ or ''' '''

a = """Hello! How are you,
I hope you are well and learning!"""
print(a)

# Accessing Characters of a string
# In python, string is like an array of characters.We can access parts of string by using its index which starts form 0.
# Square brackets can be used to access elements of the string.


# name  =  Light
# index =  01234

print(name[0])
print(name[2])
# print(name[5]) # Will throw an index error

# Looping through the string

for character in name:
    print(character)
