# file input and output or I/O for short.
# Data that is taken from the user for example from a keyboard can be written to file.
# Data in a file can be read and output to the screen
# how to store data on a disk using files

# 1) Reading data from user: input() function
# We're all familiar with working with Graphical User Interface (GUI).
# The GUI is where we execute applications from our Desktop, opening folders from My Computer, creating Documents in Microsoft Office, and browsing the web with Chrome or Firefox.
# While we're working with Python, and providing output to a user, we're using the Command Line Interface (CLI).
# This interface is text-based, as opposed to the graphics-based interface

# input():
# The input function stops the running of the program
# and waits for the user to enter data in the command line
# and press return (Enter Key)
# whatever the user inputs is converted to a string

# Example:

# The programme will remain stopped
# until you respond to this prompt with some text and press the return key
username = input("Type in your name and press return: ")

# As the value type that is received from an input is a "string"
# We need to convert it to a number to be able to use it on our formula to find how many days
# We can do this by wrapping the input inside the int() method
age = int(input("Please enter your age: "))

days = 365 * age
# days is a number
# To concatenate it to the string we have to convert it to a String
# Notice below we do this like: str(days). Yes we can also use f-strings
print("Hello " + username +
      ", you have been alive for at least " + str(days) + " days")

# 2) Returning Data to a User: print() function
# The output can be written to the terminal window => print()
# Also can be be written to a file

# Examples:
# simple one-line expression (10 + 20) which is assigned to a variable i
i = 10 + 20
# just print i
print(i)

# We have assigned a string to variable language and an integer to variable version.
language = "Python"
version = 3.9
# Formatted string literals are a way to improve the human readability of the output:
print(f'We are using {language}{version}')
