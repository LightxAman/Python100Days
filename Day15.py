# Match CASE statement
# To implement Switch-case like characteristics very similar to if-else functionality, we use Match case

# A Match statement will compare a given variable's value to different shapes, aka patters.
# The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

# The match case consists of three main entities:

# The Match keyword
# One or more case clauses
# Expression for each case

x = int(input("Enter the value of x: "))  # x is the variable to match

match x:
    case 0:
        print("X is Zero")

    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")

    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")

    # default case (will only be matched if the above case were not matched)
    # so it is basically just and else:
    case _:
        print(x)
