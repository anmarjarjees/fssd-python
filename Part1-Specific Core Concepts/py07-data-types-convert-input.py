# ===============================================================
# Converting Between Data Types
# By using built-in Python functions
# Some of the more common type conversions are in the table below.

# Function	        What it converts
# ==================================
# int()	        Converts a float or string to an integer
# float()	        Converts an int or string to a floating-point number
# str()	        Converts an int or float to a string
# hex()	        Converts a number to a hexadecimal string
# oct()	        Converts a number to a octal string
# tuple()	        Converts to a tuple
# set()	        Converts to a set
# list()	        Converts to a list
# dict()	        Converts a tuple into a dictionary


# input() function:
# *****************
# We can take input from a user using the input() function using the VS code terminal window
# Graphical User Interface (GUI).
# GUI Examples:
# Applications from our Desktop,
# Opening folders from My Computer,
# Creating Documents in Microsoft Office,
# and browsing the web with Chrome or Firefox
# Command Line Interface or CLI. This interface is text-based,

# Trying these examples:
num1 = 7
num2 = 3
print(num1 + num2)  # 10

num1 = "7"
num2 = "3"
print(num1 + num2)  # 73

num1 = "7"
num2 = 3
# The code below will generate an error:
# print(num1 + num2)
# TypeError: can only concatenate str (not "int") to str

# Conclusion:
# ***********
# Python is a strongly typed language.
# Therefore if we wanted to concatenate an int to a string,
# we wouldn’t be able to do so.
# In a language like JavaScript, which is a weakly typed language,
# we would be able to concatenate a number to a string.
# ===================================================================

# input() function:
# to ask the user to input his/her data

# In JS we used prompt() method (function) of the browser to ask the user to enter their data
# In Js prompt() method returns a string value:
# if the use enters 25 as number it will be "25"
# In JS we used parseInt() and parseFloat() and Number()
# In Js we had to do the following:
# var userNum = parseFloat(prompt("Enter any any number: "));

# in Py we have int() and float()
# in Python, input() function also return a string value even if the user enters/types a number

# Trying this:
first_number = input("Input your first number:")
second_number = input("Input your second number:")

# input() function return a string
# so like JavaScript,
# Python also uses the addition operator + to concatenate or add strings together
print(first_number + second_number)

# Another Example:
my_number = 5
my_string = "5"

## print(my_string + my_number)
# TypeError: can only concatenate str (not "int") to str

# Task#1:
# ask the user to input his name
# we know that input() function returns a string data type (like prompt function in JS)
# The data type of the value that is received/returned from an input() is a string
user_name = input("What's your name? ")

# Problem:
# Asking the user to input their age
# To calculate how many days they lived so far
# how many days this user have been alive?
# Math: to find how many days we have in 25 years old
# Notice that every year is 365 days
# So 365 times his/her age => will give us how many days: days = 365 * years
# Example: how many days we have in 10 years => 365 * 10
# Error: 365*"2" !!!
# The formula: the number of days = age * 365

# Ask the user to input his/her age:
age = int(input("Please enter your age: "))
# we know that input function returns a string data type,
# if the user inputs 24 => 24 will become "24"
# now remember after using int() function, the variable age contains an integer number!
# we have two functions to cenvert a string of numbers into real numeric numbers:
# int() => works with integers (whole numbers) - Similar to parseInt() in JavaScirpt :-)
# float() =>  works with both (integers numbers and float) - Similar to parseFloat() in JavaScirpt :-)

# Task#2:
days = 365 * age
# for testing:
print(days)  # A not user-friendly message!

# Task#:
# user_name is Alex
# age is 28
# Example output: Hello Alex! Based on your age which is 28, you have been alive for 10220 days.
# We need to concatenate strings variable with numeric variable
# In Py we need to concatenate string to string only
# In py we can't concatenate string to numbers like js
# now remember age variable has a numeric value, not a string
# The following code will throw this error: TypeError: can only concatenate str (not "int") to str
# py: can only concatenate str (not "int") to str
# print ("Hello "+user_name+"! Based on your age which is "+age+", you have been alive for 10220 days.")

# Just to recap, age is class of type integer:
print(type(age))  # <class 'int'>

# VIN (Very Important Note):
# Python doesn't accept unnecessary (not required) spaces before our lines of code:
# IndentationError: unexpected indent

# so we need to convert the age numeric value into a string: using a function named str(numeric_value) => string
# syntax: str(numeric_value) => string


# To summarize:
# *************
# We have used these list of Py Built-in functions:
# print(?)
# input(?)
# int(?)
# float(?)
# str(?)

# The three mainly used converting functions:
# *******************************************
# int() => converting a float or string to an int
# float() => converting an int or string to a float
# str() => converting an int or float to a string

# It is possible to control the data type when declaring a variable
# by combining with the specific data type function.
# Example:
# The my_number variable will be default to an integer:
my_number = 10
# If you intended a floating-point number, then use:
my_number = float(10)

# Task:
# ================================================================
# The following formula (equation) will generate/throw an error
# result = 40 + "2.2"
# print(result) # This will generate an error

# result_two = "The answer to the ultimate question is " + result
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(result_two)

# Solution Steps:
# 1. Use a data conversion method to convert "2.2" into a number type,
# so that the result printed to the terminal is 42.2
# 2. Use a data conversion method to convert the variable result into a string,
# so that the result printed to the terminal
# is The answer to the ultimate question is 42.2
# ================================================================


# *********************
#  String Formatting:
# *********************
# Solution#1:
# Below is the first option to format our output string:
print("Hello " + user_name + "! Based on your age which is " +
      str(age) + ", you have been alive for " + str(days) + " days.")

# We have other three options (solutions)
# Solution#2:
# Create placeholder items for each variable inside the string using "%s"
# and then refer to them later by using: %(list your variables as comma seperated)
print("Hello %s! Based on your age which is %s, you have been alive for %s days." %
      (user_name, age, days))

# Solution#3:
# using the string method named "format()" with {} as placeholder(s)
# Like JS, in py string is an object (class) that has methods
# so in py string has a method named format()
# like JS objectName.method() or objectName.property
# => the same here in py: object_name.method() or object_property.property
# We will use format() method as placeholder:
# to use format() method => our_string.format()

# Before answering the task, Let's take a simple example for using format() method with any string variable:
module = "Python"
program = "FSSD"
length = 600  # 600 hours

# Task: My program is FSSD, it's 600 hours length, current module is Python.
my_info = "My program is {}, it's {} hours length, current module is {}.".format(
    program, length, module)
print(my_info)

# another way:
detailsStr = "My program is {}, it's {} hours length, current module is {}."
print(detailsStr.format(program, length, module))

# For more information about using format() method:
# W3 Schools link: https://www.w3schools.com/python/ref_string_format.asp

# Below is the answer for our task:
print("Hello {}! Based on your age which is {}, you have been alive for {} days.".format(
    user_name, age, days))

# The code below is an error:
# because print() function CANNOT have other method attached to it
# print("Hello {}!").format(user_name)
# AttributeError: 'NoneType' object has no attribute 'format'
print("Hello {}!".format(user_name))

# Solution#4:
# formatting with f-strings you would do the following: f"{variable}"
# using f-strings you would do the following: f"{variable}"
# we have f and {variable}!!
# f stands format, this letter f will be just placed before our string
# {variable_name} => the placeholder of any variable
# The Modern :-) way of formatting a string
print(f"Hello {user_name}! Based on your age which is {age}, you have been alive for {days} days.")

# Notice that this Solution is similar to JS Template Literal:
# console.log(`Hello ${user_name}, your age is ${age}`)
# By using the back quote (the key beside number 1 key)

# one more extra way the same we had is JS console.log() method (beyond the course outline)
# in JS: var avg=90;
# in JS we used console.log("Your final average is: ",avg)
# be advised that py will add extra unnecessary spaces
print("Hello", user_name, "! Based on your age which is",
      age, ", you have been alive for", days, "days.")

# *****************
#  Type Conversion
# *****************

# Python functions include
##
# int() => Convert a float or string to an int (similar to JS paraseFloat())
# examples:
# int("35") => 35
# int(67.792) => 67
##
# float() => Convert an int or sting to a float
# examples:
# float("25.78") => 25.78
# float(72) => 72.0
##
# str() => Convert an int or float to a sting
##

# Example of using F-strings but we have this logical error!
# Notice: mean or average is the same at least in my lectures :-)
mean = float(first_number) + float(second_number) / 2
# Wrong result because of wrong using of PEDMAS!
print(f'The mean of x and y is {mean}')


# To review (summarize our lecture):
# When we use the input() function, the value that we input is a string.
# Therefore, if we want to add 2 + 2, then the output we’d get would be 22.
# To get around this, we would need to convert the returned value of input() function to number (int or float).
# We can do it by wrapping the input() function in the int() function
# ************************************
# For more details refer to:
# Course  => Python Fundamentals  =>  Strings and User Input
