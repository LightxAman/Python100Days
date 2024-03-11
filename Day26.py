# Tuples
# Tuples are ordered collections of data item.
# They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets().
# Tuples are unchangeable meaning we can not alter them after creation.

tup = (1, 5, 6, 6, 7, 8, 9, True)
print(type(tup), tup)

# Here python confuses and takes this as an int.
tup1 = (1)
print(type(tup1), tup1)

# So to solve this issue we add comma

tup2 = (1,)
print(type(tup2), tup2)

# Slicing
tup3 = tup[1:4]
print(tup3)

if 8 in tup:
    print("Yes, It exists!")
