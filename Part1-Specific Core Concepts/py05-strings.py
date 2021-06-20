# In Python, anything contained inside quotation marks is treated as a string.
# We can use double quotes ("") or single quotes ('').
print("Hello World")

print('Hello World')

# print("Then Mike said "What is that?"") # error

# mixing ' and "
print('Then Mike said "what is that?"')

# print('It's a beautiful day') # error
print("It's a beautiful day")

# The example here from the challenge
# Define a variable, my_string, here, then print it.
my_string = "Without hard work, nothing grows but weeds."
# Print its type on a separate line
print(my_string)


# Just quick topic:
# using input() function to get input from the user:
# in Python version 2.x.x: raw_input()
# with version 3: 'raw_input' is not defined
# in Python version 3.x.x: input()
# Quick Example:
user_value = input("Enter any value you want: ")

print("The data type of your input value is:", type(user_value))

# To Summarize:
# In Python, anything contained inside quotation marks is treated as a string.
# We can use double quotes ("") or single quotes ('').
# A string can be made up of any Unicode characters.
# Unicode characters contain 143859 characters from modern and historical scripts,
# including symbol sets.

# Important Note:
# If you have a long piece of text on multiple lines,
# you can enclose it in three double quotes """ or three single quotes '''
# as a multiline string.


# Your Task:
# 1. Define a variable named parrot and assign it the value: "It's not pining,
# it's passed on! This parrot is no more! It has ceased to be!"
# 2. print out the variable parrot

# ****************************************************
# The keyword "None"
# Signify 'empty' or 'no value here'
# Using the keyword "None" to define when there is no value at all for something
# It is not the same a 0 or the boolean False or an empty string
# Instead, None is a signal object used in Python to signify ‘empty’ or ‘no value here’.
# if you have a variable, it has a value, and if you want to remove that value, you can reassign the variable to None
# None has the data type of NoneType, which is a built-in data type just like int or float
# Example of using None:
a = 1
a = None
print(a)  # None

# to be explained (def for define a function)


def do_nothing():
    b = 0


print(do_nothing())  # None

# Your Task:
# Create a variable named admin, assign it the value: None
# On the next line type: print(admin)
