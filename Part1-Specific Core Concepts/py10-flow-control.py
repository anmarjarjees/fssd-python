# Less than: <
# <=
# ==
# >=
# >

# A value that is either True or False
# In JavaScript, we have to write the 2 bool values all in small letters:
# true
# false

first_bool = True  # it's case-sensitive: True
# Error when using "true" => NameError: name 'true' is not defined
second_bool = False  # the same: False

print(first_bool, second_bool)  # True False

# remember in JS we used typeof() => the data type of this value or variable
# typeof() => number, string, or boolean

# in Python we type() => the data type of this value or variable
# type() => int, float, string, or boolean
first_variable = 1
second_variable = 1.0
third_variable = "Hello world"
fourth_variable = True

print(type(first_variable), type(second_variable),
      type(third_variable), type(fourth_variable))
# output: <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

# We used ALT + 3 / 4 for adding/removing comment symbols => it was in Python IDLE
# In VSC: CTRL + / => to add/remove a comment => To toggle the comment

# Determining The Flow Of Execution
# if True
# then do this thing

# In JS:
# If my_variable is "True" or if it has any value then run the if block code
# if (my_variable) {
#     // do my code here (if block code)
# }

# In Python, the condition to be evaluated is terminated with a colon
# and a new line.
# The conditional code to be run if True is indented
# by four spaces as opposed to the curly braces used in JavaScript

my_variable = False  # We can change it to False for more practice
# if (my_variable) {
#     console.log("It's True!");
# }

if my_variable:
    # In Py we DO HAVE to indent (adding spaces)
    # At least (1 space ) has to be placed before each line of this if block:
    # But notice that:
    # 1. By convention we SHOULD really add one TAB (4 spaces) before each line
    # 2. All the lines inside this if condition MUST have the same number of spaces
    # in this example all have (4 spaces = 1 TAB) which is the Python standard
    print("This condition is True")
    print("Here is my second line inside if")
    print("Here is my third line inside if")
    print("That's it, These are all my lines inside if condition")
# At the end to close the if block, just start typing from the first column (beginning)

# This line is not part of if block
print("Here is my text outside the if block")

# Using if else:
light = 'green'  # We can use ' or " with string values

# Like JS we CANNOT use = comparison, also here in Py We have to use ==
if light == 'green':
    print('You may proceed')
    print('Take your bus')
else:
    print('Please wait here')

print("I am the rest of the program that will always appear whatever the condition is true or false")


# if we put 20 => "20" but after float(): 20
number = float(input("Please enter a number: "))

if number <= 5:
    print("The number is less than 5, good job!")

# An 'if statement', establishes if a condition is true or false.
# Python includes elif (else if in JS) and else.

your_num = float(input("Please input another number: "))

if your_num == 10:
    # Task: output => 10 is equal to 10
    # the first 10 will be the variable "your_num"
    # The 3 different ways to output our text and numeric values as we explained before:

    # First Way:
    print(str(your_num) + "is equal to 10")

    # Second Way:
    print("%s is equal to 10" % your_num)

    # Third Way:
    print(f"{your_num} is equal to 10")
else:
    print("%s is not equal to 5" % your_num)
    # Or
    print(f"{your_num} is not equal to 10")


last_num = float(input("Please input another number for the last time: "))

if last_num > 5:
    print(f"{last_num} is greater than 5")
elif last_num < 5:
    print(f"{last_num} is less than 5")
else:
    print(f"{last_num} is equal to 5")


# The Modern way of formatting a string
print(
    f"Hello! your first number was {number}, and you are last one was {last_num}")


# *************************
# Logical Operators
# In JS ! => In Python: not
# JS && => Python: and
# JS || => Python: or
# *************************

it_is_one_oclock = False  # It's not 1:00 (PM)

if it_is_one_oclock:  # it means if "it_is_one_oclock" is True or if it has a value
    print("We need to end our lecture")
else:
    print("We can continue...")

# In JS
# if (!it_is_one_oclock) {
#      console.log("We need to end our lecture");
# } else {
#     console.log("We can continue...");
# }


# OR in JS:
# if (it_is_one_oclock != True) {
#     my code
# }


print("### using not example: ###")
if not it_is_one_oclock:
    # The keyword "not":
    # if not (False) => if it's True
    # if not (True) => if it's False
    print("We can continue...")
else:
    print("We need to end our lecture")

# declare a variable "avg" with the value of 92.0
avg = 92.0

if avg >= 90 and avg <= 100:
    # this condition will work only if True and True
    print("Excellent")

# Example of using "or" logical operator:
# You can apply for "Toronto Public Library-TPL" Card for "FREE"
# if you met at least one of the following condition:
# 3 boolean variables:
live_in_toronto = False
study_in_toronto = False
work_in_toronto = True

if live_in_toronto or study_in_toronto or work_in_toronto:
    print("You can have TPL card for free!")
else:
    print("You need to pay for this card")

# Hint:
# - Thinking of True is 1 and False to be 0
# - Thinking of "and" to be * and "or" to be +
# - The result is either 1 or 0 (no 2)
#
# TRUE and TRUE => TRUE => 1 * 1 = 1
# TRUE and FALSE => FALSE => 1 * 0 = 0
# FALSE and TRUE => FALSE
# FALSE and FALSE => FALSE

# TRUE or TRUE => TRUE => 1 + 1 = 1
# TRUE or FALSE => TRUE => 1 + 0 = 1


# Another example (LMS):
# Declaring (with initial value for sure) three variables boolean variables:
exit_program = True
manual_override = False
critical_systems_shutdown = False

if not exit_program and not critical_systems_shutdown:
    # not exit_program => False
    # not critical_systems_shutdown => True
    # if "False" and "True" => False
    # so this if block will NOT run because this condition is False
    print("Shutting System")
elif exit_program and critical_systems_shutdown is not True:
    # exit_program: True
    # critical_systems_shutdown is not True: True
    # elif True and (False is not) True => True
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")

# The same code in JS:
# if (!exit_program && !critical_systems_shutdown) {
#     console.log("Shutting System");
# } elseif (exit_program && critical_systems_shutdown!=True) {
#     console.log("Critical systems must be safely shut down before exiting the program");
# } else {
#   console.log("This program will now be terminated...")
# }


# Now The same example with the same 3 boolean variable but using "Nested Conditions"
# By implementing additional if-else ladders inside of existing if-else blocks
# Read the logic/code and try to guess the answer before checking the output
if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")


# *****************
# Ternary Operator:
# *****************
# Sometimes we don’t need to create lengthy if-else conditions,
# as it would be easier to work with a single one-line of code (simple formula).
# In this instance, we’d use an if expression

# Example:
its_morning = False  # boolean variable with the value of "False"

# Simple if condition block (first):
if its_morning:  # if my_boolean_var == True OR has any value except "False"
    my_greeting = "Good morning!"
else:
    my_greeting = "Good evening!"

print(my_greeting)

# the other way "Ternary Operator":
# our_variable = this_value if True else other_value
my_message = "Good morning!" if its_morning else "Good evening!"
print(my_message)

# another example from a previous :
light = 'red'
# Task convert this into ternary Operator
if light == 'green':
    print('You may proceed')
else:
    print('Please wait here')

# with ternary operator, we can create a variable to get the returned value:
what_to_do = 'You may proceed' if light == 'green' else 'Please wait here'
print(what_to_do)

# Or we can place the full logic (Ternary Operator) inside print function
print('You may proceed' if light == 'green' else 'Please wait here')

# Another example of placing the entire ternary statement inside the print()
age = 22
print("You can register for this course" if age >=
      18 else 'Please contact your advisor')

# Even / Odd Number Check
num = 2
if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')

result = 'Even Number' if num % 2 == 0 else 'Odd Number'
print(result)

# Challenge (Restaurant):
# 1. Create a boolean variable if the customer is "vegetarian": True or False
is_vegetarian = True  # Assuming that the customer is vegetarian

# 2. If condition and If ternary operator to print:
# "Please take the Vegetarian menu" <= if the customer is vegetarian
# "Please take the Normal Menu"

# First part using if condition full block:
if is_vegetarian:
    print("Please take the Vegetarian Menu")
else:
    print("Please take the Normal Menu")

# Second part using the ternary operator:
# Hint: you can use a variable or direct print
menu = "Please take the Vegetarian menu" if is_vegetarian else "Please take the Normal Menu"
print(menu)


# Breakpoints Using "raise SystemExit"
# It is an Exception in python => Breaks out of a running program
# Using: raise SystemExit()
# You might need to stop the program at a specific point
# to see what state it is in at that time.
# "raise SystemExit" forces the program to stop at a particular point.
# SystemExit, when raised, runs the exit() function in Python.
# This means the code is exited safely.
# This is analogous to shutting down your desktop PC from the menu
# rather than switching off the power at the wall

age = 17
if age <= 18:
    #print('You must be older than 18!')
    raise SystemExit(f'Sorry your age is {age}! You must be older than 18.')

# All the code below will be ignored because of "raise SystemExit"
print("Some simple code below for testing!")
num1 = 2
num2 = 3
total = num1 + num2
print(total)
# ****************************************************************************************************
# ====================================================================================================

# FizzBuzz is a classic programming problem that is often asked as an interview question.
# Write some tests for the FizzBuzz game.

# Problem:
# Create a function called fizzBuzz:
# This function should take in number as a parameter
# (numeric argument is needed to be passed into this function).

# The function should do the following:

# If the number is divisible by 3 AND 5, then print "FizzBuzz", example: 15
# If the number is divisible by 3, then print "Fizz", example: 9
# If the number is divisible by 5, then print "Buzz", example: 25
# Else just print the number itself, example: 8

# Write a set of tests that pass in various values to the FizzBuzz function
# and ensure that the function meets the above requirements.
# Make sure that you test all different "types" of inputs that the function may receive.
# **************************************************************************************

# The math logic (formula):
#  1) How to know if the number is divisible by 3 (the number can be divided by 3 without remainder):
#     for example: 243

#     - we add every individual number 2+4+3 = 9
#     - can we divide 9 by 3 with out any remainder and the answer is Yes
#     So the number "243" is divisible by 3

# 2) How to know if the number is divisible by 5:
#    for example: 3425
#     - We need to look at the last number if it's 0 or 5
#     - If Yes then this number is divisible by 5

# The logic for programming based on the code institute logic:
#     if the remainder of division by 3 is 0 => divisible by 3
#     if the remainder of division by 5 is 0 => divisible by 5
# **************************************************************************

# To review:
# we did a similar example in our lecture, when we had to find if the number is even or odd
# The logic:
# if the remainder of dividing the number by 2 is 0 => it's an even number
# else it's an odd number
# the formula: number % 2


num = float(input("Input your number: "))

if (num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
elif (num % 3 == 0):
    print("Fizz")
elif (num % 5 == 0):
    print("Buzz")
else:
    print(num)

# A challenge:
# You have these two variables:
admin = False
update_required = True
# The steps for this challenge:
# Steps:
# 1. Write an if-else statement, that checks the variable admin, if it is assigned True pass (using the pass keyword) if it assigned False print: "You need admin privileges to do this"

# 2. If you have correctly structured your if-else and run your code it should print out the above string

# 3. Remove the pass keyword

# 4. And add another if-else statement, that checks the variable update_required, if it is assigned True print: "You are authorized to update" else print: "No update required"

# 5. Change the value of the variable admin on line one to: True

# 6. If you have correctly structured your nested if-else statement and set the variable admin to True your output should match the image above.
# Tips
