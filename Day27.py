# Tuple Operations/Manipulating tuple
# Tuples are immutable, if you want to add,change tuple items,
# Then you must convert the tuple to a list.
# Then perform operations on that list and convert it back to tuple.

countries = ("Spain", "India", "USA", "England")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
