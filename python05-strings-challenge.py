# Define a variable, my_string, here, then print it.
my_string = "Without hard work, nothing grows but weeds."
# Print its type on a separate line
print(my_string)


# Data Types:
# string: "ABC" or "123" or 'XYZ' or '456'
# numbers: Int (whole number) or float (with decimals)
# boolean: True of False
# In JavaScript, we used typeof() => return the data type of the variable
# Example: console.log(typeof(my_string)); # in JS

# in Py => type() => return the data type of the variable
print(type(my_string))  # <class 'str'>


num = 7.8
print(type(num))  # <class 'float'>

max = 100
print(type(max))  # <class 'int'>

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

print("The data type of your input value is:", type(user_value))
