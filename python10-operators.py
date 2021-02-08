# Less than: <
# <=
# ==
# >=
# >

# if we put 20 => "20" but after float(): 20
number = float(input("Please enter a number: "))

if number <= 5:
    print("The number is less than 5, good job!")

# An 'if statement', establishes if a condition is true or false.
# Python includes elif (else if in JS) and else.

your_num = float(input("Please input another number: "))

if your_num == 10:
    print("%s is equal to 10" % your_num)
    # OR using the "modern" way: using f-format
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

# ************************
#  Logical Operators
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
# if (it_is_one_oclock != True) {
#     my code
# }

# OR in JS:
# if (!it_is_one_oclock) {
#     my code
# }

print("### using not example: ###")
if not it_is_one_oclock:
    # The keyword "not":
    # if not (False) => if it's True
    # if not (True) => if it's False
    print("We can continue...")
else:
    lecture
    print("We need to end our lecutre")

# declare a variable "avg" with the value of 92.0
avg = 92.0

if avg >= 90 and avg <= 100:
    # this condition will work only if True and True
    print("Excellent")

# Example of using "or" logical operator:
# You can apply for TPL Card for "FREE" if you met at least one of the following condition:
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
# - Thinking of "and" to be * and "or" +
# - The result is either 1 or 0 (no 2)
#
# TRUE and TRUE => TRUE => 1 * 1 = 1
# TRUE and FALSE => FALSE => 1 * 0 = 0
# FALSE and TRUE => FALSE
# FALSE and FALSE => FALSE

# TRUE or TRUE => TRUE => 1 + 1 = 1
# TRUE or FALSE => TRUE => 1 + 0 = 1


# Another example (LMS):
# 3 boolean variables:
exit_program = True
manual_override = False
critical_systems_shutdown = False

if not exit_program and not critical_systems_shutdown:
    # not exit_program => False
    # not critical_systems_shutdown => True
    # if "False" and "True" => False
    # so this if block will not run because this condition is False
    print("Shutting System")
elif exit_program and critical_systems_shutdown is not True:
    # exit_program: True
    # critical_systems_shutdown is not True: True
    # elif True and False is not True => True
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")

# the same code in JS:
# if (!exit_program && !critical_systems_shutdown) {
#     console.log("Shutting System");
# } elseif (exit_program && critical_systems_shutdown!=True) {
#     console.log("Critical systems must be safely shut down before exiting the program");
# } else {
#   console.log("This program will now be terminated...")
# }

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
    my_greeting = "Good morning"
else:
    my_greeting = "Good evening!"

print(my_greeting)

# the other way "Ternary Operator":
# our_variable = this_value if True else other_value
my_message = "Good morning" if its_morning else "Good evening!"
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
    print("Please take the Vegetarian menu")
else:
    print("Please take the Normal Menu")

# Second part using the ternary operator:
# Hint: you can use a variable or direct print
menu = "Please take the Vegetarian menu" if is_vegetarian else "Please take the Normal Menu"
print(menu)
