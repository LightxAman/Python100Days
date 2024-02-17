# If-Else conditional statements

a = int(input("Enter your age: "))
print("\nYour age is: ", a)

# Conditional operators
# >, <, >=, <=, ==, !=


print("\n\nExample of if-else ")

print(a > 18)
print(a >= 18)
print(a <= 18)
print(a == 18)
print(a != 18)

if a > 18:
    print("You can drive!")
# This space in line 16 and 19 is called indentation. It signifies that we are still in that block.
else:
    print("You cannot drive!!")

print("\n\nExample of Elif ")

num = 0

if num < 0:
    print("\nNumber is negative")
elif num == 0:
    print("\nNumber is zero")
else:
    print("Number is positive")
