# List Methods

# list.sort()
# This method sorts the list in ascending order. The original list is updated.

print("Example 1: List.sort()")
l = [1, 24, 34, 25, 65, 9]
print("The current list: ")
print(l)

print("The list after sorting: ")
l.sort()
print(l)

print("The list in descending order: ")
l.sort(reverse=True)
print(l)

# Append : Adding an element at the back of a list
print("Example 2: List.append()")
l1 = [1, 4, 2, 5, 7, 3, 8]
print("The list is: \n", l1)

print("Adding an element at the end of list: ")
l1.append(10)
print(l1)

# Reverse
print("Example 3: List.reverse()")
print("The list is: \n", l)
l.reverse()
print("The reversed list is: \n", l)

# index
print("\nExample 2: List.index()")
# This method returns the index of the first occurrence of the list item
print("The list is : \n", l)
print(l.index(65))
