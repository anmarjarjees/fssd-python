# To Review, in JavaScript we covered the "Primitive JavaScript Data Types"
# Two types of "Primitive Data Types":
# 1) Definitive types:
# - Strings
# - Numbers
# - Boolean: true/false
# 2)  Not Definitive Types: to represent data that has no definitive type, like:
# - a variable with no value
# - an empty value in a database that is not necessarily an empty string
# for these types we have:
# - "None" in Python and ("null" and "undefined") in JavaScript

# For more very intensive explanation From MDN website about JavaScript:
# Primitive => # In JavaScript, a primitive (primitive value, primitive data type)
# is data that is not an object and has no methods.
# Six Data Types that are primitives, checked by typeof operator:
# undefined : typeof instance === "undefined"
# Boolean : typeof instance === "boolean"
# Number : typeof instance === "number"
# String : typeof instance === "string"
# BigInt : typeof instance === "bigint"
# Symbol : typeof instance === "symbol"
# The latest ECMAScript standard defines nine types:
# MDN Link:
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#data_and_structure_types

# Python Data Types:
# ******************
# The most basic data types in computing are:
# - Boolean (bool) which has two built-in values of "True" or "False"
# - Text has the type of string (str)
# - There are several numeric types such as integer (int), float and complex numbers
# numbers: int and float
# int => whole number (no decimal points)
# float => decimal numbers (fractions)

# You can save a sequence of numbers in a list, type, or range
# You can also map data using the dictionary (dict) type.
# This is analogous to an English dictionary
# where you can look up a word and get a derivation


# Define a variable, my_string, here, then print it.
my_string = "Without hard work, nothing grows but weeds."
# Print its type on a separate line
print(my_string)


# string: "ABC" or "123" or 'XYZ' or '456'
# numbers: Int (whole number) or float (with decimals)
# boolean: True of False
# In JavaScript, we used typeof() => return the data type of the variable
# Example: console.log(typeof(my_string)); # in JS
# Python is a strong OOP languages: Classes and objects
# In JavaScript, we used a Constructor Function to represent a class structure
# While in Python we use the word "class" to create a class structure [for later :-)]

# in Py => type() => return the data type of the variable
print(type(my_string))  # <class 'str'>

# There are three distinct numeric types in Math:
# - integers
# - floating-point numbers
# - complex numbers

# In our code we use these two:
# - integer (whole number)
# - floating-point number or float (a number that is followed by a decimal point)

# Good To Know :-)
# The reason that we need to differentiate between the two different types of numbers
# is so that Python can inform the computer of how much memory will need
# to be allocated to store that value because it requires more memory than floats

num = 7.8
print(type(num))  # <class 'float'>

max = 100
print(type(max))  # <class 'int'>

# For example, if you wanted to declare an int in C or Java
# you would write something like this: int my_number = 42;
# We don’t need to do this in Python!
# The reason for this is that Python is what we call a "dynamically typed language"

# in JavaScript
# var isItRight = true; # in JS


# Boolean in Py:
is_it_right = True
print(type(is_it_right))  # <class 'bool'>

# Just quick topic:
# using input() function to get input from the user:
# in Python version 2.x.x: raw_input()
# with version 3: 'raw_input' is not defined
# in Python version 3.x.x: input()
# Quick Example:
user_value = input("Enter any value you want: ")

# remember our first code of getting user's input in JS:
# let userValue = prompt("Enter any value you want: ");
# the same as JS => prompt() function returns a string data type
# in Py => input() function returns a string data type
print("The data type of your input value is:", type(user_value))

# More Examples:
print("=========== More Examples ===========")
print(type("Hello, World!"))  # <class 'str' >
print(type(42))  # <class 'int' >
print(type(3.145))  # <class 'float' >
print(type(1j))  # <class 'complex' >

# ["egg", "bacon", "spam"] => a list (array in JavaScript)
print(type(["egg", "bacon", "spam"]))  # <class 'list' >

# ("egg", "bacon", "spam") => tuple
print(type(("egg", "bacon", "spam")))  # <class 'tuple' >

print(type(range(6)))  # <class 'range' >

# {"name": "John", "age": 80} => a dictionary (Similar to JS object or JSON object!)
print(type({"name": "John", "age": 80}))  # <class 'dict' >

# {"egg", "bacon", "spam"} => set
print(type({"egg", "bacon", "spam"}))  # <class 'set' >
print(type(True))  # <class 'bool' >

# if you want to run a check on the type,
# you can use isinstance() which will return True or False.
# In the example below:
# both my_var and 2 are integers so type() will return <class 'int'> and isinstance() will return True.
my_var = 2
type(my_var)
type(2)
isinstance(my_var, int)
print(isinstance(my_var, int))  # True
print(isinstance(3.14, int))  # False


# Task:
# you have these variables:
itm_one = 10
itm_two = 21.56
itm_three = 'A string of text'
itm_four = True

# print the type of the variable itm_one
# print the type of the variable itm_two
# print the type of the variable itm_three
# print the type of the variable itm_four
# HINT: in Python we can check the type of our data by using the type() method

print('Using "None": ')
# The "None"
# ***********
# None signifies when there is no value given for something in Python
# You might declare a variable at the top of a file/function
# but not have a value to assign to it at that moment
# Examples:
age = None
total = None
age = 20
print(age)  # -> 20
print(total)  # -> None
