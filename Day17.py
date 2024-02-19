# Loops - for and while

# While loop
# while loops executes statement while the condition is true,
# as soon as Condition value -> false interpreter come out loop

# for i in range(3):
#     print(i)

# Basic while loop
print("Basic while loop example!")
i = 0

while i < 4:
    print(i)
    i = i + 1

print("Done with the loop")

# a little bit playing around
print("\nplaying around with while loop!")
i = int(input("\nEnter the number: "))
while i < 40:
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")

# Example of else with while loop
print("Else with while loop example!")
count = 5
while count > 0:
    print(count)
    count = count - 1
    # count = count + 1 # Will make an infinite loop due to no terminating condition
else:
    print("I'm inside else")
