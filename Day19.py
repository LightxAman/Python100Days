# Do-While loop in python
# do…while is a loo[ in which a set of instructions will execute at least once(irrespective of the conditions)
# and then the repetition of loo['s body  will depend on the condition passed at the end of the while loop.
# It is also known as an exit-control loop

# How to emulate do...While loop in python?
# TO create a do while loop in python, you need to modify the while loop a bit in order to get similar behavior to a
# do while loop

# The most common technique to emulate a do-while loop in python is to use an infinite while loop with a break statement
# wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
