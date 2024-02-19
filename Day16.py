# Loops - for and while


# For Loop
# for loops can iterate over a sequence of iterable objects in python.
# Iterating over a sequence is nothing but iterating over stirngs, lists, tuples, sets and dicts.

name = 'Light'
for i in name:
    print(i)
    if i == "g":
        print("This is letter g!")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k + 1)

for k in range(1, 9):
    print(k)

# range(start, stop, step)
# step omits the no of values sequentially according to value of step.
for k in range(1, 12, 2):
    print(k)

# for k in range(1, 20000):
#     print(k)
