# In addition to the basic exception "RuntimeError".
# We used these built-in more specific exceptions:
# >> "ValueError"
# >> "ZeroDivisionError"
# These are more specific exceptions provided by Python. When writing your code

# It is essential to think about what possible errors might happen and how to handle them.
# It is a good idea to test your code as you go.
# What happens when you enter incorrect values for your function arguments, for example?
# Using more specific exceptions can make it quicker to debug what has gone wrong with your code.

# Good to do:
# When you raise an exception,
# you can include a string of text to provide information pertinent to your code.

# The following commented code below that we used in the previous file contains 3 except blocks:
"""
while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except ValueError:
        print("Both values have to be integers.")
    except ZeroDivisionError:
        print("Please enter a valid denominator (has to be more than 0).")
    except Exception:
        print('Another error has occurred')
"""

# Can be summarized to the following code
# By including "multiple specific exceptions" in just one "Except" block using a tuple!

# Example (same one but with only one except block):
# This code is commented:
"""
while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)

     # Multiple specific exceptions can be included in one except block by addeding them to a tuple
    # in the except statement.
    except (ValueError, ZeroDivisionError):
        print('An error has occurred')
"""
# Notice that a specific exception can be raised anywhere in your code to catch errors.

# Example: a try block which counts down from 5 to -5
# flor loop printing 5 4 3 2 1 0 -1 -2 -3 -4 -5
# Note that both exceptions "raise Exception" and "raise TypeError" include custom text
try:
    # counts down from 5 to -5
    for i in range(5, -6, -1):
        if i < 0:
            # raises an exception for negative numbers
            raise Exception('Integers must be positive.')
        else:
            print(i)

# At the point this exception is raised the except block is run.
except:
    x = [1, 2, 3, "hello"]
    # This time a list is looped through and an exception is raised if a non-integer value is seen.
    for item in x:
        # we are explicitly checking for type
        if not type(item) is int:
            # In this "except" block a TypeError has been raised as we are explicitly checking for type.
            raise TypeError("Only integers are allowed")
        else:
            print(item)

# NOTE and Hint:
# To see the complete list of the built-in Python exceptions,
# You can read this article in the official documentation in this link:
# Link: https://docs.python.org/3/library/exceptions.html#built-in-exceptions

# Challenge: Catching Specific Errors
# Steps:
# 1. Write a try, except statement.
# In the try statement, try to print a variable named non_existent_variable that has not been defined.

# 2. Use an except statement to check for a "NameError" exception
# and print "Variable not defined" to the terminal if a NameError occurs.
