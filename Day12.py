# String methods

a = "!! Light!! !!"
print(len(a))

# Upper() and Lower()
# string are immutable, however we create a new copy of string to make changes

print("\nUpper() and Lower() example: ")

print(a.upper())
print(a.lower())

# rstrip()
# Removes any trailing characters

print("\nrstrip() example: ")

print(a.rstrip("!"))

# replace()
# Replaces all occurrences of a string with another string

print("\nreplace() example: ")

print(a.replace("Light", "Dark"))

# Split()
# Splits the given string at the specified instances and returns the seprarated strings as "list" items

print("\nSplit() example: ")

print(a.split(" "))

# Capitalize()
# turns only the first character of the string to uppercase and the rest other characters of string are turned to lowercase.
# The string has no effect if the first character is already uppercase

print("\nCapitalize() example: ")

b = "introduction to python"

c = "\ninTroducTion to pytTon"

print(b.capitalize())
print(c.capitalize())

# center()
# aligns the string to the center as per parameters
print("\ncenter() example: ")

print(b.center(50))
print(len(b.center(50)))
print(len(b.center(1)))

# Count()

print("\nCount() example: ")

d = "Dark"

print(d.count("\nDark"))

# Endswith()
print("\nEndswith() example: ")

print(a.endswith("!!"))

print(a.endswith("ht", 4, 7))

# find()
# searches for the first occurrence of the given value and returns the index where it is present.
# If the given value is absent form the string then return  -1

print("\nFind() example: ")

print(b.find("to"))

# Index()
# It searches for the first occurrence of the given value and return the index where it is present.
# if given value is absent form the string then raise an exception.
print("\nIndex() example: ")
print(b.index("to"))
# print(b.index("Myy"))

# isalnum()
# returns True only if the entire string only consists of A-Z, a-z,0-9,
# If any other character or punctuation are present, then it returns false.
print("\nisalnum() example: ")

e = "WelcomeToPython"
f = "WelcomeTo100DaysOfPython"

print(e)

print(e.isalnum())

print(f)
print(f.isalnum())

# isalpha()
# A-Z and a-z
print("\nisalpha() example: ")

print(f)
print(f.isalpha())
