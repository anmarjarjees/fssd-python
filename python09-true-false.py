# A value that is either True or False

first_bool = True  # it's case-sensitive: True
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

my_variable = True  # We can change it to False for more practice
# if (my_variable) {
#     console.log("It's True!");
# }

if my_variable:
    # In Py we DO HAVE to indent (adding spaces)
    # At least (1 space ) has to be placed before each line of this if block:
    # But notice that:
    # 1. By convension we SHOULD really add one TAB (4 spaces) before each line
    # 2. All the lines inside this if condition MUST have the same number of spaces
    # in this example all have (4 spaces = 1 TAB) which is the Python standard
    print("This condition is True")
    print("Here is my second line inside if")
    print("Here is my third line inside if")
    print("That's it")
    # At the end to close the if block, just start typing from the first column (begining)

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
