# f-strings
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
