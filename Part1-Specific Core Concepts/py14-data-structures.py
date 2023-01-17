# Collections:
# Lists (Arrays in JS):
# A list is a collection of items or elements that are ordered and is changeable.
# It can contain duplicate items.
# Those items can be of different types such as strings, integers, floats or even another list.
# You can use an index to find an element in the list.
# Lists are zero-indexed, so the first element has index 0.


myList = ['HTML', 200, True, 'HTML']

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# To get/access any value/element/item/ in a list => list_name[index number]

# print the first fruit:
print(fruits[0])  # the current element in index 0 => "apple"

# Get an item located in a list
second_item = fruits[1]  # the second item/element in my list
print(second_item)
print()

# In JavaScript, we used:
# - push() to add item to the array
# - pop() to remove item from the array

# using append() method
# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Using reverse() method
# Reverse the list
fruits.reverse()
print(fruits)
print()

# Sort the list alphabetically: A - Z
fruits.sort()
print(fruits)
print()

# Note:
# In sorting method only => "820" < "97" => True! <=> the same thing we had in J
# So when sorting numbers we have to make sure that both the values and the data types are numeric
my_str_numbers = ["820", "97", "100", "25"]
print(f"my_str_numbers before sorting: {my_str_numbers}")
# my_str_numbers before sorting: ['820', '97', '100', '25']

my_str_numbers.sort()  # suppose to be: 25 then 97 then 100 then 820
print(f"my_str_numbers after sorting: {my_str_numbers}")
# my_str_numbers after sorting: ['100', '25', '820', '97']

my_numbers = []  # similar to JS code => let myNumbers=[];
for element in my_str_numbers:
    my_numbers.append(float(element))

print(f"my_numbers before sorting: {my_numbers}")
# my_numbers before sorting: [100.0, 25.0, 820.0, 97.0]

my_numbers.sort()
print(f"my_numbers after sorting: {my_numbers}")
# my_numbers before sorting: [25.0, 97.0, 100.0, 820.0]

# As a list can contain many data types, not all methods will work on all lists.
# You would not be able to sort the list:
# [ None, 1, 'one', True] as the types of the items are not comparable (different data types).

# *****************
# Review for range:
# *****************
# remember we used this function in for loop
range(1, 10)  # all the numbers from 1 to 9
range(10)  # all the numbers from 0 to 9
range(0, 10, 2)  # all the numbers from 0 to 10 with step 2 (+2) => the even number
# ==================================================================================

# to print from 1 to 10
for num in range(1, 11):
    print(num)


# List Slicing & Indexing
# ***********************
# Sometimes we may only need a subset of a list, instead of a full list!
# So to create a subset of a list, instead of a full list.
# In this case, we would use slice notation to chop up the list

fruits.append("peach")
print(fruits)
# ['apple', 'banana', 'cherries', 'orange', 'pear', 'plum', 'peach']
print(fruits[0])  # apple

# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])  # peach
print(fruits[-2])  # plum


# The slice() function returns a sub-list from the main list
# This slice object can take three arguments:
# slice(start, end, step)
# the arguments are integer values of the starting position, end position and step size.
x = slice(3)
print(fruits[x])  # ['apple', 'banana', 'cherries']

# notice that index 5 will not be included (same as range() function)
x = slice(3, 5)
print(fruits[x])  # ['orange', 'pear']

# starting form index: 1 to index: 6
x = slice(1, 7, 2)
print(fruits[x])  # ['banana', 'orange', 'plum']

# one last example:
my_subjects = ["HTML", "CSS", "Bootstrap", "JavaScript",
               "jQuery", "Python", "Flask", "Databases", "Django"]
x = slice(1, 7, 2)
# 1: will be "CSS"
# 7: the highest index that we can reach is 6
# 2: think about 2 like x +=2 by moving two
print(my_subjects[x])
# ["CSS", "JavaScript", "Python"]

# Combination of indexing and range:
# *********************************
# We indicate the index at which we wish to start.
# Then after the colon (:)
# we use the index at which we want to stop

# Let's try to print: ["HTML", "CSS", "Bootstrap"]
print(my_subjects[0:3])

# Let's try to print: ["HTML", "CSS", "Bootstrap", "JavaScript"]
print(my_subjects[:4])

# Let's try to print: ["Bootstrap", "JavaScript", "jQuery", "Python",]
print(my_subjects[2:6])

# my original list:  ["HTML", "CSS", "Bootstrap", "JavaScript", "jQuery", "Python", "Flask", "Databases", "Django"]
print(my_subjects[0: 7: 2])
# ['HTML', 'Bootstrap', 'jQuery', 'Flask']

# The last item in a list has the index of -1,
# so you can reverse the list using the [::-1] notation.
# You can also use negative values for a start and stop if you want to index from the end of the list.
# list[-1] refers to the last element, list[-2] is the second-last, and so on.

# The "list" methods and descriptions:
# Method	        Description
# list.append(x)	Add an item to the end of the list.
# list.extend(list)	Extend the list by appending another list.
# list.insert(i, x)	Insert an item at a given position. The first argument is the index of the element before which to insert
# list.remove(x)	Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
# list.pop(i)	Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
# list.clear()	Remove all items from the list.
# list.index(x, start, end)	Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
# list.count(x)	Return the number of times x appears in the list.
# list.sort(key=None, reverse=False)	Sort the items of the list in place
# list.reverse()	Reverse the elements of the list in place.
# list.copy()	Return a copy of the list. Equivalent to a[:]

print("Practising more list methods with 'menu' list:")
menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu)  # ['eggs', 'bacon', 'spam', 'spam']

# we have two elements with the value of "spam"
print(menu.count('spam'))  # 2
print(menu.count('eggs'))  # 1
print(menu.index('eggs'))  # 0
print(menu.reverse())  # None
print(menu)  # ['spam', 'spam', 'bacon', 'eggs']
print(menu.append('lobster thermidor'))  # None
print(menu)  # ['spam', 'spam', 'bacon', 'eggs', 'lobster thermidor']
print(menu.sort())  # None
print(menu)  # ['bacon', 'eggs', 'lobster thermidor', 'spam', 'spam']
print(menu.pop())  # spam


print("*********************")
print("Working with Tuples")
# Tuples:
# *******
# Place items inside parentheses and separate with commas
my_modules = ("HTML", "CSS", "Bootstrap", "JavaScript",
              "jQuery", "Python", "Flask", "Databases", "Django")

print(type(my_modules))  # <class 'tuple'>
print(my_modules)
# ('HTML', 'CSS', 'Bootstrap', 'JavaScript', 'jQuery', 'Python', 'Flask', 'Databases', 'Django')

# output: "HTML"
print(my_modules[0])  # Using the list way
# The following code will give an error
# print(my_modules(0))  # TypeError: 'tuple' object is not callable

# Create an empty tuple()
empty_tuple = ()
print(empty_tuple)  # ()

# Create a tuple name "my_tuple" using this way (by skipping the parenthesis):
my_tuple = 12345, 54321, 'hello!', True, False, 56.43
print(type(my_tuple))  # <class 'tuple'>
print(my_tuple)  # (12345, 54321, 'hello!', True, False, 56.43)

print("Unpacking Tuple")
# unpacking tuple into variables:
# x, y, z = my_tuple # ValueError: too many values to unpack (expected 3)

a, b, c, d, e, f = my_tuple
# printing some of them:
print(a)  # 12345
print(d)  # True
print(f)  # 56.43


# More Example:

# Create a tuple variable named cars and pack it with the values of "Tesla", "BMW" and "Ferrari"
cars = "Tesla", "BMW", "Ferrari"
# Or cars = ("Tesla", "BMW", "Ferrari")
print(cars)

# Create a variable named get_car
# use tuple indexing to pull out the "BMW" value from the cars tuple
# using the correct index number.
get_car = cars[1]
print(get_car)

# Unpack the cars tuple and assign its values to variables named: car_one, car_two and car_three
car_one, car_two, car_three = cars
print(car_one)
print(car_two)
print(car_three)


print("*********************")
print("Working with Dictionaries")

# Dictionaries:
# *************
# Provides with a means of storing data in a more meaningful way
# Sometimes we need a more structured way of storing our information
# in a collection. To do this, we use "dictionaries"
# Dictionaries will enable us to use what are called key/value pairs
# A dictionary can be thought of as a mapping between indexes (known as keys) and values.
# Each key must be unique and unchanging as that key maps to a particular value.

"""
In JS we worked with JSON structure:
a JSON object looks like this:

user = {
    "username":"martinsmith",
    "first_name":"Martin",
    "last_name":"Smith",
    "age":47
}


we also learned about a pure JavaScript object
member = {
    username:"martinsmith",
    first_name:"Martin",
    last_name:"Smith",
    age:47
}
"""

# Now in Python, dictionary is like JSON object:
user = {
    "username": "martinsmith",
    "first_name": "Martin",
    "last_name": "Smith",
    "age": 47
}

# We have created a dictionary called "user".
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

# Trying now with the dictionary method "items()"":
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

# More Examples:
# Below, This dictionary has four keys (username, first_name, last_name, and age)
# Each of these keys has a value associated with it ("tombombadil", "Tom", "Bombadil", 100)
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(type(user))  # <class 'dict'>
print(user)
# {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}

# To get the value of a dictionary, you have to use the key
# To print the user's age:
print(user['age'])  # 100

# To print the first name:
print(user['first_name'])  # Tom

# To add a new key with a value,
# you can use the items key in square bracket notation and the assignment operator with a value.
# Add properties/keys to our dictionary on the fly:
user['city'] = 'Toronto'
print(user)
# {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100, 'city': 'Toronto'}

# print(user['gender'])
# KeyError: 'gender'

# We can delete a key and its value from our dictionary using the keyword "del":
# To delete a key/value pair use del and the key
del user['city']

print(user)

# using list() function
# To list the keys in the dictionary, you can use list()
# passing our dictionary as an argument to the list() function will return a list with the keys of the object
temp = list(user)
# or print(list(user))
print(temp)  # ['username', 'first_name', 'last_name', 'age']

# using the function sorted() for our dictionary:
print(sorted(user))
print(user)
# {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}

# if you just want to know if a key exists within the dictionary, use the "in" keyword:
# Below are asking "Python" if we have the key "username" in the dictionary "user"
# the answer will: True if the key is exist or False if it's not
print('username' in user)  # True

print("********************************")
# More about dictionaries:
# Task: Creating a new dictionary named "client" (has the same keys as user)
# creating a list of 4 string elements that will represent the keys of out dictionary:
keys = ['username', 'first_name', 'last_name', 'age']
# creating a variable "default_value" with empty string:
default_value = ''

# creating our dictionary named "client" using dict.fromkeys()
# dict() function => is used to create a dictionary from a list data type
# fromkeys() method => is used to specify the keys list as the keys and a variable of an empty string as the values
client = dict.fromkeys(keys, default_value)
# we have created our dictionary with default values of empty strings:
print(client)
# {'username': '', 'first_name': '', 'last_name': '', 'age': ''}
# Notice we can use the same method to override/clear any dictionary values:
# Below we are targeting our dictionary "user":
user = dict.fromkeys(keys, default_value)
print(user)
# {'username': '', 'first_name': '', 'last_name': '', 'age': ''}

# then assign new values to its keys:
user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)

print("**** Challenge *****")
# Challenge:
# Steps
# 1. Declare a variable named "spaceship" and assign it the value of a dictionary.
# 2. Inside the dictionary, define the following key value pairs:
# 1) key: "name", value: "Red Dwarf",
# 2) key: "type", value: "Mining vessel",
# 3) key: "owner", value: "Jupiter Mining Corporation",
# 4) key: "captain", value: "Frank Hollister"
# 3. print the value of the spaceship object to the terminal

# First Solution*: Based on the above required steps (try it on LMS)

# Second Solution: using dict.fromkeys()
# 1. Create our list of the keys:
spaceship_keys = ["name", "type", "owner", "captain"]

# 2. Create our dictionary named "spaceship" using dict.fromkeys()
spaceship = dict.fromkeys(spaceship_keys)

print(spaceship)
# output: {'name': None, 'type': None, 'owner': None, 'captain': None}


spaceship = dict.fromkeys(spaceship_keys, "Not set yet!")
print(spaceship)
# {'name': 'Not set yet!', 'type': 'Not set yet!', 'owner': 'Not set yet!', 'captain': 'Not set yet!'}

# NOTE: We can't use dict.fromkeys() to assign different values for every individual key!
# the following code will generate this error:
# TypeError: fromkeys expected at most 2 arguments, got 5
# spaceship = dict.fromkeys(spaceship_keys, "Red Dwarf", "Mining vessel", "Jupiter Mining Corporation", "Frank Hollister")


# The only way to assign a value for each key:
spaceship["name"] = "Red Dwarf"
spaceship["type"] = "Mining vessel"
spaceship["owner"] = "Jupiter Mining Corporation"
spaceship["captain"] = "Frank Hollister"
print(spaceship)

# Creating a "list" (Array) out of the dictionary keys:
my_key_list = list(spaceship.keys())
print(type(my_key_list))  # <class 'list'>
print(my_key_list)  # ['name', 'type', 'owner', 'captain']

# Creating a "list" (Array) out of the dictionary values:
my_value_list = list(spaceship.values())
print(type(my_value_list))  # <class 'list'> # object (Array) in JavaScript
print(my_value_list)
# ['Red Dwarf', 'Mining vessel', 'Jupiter Mining Corporation', 'Frank Hollister']

print("The \"dictionary\" methods")
# The "dictionary" methods and descriptions:
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a new dictionary with the specified keys and value

# get(keyname, value)	Returns the value of the specified keyname. Used in the previous unit.
# Returns default None if the keyname doesn't exist unless you override this default with a optional value.

# items()	Returns a list containing a tuple for each key:value pair
# keys()	Returns a list containing the dictionary's keys. Used in the previous unit.
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key:value pair

# setdefault()	Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value

# update()	Updates the dictionary with the specified key:value pairs
# values()	Returns a list of all the values in the dictionary. Used in the previous unit.

# using items()
print(user.items())
# the output:
"""
dict_items([
('username', 'tombombadil'), 
('first_name', 'Tom'), 
('last_name', 'Bombadil'), 
('age', 100)
])
"""

# using update()
user.update({'city': 'Toronto'})  # ' or "
print(user)
# {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100, 'city': 'Toronto'}

# using popitem() => removes the last one
user.popitem()
print(user)
# or just all in one step => print(user.popitem())
# {'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}


# using get(keyname, value)
print(user.get('age', 0))  # 100
# 0 is the fallback option (the default value) if the key "age" is not exist

# Or using:
user_age = user.get('age')
print(user_age)  # 100

# We are asking for a value of key that doesn't exit!
user_email = user.get('email')
# if the key is not exits, Python will return the keyword "None"
print(user_email)  # None

# Or having a default value
user_address = user.get("address", "Sorry, Invalid Key Request!")
print(user_address)  # Sorry, Invalid Key Request!

# using clear()
user.clear()
print(user)  # {}

# Challenge:
# Steps
# 1. Use the update() method to add a new key-value pair to the challenger dictionary. The key is "occupation" and the value is "Hunter"
# 2. Use the get() method to get the value stored at the "occupation" key in the challenger dictionary, and assign the value to a variable named occupation
# 3. Add a print statement to print the value of the occupation variable to the terminal.
# 4. Use the update() method to update the value stored at the "age" key to 17
# 5. Use the pop() method to remove the key-value pair for "status" from the challenger dictionary.
challenger = {
    "name": "Katniss Everdeen",
    "age": 16,
    "district": 12,
    "weapon": "Bow and Arrow",
    "status": "Victor"
}
# add your code here

print(challenger)

# *************************************************************************
# Sets: An unordered collection with no duplicates
# uses curly brackets, but commas separate items in the collection.

# we have added multiple identical items to the set "spam"
breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}

print(type(breakfast))  # <class 'set'>
# when we print the set, the duplicates have been removed
print(breakfast)  # {'bacon', 'egg', 'spam'}

for item in breakfast:  # loop 3 times only
    print(item)

# using the same keyword "in" to check if we have this value or not:
print('egg' in breakfast)  # True

# using add() method
breakfast.add('sausage')
print(breakfast)  # {'sausage', 'spam', 'bacon', 'egg'}

# using add() method again
breakfast.add('bread')
print(breakfast)  # {'bread', 'sausage', 'spam', 'bacon', 'egg'}

# using update() method
breakfast.update(['Lobster Thermidor', 'truffle pate',
                 'crevettes', 'shallots', 'aubergines'])
print(breakfast)
# {'shallots', 'egg', 'spam', 'Lobster Thermidor', 'truffle pate', 'bacon', 'crevettes', 'aubergines'}

# using discard() method
# breakfast.discard() # TypeError: set.discard() takes exactly one argument (0 given)

# We have to specify the name of the item that we want to remove from our set values
breakfast.discard('crevettes')
print(breakfast)
# {'bread', 'truffle pate', 'Lobster Thermidor', 'sausage', 'bacon', 'aubergines', 'shallots', 'egg', 'spam'}

# Below "tea" is not exist, python will just ignore the command without any errors!
breakfast.discard('tea')

# Check the following Code:
print("**** Working with Set() Function ****")
hello = set("Hello")
world = set("World")

print(f"The unique letters in hello are: {hello}")
# | is the symbol for union
print(f"The letters in hello or world or both are: {hello|world}")

# & is the symbol for intersection
print(f"The letters in both hello and world are: {hello&world}")

# - is the symbol for difference
print(f"The letters in hello but not world are: {hello-world}")

# ^ is the symbol for symmetric difference
print(f"The letters in hello and world but not both are: {hello^world}")

# Challenge

product_list = ['hammer', 'saw', 'nails', 'wood',
                'screws', 'paint', 'brushes', 'light bulbs']
products_bought = {'nails', 'screws', 'hammer', 'wood', 'saw',
                   'hammer', 'saw', 'nails', 'nails', 'screws', 'hammer'}

# Steps:
# 1. Use the add() method to add the string "light bulbs" to the products_bought set
# 2. use the update() method to add a list of three more products that have been bought ['wood', 'screws', 'saw'] to the products_bought set.
# 3. Create a variable has_nails and assign it an expression that checks if "nails" is in the products_bought set.
# 4. Create a variable has_paint and assign it an expression that checks if "paint" is in the products_bought set.
# 5. Create a variable named unsold_items. Assign it an expression that finds the difference between product_list and products_bought using the difference operator. You will need to convert product_list to a set within the expression
# 6. Print out the variable: has_nails
# 7. Print out the variable: has_paint
# 8. Print out the variable: unsold_items

# add your code here
