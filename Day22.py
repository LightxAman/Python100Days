# LIST

# Introduction to Lists in Python
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets[].
# Lists are changeable meaning we can alter them after creation.

# a basic implementation of List
marks = [3, 5, 6, 7, 7, 6, 8, "Light", "Dark"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

# Can have variety of diff data types together.
details = ["Light", 10, "Dark", 6.8, True]
print(details)

# Indexing

# Negative indexing is used to access the items, but from the end of list.
# The last item on the list has index [-1], second last [-2] ,...

print(marks[-3])  # negative indexing
print(marks[len(marks) - 3])  # negative to positive, easier to understand.

# Checking if an item is in list

if 7 in marks:
    print("Yes")
else:
    print("No")

if 65 in marks:
    print("Yes")
else:
    print("No")

if "Light" in marks:
    print("Yes")
else:
    print("No")

# Printing all elements of marks

print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:-4])

# jump index
print(marks[1:4:2])

# List comprehension
print("\n\nList comprehension")

lst = [i for i in range(4)]
print(lst)

lst = [i for i in range(6)]
print(lst)

lst = [i for i in range(40)]
print(lst)

lst = [i for i in range(10) if i % 2 == 0]
print(lst)
