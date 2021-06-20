# Functions:
# Functions allow us to write a chunk of code that we can invoke whenever we choose
# So the main purpose behind using functions is to have reusable code
# We've used plenty of different Py built-in functions:
# print(), input(), range(), and len()
# We will learn to create our own custom functions

# In JS:
# function printMessage() {
#     console.log("Hello World!");
# }

# printMessage()

# Using PythonTutor


# In Py: we also need to create the function then call it later
# def: This is the keyword that we use to tell Python that we are creating a function definition
# then the function name, be sure to give your functions meaningful names
# when other people try to use your code, they'll able to make sense of what the function does
# without having to read the code in the function

def print_message():
    print("Hello World!")


# A function is a block of code that only runs when it is called
# Calling a function is executing the code => use the function name followed by parentheses
# A function can be called by another function or even by itself
# call/run the function (4 times):
print_message()  # Hello world!
print_message()
print_message()
print_message()

# NOTE: Python functions MUST BE declared and defined before they are called


# Parameters and Arguments:
# We might need our functions to perform actions on specific pieces of data.
# In this case, we would use "parameters" and "arguments" to pass that part of data to the function
# You can pass information into the function as arguments inside the parentheses separated by commas
# (parameter) => is the variable listed in the parentheses when the function is defined
# (argument) => is the value you pass into the function parentheses when it is called

# name is a parameter for this function (the variable to used inside the function)
# This function is expecting to have a value for the name parameter
def show_content(name):
    # the value of the "name" are being used in this print statement
    print(f"Hello {name}!")


    # Alex will be the argument => the value to be passed to function parameter
show_content("Alex")
# Martin will be the argument => the value to be passed to function parameter
show_content("Martin")

# This code will give us an error:
# TypeError: show_content() missing 1 required positional argument: 'name'
# show_content() # error because this function needs an argument

# in JS
# let x=1;
# if (x) {
#     // add my code later
# }

# in Py
x = 1
if x:
    pass


# another example:
# Task: create function to receive the value of user's age
# if the user's age is equal to or greater than 18 print "Go to classroom#18"
# else print "Go to classroom#12"

# we can set a default value for "age" parameter in case if we didn't pass any value to the function
# this called an optional parameter
# Optional parameters will allow us to provide values to a function with some value
# in case they are not provided when the function is invoked

def user_age(age=15):
    if age >= 18:
        print("Go to classroom#18")
    else:
        print("Go to classroom#12")


# saving our time by hard coding the age value (instead of input to ask the user)
your_age = 20
user_age(your_age)  # Go to classroom#18

# below we are not passing any value, the age will be equal to 10 (by default)
user_age()  # Go to classroom#12

# user_age("abc) # age = "abc"
# TypeError: '>=' not supported between instances of 'str' and 'int'
# Python can't solve this question: is abc >= 18 ???

# More Examples: Using "return" Statement

# Example 1:


def print_name(name="World"):
    return f"Hello {name}"


username = input("What's your name? ")
print(print_name())  # Hello World
print(print_name(username))  # Hello the value of username


# Example 2:
# 2. This function runs for the name and age function calls


def get_user_input(prompt):
    # The return statement (exactly like JS):
    # - returns the result of the function and is the point where the code stops running
    # - statements after a return statement are not executed
    # - can only be used within a function
    # NOTE: if no expression is included in the return statement, then "None" is returned
    return input(prompt)

# 4. This function runs twice


def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)


# 1. name and age are the first two function calls to run sequentially (when we run our app)
name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

# 3. Then function calls run sequentially
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")

# lambda:
# There is another type of function in "Python" known as "Lambda":
# - a small anonymous function (no name just the keyword "lambda").
# - can take any number of arguments but only has one expression
# W3schools: https://www.w3schools.com/python/python_lambda.asp


# Example:

# Here is the normal function of just adding two numbers
def add1(a, b):
    return a + b


# Writing the same function using lambda
# As you can see the function has no name (hence anonymous) so we have assigned it to the variable add
# The pattern: "lambda" the list of the parameters with commas : one experssion (one statement)


def add2(a, b):
    return a + b
# add2 = lambda (a, b): a + b


print(add1(5, 12))
print(add2(5, 12))


def multiply(a, b): return a * b
# Or using lambda
# multiply = lambda a,b: a*b


print(multiply(5, 6))


# Challenge:
# Steps
# 1. Define a function named "add_numbers" that takes two parameters: named: nums_tuple, min_value
def add_numbers(nums_tuple, min_value):
    # 2. The function should "return" the "sum" of all the values in the nums_tuple
    # that are greater or equal to the min_value
    sum = 0
    for num in nums_tuple:
        if num >= min_value:
            sum += num
    return sum


# 3. Outside of the function
# 4. Create a variable named: total and assign it the return value from calling the add_numbers function and passing in the two arguments: (21, 4, 7, 19, 1), 15
total = add_numbers((21, 4, 7, 19, 1), 15)

# 5. print total
print(f"total is: {total}")
