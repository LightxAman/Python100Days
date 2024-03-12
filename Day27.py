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

# Examples of tuples
languages = ('Python', 'Swift', 'C++')

# access the first item
print(languages[0])  # Python

# access the third item
print(languages[2])  # C++

# Python Tuple Length
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars))

# Iterate Through a Tuple
fruits = ('apple', 'banana', 'orange')

# iterate through the tuple
for fruit in fruits:
    print(fruit)
