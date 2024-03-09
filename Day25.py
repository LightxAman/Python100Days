# List Methods

# list.sort()
# This method sorts the list in ascending order. The original list is updated.

print("\nExample 1: List.sort()")
l = [1, 24, 34, 25, 65, 9]
print("The current list: ")
print(l)

print("The list after sorting: ")
l.sort()
print(l)

print("\nThe list in descending order: ")
l.sort(reverse=True)
print(l)

# Append : Adding an element at the back of a list
print("\nExample 2: List.append()")
l1 = [1, 4, 2, 5, 7, 3, 8]
print("The list is: \n", l1)

print("Adding an element at the end of list: ")
l1.append(10)
print(l1)

# Reverse
print("\nExample 3: List.reverse()")
print("The list is: \n", l)
l.reverse()
print("The reversed list is: \n", l)

# index
print("\nExample 4: List.index()")
# This method returns the index of the first occurrence of the list item
print("The list is : \n", l)
print(l.index(65))

# Count
print("\nExample 5: List.count()")
# Returns the count of the no. of with the given value.
print(l.count(65))

# Copy
# Returns copy of the list.
# This can be done to perform operations on the list without modifying the original list
print("\nExample 6: List.copy()")

m = l
m[0] = 0
print(l)

# This changes the original list, since m is a reference of l.

# so instead do this

m = l.copy()
m[0] = 0
print(l)

# Insert
print("\nExample 7: List.insert()")
print(l)
l.insert(1, 77)
print(l)

# Extend

print("\nExample 8: List.extend()")
m = [900, 100, 200]
l.extend(m)
print(l)

# Concatenate two list
print("\nExample 9: List concatenate")
k = l + m
print(k)
