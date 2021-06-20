# Using Modules:
# In Python, we call a Python file a "module".
# as developers, we also create modules every time we create our python files.
# We can even import functions, classes, and variables from other modules (python files)
# The syntax: from file_name import required_function

# Example:
# we want to use a built-in function named randint() to generate random integer numbers
# This function inside a module (a python file) named "random"
# the "random" module (Py file) contains "randint()" function

# Case1: you can use this import statement
# importing only randint function/method from the module random
from random import randint

# Case2: you can use this one
import random  # importing the entire library of the module "random"

# We use the "from" keyword to target a module (a python file)
# and the "import" keyword to import the specific function(s)
# from the random module.

# to call "randint" => randint(a: int, b: int)
# Return random integer in range [a, b], including both end points
# printing a random integer value between 1 and 100
print(random.randint(1, 100))
# If we don't import this function form its file:
# NameError: name 'randint' is not defined

# The randint function takes two arguments
# which define the range from which to generate a random number.
# The first argument being the lowest number
# and the second argument being the highest possible generated number.
# Our example above generates a random number between 1 and 100.

# we didn't have to create a new function to generate a random number,
# we only imported this already created function
# from a module (python file) named "random"

# In Python, a module is just a file.
# Yes, it's a file with the extension .py on the end.
# When you install Python:
# Python will place a bunch of .py files into various folders on your computer.
# the .py file is just a bunch of Python code of course!
# It's like a word document that is full of functions and other Python code,
# just the like ones you've written in our code examples.

# The key to understanding Python (and object oriented programming in general)
# is to understand that everything is just a file that can be imported
# so that it's functions can be used in your own code.
# To do this in Python, we use the "import" statement.
# In general there are a couple different ways to import a file in Python

"""
Another way of writing multiple lines of comments
Multiline comments can take up as many lines as you require. 
The comment itself is put between:
three opening double quotations and three closing double quotations.
Although it's not the official symbols of writing a comment 
"""

# To summarize:
# If you use Case1 => from random import randint
# the statement => randint(min,max)
print("print a random number from 1 to 10")
print(randint(1, 10))

# If you use Case2 => import random
# the statement => random.randint(min,max)
print("print a random number from 1 to 10")
print(random.randint(1, 10))

# We will cover this concept in more details, so stay tuned
