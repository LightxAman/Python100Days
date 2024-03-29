# f-strings in python
# string formatting can be done in python using format method.

# Example
print("Example 1")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498.
# It is aka Literal string Interpolation or more commonly as f-string.
# The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the string itself.

print("\nExample 2: Old ways")
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Light"

print(letter.format(name, country))

print("\nExample 3")
print(f"Hey my name is {name} and I am from {country}")

# f-string is newly introduced 3.6 onwards

print("\nExample 4")
print(f"{2 * 30}")
print(type(f"{2 * 30}"))

print("\nExample 5")

# if we want to retain the raw string without replacing the variables values use double {{
print(f"We use f-strings like this!!,Hey my name is {{name}} and I am from {{country}} ")

# More Examples
print("\nExample 5")
language = "Python"
school = "freeCodeCamp"
print(f"I'm learning {language} from {school}.")

# How to Evaluate Expressions with Python f-Strings
print("\nExample to show how to Evaluate Expressions with Python f-Strings")
num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")

# How to Use Conditionals in Python f-Strings
print("\n How to Use Conditionals in Python f-Strings")
num = 87
print(num)
print(f"Is num even? {True if num % 2 == 0 else False}")

# How to Call Methods with Python f-Strings
print("\nHow to Call Methods with Python f-Strings")
author = "jane smith"
print(f"This is a book by {author}.")

# To print out the author's name formatted in title case
print("\nTo print out the author's name formatted in title case")
author = "jane smith"
a_name = author.title()
print(f"This is a book by {a_name}.")
