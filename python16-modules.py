# Using Modules:
# In Python, we call a Python file a module.
# as developers, we also create modules every time we create our python files.
# We can even import functions, classes, and variables from other modules (files)
# from file_name import required_function

# Example we want to use a built-in function named randint() to generate random integer numbers
# This function inside a module named "random"
# "random" module (file) contains "randint()" function

from random import randint
# We use the "from" keyword to target a module (a python file)
# and the "import" keyword to import the specific function
# from the random module.

# printing a random integer value between 1 and 100
print(randint(1, 100))
print(100)
# The randint function takes two arguments
# which define the range from which to generate a random number.
# The first argument being the lowest number
# and the second argument being the highest possible generated number.
# Our example above generates a random number between 1 and 100.

# we didn't have to create a new function to generate a random number,
# we only imported this already created function
# from a module (python file) named "random"

# In Python, a module is just a file.
# Specifically, it's a file with the extension .py on the end.
# When you install Python, all it's really doing
# is placing a bunch of .py files into various folders on your computer.
# And what is a .py file, exactly? What's in it?
# Well, it's just a bunch of Python code of course!
# It's like a word document that just happens to be full of functions and other Python code,
# just the like ones you've written in recent examples.

# The key to understanding Python (and object oriented programming in general)
# is to understand that everything is just a file that can be imported
# so that it's functions can be used in your own code.
# To do this in Python, we use the import statement.
# In general there are a couple different ways to import a file in Python

# For more practice try this challenge:
# Python Fundamentals > Modules > Using Modules Challenges (The second icon)
"""
Another way of writing multiple lines of comments
Multiline comments can take up as many lines as you require. 
The comment itself is put between:
three opening double quotations and three closing double quotations.
Although it's not the official symbols of writing a comment 
"""
