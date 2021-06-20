# Passing Functions Around
# - A function is an object
# - Allows you to pass a function around
# - Avoid repetition by reusing existing functions

# NOTE:
# In Python, functions are "first class objects" that means that functions in Python
# can be used or passed as arguments.

# In Python function is itself an object:
# Is an instance of the "Object" type
# We can be refer to a function in the same way as we refer to a string object
# You can assign a function to a variable or even store it in a data structure
# A function can be passed as a parameter into another function or even to itself
# You can return the function from a function
# you can check this article: https://www.geeksforgeeks.org/decorators-in-python/

# List of numeric values (array in JS)
numbers = [4, 7, 12, 33, 13, 67]

# Using the pop() method (function inside an object) to remove the last element in our list
# W3Schools: https://www.w3schools.com/python/ref_list_pop.asp
removed_num1 = numbers.pop()
print(removed_num1)
print(numbers)  # [4, 7, 12, 33, 13]

# Or we can do it in Python in this way:
# We used the list method pop again on numbers but assign it to the variable "removed_num2"
removed_num2 = numbers.pop
print(removed_num2)  # <built-in method pop of list object at 0x000001C7955584C0>

# Imagine that we are telling python to concatenate the value of varaible "removed_num2" which "numbers.pop"!
# to the () => the result => numbers.pop()
# Python: numbers.pop + () => numbers.pop()
# By merely adding parentheses to the variable "removed_num2" => we can use the pop method!
print(removed_num2())  # 13
print(numbers)  # [4, 7, 12, 33]

# Just for fun:
# removed_num2 = numbers.anything
# AttributeError: 'list' object has no attribute 'anything'

# let's try to remove the number "12" which has the index of 2
print(removed_num2(2))  # 12
print(numbers)  # [4, 7, 33]

# Another Example:
integers = [1, 2, 3, 4, 5, 6]

# Create a function to return:
# True => if the integer value in our list "integers" is divisible by three
# False => if otherwise
# In Math, the number is divisible by three if we have no reminder when we divide it by 3
# in other word, if the remainder of the division by 3 is 0 => this number is divisible by three
# Using the modulo "%" operator


def is_divisible_by_three(num):
    # => because we are using "==" => it's a comparison equation that returns either True or False
    return num % 3 == 0


print(is_divisible_by_three(27))  # True
print(is_divisible_by_three(28))  # False
print(is_divisible_by_three(5))  # False
print(is_divisible_by_three(3))  # True

# passing both the function "is_divisible_by_three" and the list "integers"
# to a builtin function from Python called filter() which returns only the values that are True
# W3Schools: https://www.w3schools.com/python/ref_func_filter.asp
# The list() function creates a list object
# W3schools: https://www.w3schools.com/python/ref_func_list.asp
my_new_list = list(filter(is_divisible_by_three, integers))
print(my_new_list)  # [3, 6]

# One More Example:


def print_arguments(**args):
    """Prints the arguments"""
    print(f'The arguments are {args}')


def pass_function(function_name, **args):
    """Takes a function as an argument
    Passes the argument 'l' to the function passed in 
    """
    print("This function takes another function as an argument")
    function_name(f=args['l'])  # The arguments are {'f': 'spam'}


pass_function(print_arguments, l='spam')
