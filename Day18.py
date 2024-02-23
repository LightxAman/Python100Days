# Break and Continue statements

# Break statement
# It enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within

# Example:
print("Basic example for Break Statement: ")
for i in range(12):
    if i == 10:
        break
    print("5 X ", i + 1, "=", 5 * (i + 1))

print("Outside of LOOP!")

# Continue Statement
# The continue statement skips the rest of the loop statement and causes the next iteration ro occur

print("Basic example for continue statement: ")
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 X ", i, "=", 5 * i)
