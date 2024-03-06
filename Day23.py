# Python Practice examples on functions

# Example 1 :defining a function to calculate LCM
def calculate_lcm(x, y):
    # selecting the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


# taking input from users
print("Example 1: defining a function to calculate LCM")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The L.C.M. of", num1, "and", num2, "is", calculate_lcm(num1, num2))


# Example 2: defining a function to calculate HCF
def calculate_hcf(x, y):
    # selecting the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


# taking input from users
print("\nExample 2: defining a function to calculate HCF")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The H.C.F. of", num1, "and", num2, "is", calculate_hcf(num1, num2))

# Example 3: defining a function to import and use the calendar module
import calendar

# ask of month and year
print("\nExample 3: Defining the function for a calender")
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy, mm))


# Example 4: defining a function to calculate Volume of cuboid
def volume_of_cuboid(length, breadth, height):
    return length * breadth * height


nu1 = int(input("Enter first number: "))
nu2 = int(input("Enter second number: "))
nu3 = int(input("Enter second number: "))

print("The Volume of cuboid of L, B, H :", nu1, ",", nu2, " and ", nu3, "is", volume_of_cuboid(nu1, nu2, nu3))
