# Taking User input

# Syntax : variable = input()

# A basic example
a = input("Enter your name: ")
print("My name is", a)

x = input("\n\nEnter first number: ")  # eg x = 100
y = input("\nEnter Second number: ")  # eg y = 12
print(x + y)  # this will show output as 10012

# This is because by default the value which we are giving is number but python input() is not smart enough by default
# it wll take that as a string, hence concatenating them.

print(int(x) + int(y))  # This will now perform Addition operation, since it is now type-casted
