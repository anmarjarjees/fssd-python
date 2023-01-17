# In this file, we need to use the PI of the "math" module
# This module "math" provides access to the mathematical functions defined by the C standard
# In order to use/access all the functions inside the "math" module,
# We need to import it into our current python file
# # Import "math Library"
import math  # This will import the full library of the module "math"

# or if we only need to use the "pi" from the module "math"
# we can use also use this sentence
from math import pi  # this will import ONLY the "pi" constant for the module "math"

# By the way, you can use * symbol to import everything
# from math import * == the same as ==> import math


# We had the same in JS => Math.PI
# For reviewing: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI

# Constants: math.pi
# The math.pi constant returns the value of PI: 3.141592653589793
# Print the value of pi
print(math.pi)

print(pi)

# The value of "pi" from the "math library" is expressed within the print statement.
# A "format specifier" can be included after the "colon." => :.
# In this case, the value is rounded to two significant figures
# Here the format specifier ".2f" is used to truncate at 2 decimal places
print(f'The value of pi to 2 decimal places is {math.pi:.2f}')

# NOTE: If we don't import the math library, we will receive this error
# NameError: name 'math' is not defined

# Two more examples about using :. and a format specifier:
my_number = 70.89189
print(f"My number is: {my_number:.2f}")  # 70.89

my_number = 9189
print(f"My number is: {my_number:.2f}")  # 9189.00


# When including a "non-keyboard character" such as the pound sterling,
# it can be done by using the chr() and the Unicode value (163 in this case).
# The currency symbol for pounds sterling has Unicode character number 163
pound = chr(163)
print(pound)  # £

# Creating a dictionary:
tabulate = {
    'Egg & Spam': 1,
    'Egg, Bacon & Spam': 1.5,
    'Egg, Bacon Sausage & Spam': 2,
}

# the simple/basic print
# {'Egg & Spam': 1, 'Egg, Bacon & Spam': 1.5, 'Egg, Bacon Sausage & Spam': 2}
print(tabulate)
print(type(tabulate))  # <class 'dict'>

# simple loop to print the tabulate:
# This loop is not useful! It will print every item 3 times because we have 3 elements
"""
for item in tabulate:
    print(tabulate)
"""

# the reasonable and better loop option => using items() method
for item in tabulate.items():
    print(item)
# The output:
# ('Egg & Spam', 1)
# ('Egg, Bacon & Spam', 1.5)
# ('Egg, Bacon Sausage & Spam', 2)

# print the keys and the values of tabulate without spacing format:
# in this for loop:
# The variable "key" will represent each key in the dictionary:
# Egg & Spam, Egg, Bacon & Spam, and Egg, Bacon Sausage & Spam
# The variable "value" will represent each value for every individual key:
# 1, 1.5, 2
print("==== Main Menu ====")
for key, value in tabulate.items():
    print(f"the meal: {key}")
    print(f"its price: {value}")
    print("===================")
# The output:
# the meal: Egg & Spam
# its price: 1
# ===================
# the meal: Egg, Bacon & Spam
# its price: 1.5
# ===================
# the meal: Egg, Bacon Sausage & Spam
# its price: 2
# ===================

# Loops over a dictionary:
for key, value in tabulate.items():
    # The format specifiers here denote a minimum width of 25 for the key labels
    # and 5 characters for values of each key
    print(f'{key} - {pound} {value}')
# The output:
# Egg & Spam - £ 1
# Egg, Bacon & Spam - £ 1.5
# Egg, Bacon Sausage & Spam - £ 2

# Loops again over a dictionary of menu items as keys and prices as values
for item, price in tabulate.items():
    # The format specifiers here denote a minimum width of 25 for the key labels
    # and 5 characters for values of each key
    print(f'{item:25} - {pound} {price:5}')
# The output:
# Egg & Spam                - £     1
# Egg, Bacon & Spam         - £   1.5
# Egg, Bacon Sausage & Spam - £     2


# The newline (\n) is used to add a new line after the second print statement
# This also helps make the output easier to read.

# loop through a number from 99 down to 1
for number in range(99, 0, -1):
    line_one = f"{number} bottle(s) of beer on the wall. {number} bottle(s) of beer"
    line_two = f"Take one down, pass it around. {number-1} bottle(s) of beer on the wall\n"

    print(line_one)
    print(line_two)
