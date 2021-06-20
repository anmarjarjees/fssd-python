# The print() Statement:
# The print() function (provided by Python) displays information on the screen.
# It is used in command line (or terminal) or scripts
# Functions: are a grouping of statements that work together
# to perform any actions that we may need

# NO ; with python
print("Hello World!")

# Or with commas
print("Please", "say", "hello", "back!")

# Hint for debugging:
# By placing print statements throughout your code
# you can see what values are at each point
# in the same way you did with JavaScript console.log().
# This helps debug the code by finding from where the unexpected result is generated.


# *************
# Syntax Errors
# *************
# Programming in Python like any other programming language
# can have errors. Two main types of errors:

# "Syntax Errors" OR "Parsing Errors":
# ************************************
# the most commonly seen error messages
# The parser repeats the line where the error has been detected
# in the terminal.
# A caret (^) points to the earliest point in the line
# where the error occurs.

# Look for the arrow pointing to your error

# Example:
# print 'Hello, World!' <=> Error No Brackets!

# Logic Errors:
# *************
# Logic errors are when the code gives a different output than you were expecting
# These are the most difficult errors to fix
# An error with the logic of your code => Debug the code

# Example:
# Simple formula to find the average (as we did in JavaScript):
exam1 = 90
exam2 = 80
average = exam1+exam2/2  # <=> Error: Incorrect Operator Precedence
