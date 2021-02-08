# Dictionaries
# Provides with a means of storing data in a more meaningful way
# Sometimes we need a more structured way of storing our information
# in a collection. To do this, we use dictionaries

"""
In JS we worked with JSON structure:
JSON object
user = {
    "username":"martinsmith",
    "first_name":"Martin",
    "last_name":"Smith",
    "age":47
}

we also learned about a pure SJ object
member = {
    username:"martinsmith",
    first_name:"Martin",
    last_name:"Smith",
    age:47
}
"""

# Now in Python (is like JSON object):
user = {
    "username": "martinsmith",
    "first_name": "Martin",
    "last_name": "Smith",
    "age": 47
}

# We have created a dictionary called user.
# This dictionary has four keys (username, first_name, last_name, and age).
# Each of these keys has a value associated with it
# ("martinsmith", "Martin", "Smith", 47).

print(user)
# output: {'username': 'martinsmith', 'first_name': 'Martin', 'last_name': 'Smith', 'age': 47}

# If we wish to access the values contained within the dictionary,
# we use a similar syntax to indexing in lists and tuples:

# example: output just the first name of the user dictionary:
print(user["first_name"])

# Task: print: The username is: martinsmith
print(f"The username is: {user['username']}")  # The username is: martinsmith

# the same loop for list we can use with dictionary
# The following loop will print the keys of the dictionary
for item in user:
    print(item)

# the above loop output will only print the keys:
"""
username
first_name
last_name
age
"""

# What if we want the values associated with each of those keys?
# Then we’d simply use the square brackets like before:
# Hint user["first_name"] => to get the value of the first_name key
for item in user:
    # printing each value associated with its key which is in this loop will be the item
    print(user[item])

# the above loop output will only print the values of each key:
"""
martinsmith
Martin
Smith
47
"""

# the method items()
# If we needed access to both, keys, and values,
# we’d have to use a dictionary method called .items().
print("------ Printing Keys and Values -------")

# Trying without items() first:
for item in user:
    print(f"Key: {item}")
    print(f"Value: {user[item]}")

# the above loop output will only print the keys and values of each key:
"""
Key: username
Value: martinsmith
Key: first_name
Value: Martin
Key: last_name
Value: Smith
Key: age
Value: 47
"""

# Trying now with items():
for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")

# These variables don’t need to be called "key" and "value",
# but as the first variable will be the key and the second variable will the value,
# it’s considered to be a good convention.

# the example is technically working fine, but it's confusing regarding the names:
# like what's x and y ?!
for x, y in user.items():
    print(f"x: {x}")
    print(f"y: {y}")
    print("------------------")
