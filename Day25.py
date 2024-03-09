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
