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


# Example 3 using for loop
Num = int(input("Enter a value:"))
Temp = num
Rev = 0
while num > 0:
    dig = num % 10
    revrev = rev * 10 + dig
    numnum = num // 10
if temp == rev:
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")
