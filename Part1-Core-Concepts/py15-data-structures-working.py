# Iterating Python Data Structures

# Working with lists
# Task Review:
# Return total of 1, 2, 3, 4, 5 adding them all together
# total = 1+2+3+4+5
numbers = [1, 2, 3, 4, 5]
total = 0

# 3 different to loop through a collection of values
for number in numbers:
    pass

for number in range(1, 6):  # this will include: 1, 2, 3, 4, 5
    pass

for number in [1, 2, 3, 4, 5]:
    total += number

print(total)

# result
result = 1
for number in numbers:
    result *= number

print(result)


# Working with Dictionary
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

# If we needed access to both, keys, and values,
# we use a dictionary method called .items()
print(user.items())
# dict_items([
# ('username', 'tombombadil'),
# ('first_name', 'Tom'),
# ('last_name', 'Bombadil'),
# ('age', 100)
# ])

# using the normal for loop:
# the variable "item" will only represent the keys of the dictionary "user"
for item in user:
    print(item)  # => only print the keys (not the values)

# output:
# username
# first_name
# last_name
# age

# We are using these two variables:
# key is just a name (it could be x, y, etc...) to represent the keys of our dictionary "user"
# value is just name (it could be x, y, etc...) to represent the values of our dictionary "user"
"""
for key in user:
    print(f"the key: {key}")
    print(f"its value: {value}")
# Error: ValueError: too many values to unpack (expected 2)
"""

# The solution: using the ".items()" method
print("printing keys and values individually")
for key, value in user.items():
    print(f"the key: {key}")
    print(f"its value: {value}")
    print("===================")

print("printing both keys and values as one!")
for key_value in user.items():
    # example ('username', 'tombombadil')
    print(f"the key and its value: {key_value}")
    print("======================================")

# Working With Set
# another example about working with set
# Create a set using the set() function
directions = set(['north', 'south', 'east', 'west'])
print(type(directions))  # <class 'set'>
print(directions)  # {'west', 'north', 'south', 'east'}

# we can create our set using {} directly:
margins = {'top', 'right', 'bottom', 'left'}
print(type(margins))  # <class 'set'>
print(margins)  # {'top', 'right', 'bottom', 'left'}

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)


# List Comprehensions:
numbers = []
for x in range(10):  # looping from 0 to 9
    numbers.append(x)

print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# This same code could be written as a list comprehension.
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nesting loops with lists:
# We need to declare our empty list before staring using it inside our loop
# the same as we did in JS: let my_numbers=[];
combination = []
for x in [1, 2, 3]:  # x=1 and so on
    for y in [3, 1, 4]:  # y=3, y=1, y=4 and so on
        if x != y:
            combination.append((x, y))  # combination[(1,3),(1,4) and so on]

# The code above (two for loops)
# returns [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)] which is a list of tuples.
print(combination)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# This can be done in one line:
combination = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# it was easy to convert the full if block statement into ternary operator!

# More examples from LMS:
# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in range(10)])

# 2. [0, 2, 4, 6, 8, 10]
print([i for i in range(0, 11, 2)])

# 3. [0, 1, 4, 9, 16, 25, 36, 49]
print([x**2 for x in range(0, 8)])

# 4. [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print([((i, (i+1))) for i in range(5)])

# 5. ['woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo']
print(['woohoo' for i in range(7)])

# 6. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
hw = 'hello world'
print([i for i in hw])

# 7. [('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
ab = 'ABCDEF'
print([(ab[i], ab[j]) for i in range(0, 3) for j in range(3, 6)])
