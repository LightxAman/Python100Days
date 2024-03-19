# Palindrome Program

str = 'JaVaJ'
strstr = str.casefold()

# This string is reverse.
rev = reversed(str)

if list(str) == list(rev):
    print("PALINDROME !")
else:
    print("NOT PALINDROME !")
