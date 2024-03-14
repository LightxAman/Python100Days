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

vegetables = ('carrot', 'Potato', 'Spinnach')

# iterate through the tuple
for vegetables in vegetables:
    print(vegetables)

# Accessing Elements

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[1:3])  # Output: (2, 3)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
