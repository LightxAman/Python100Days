# Palindrome Program

# Example 1

str = 'JaVaJ'
strstr = str.casefold()

# This string is reverse.
rev = reversed(str)

if list(str) == list(rev):
    print("PALINDROME !")
else:
    print("NOT PALINDROME !")

# Example 2

string = input("Enter a letter:")
if string == string[::-1]:
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")
