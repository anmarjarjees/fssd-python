# The **kwargs object behaves very similarly but rather than a tuple is a dictionary.
# Like with *args you can change the name as long as the ** unpacking operator precedes it
# Where you would use **kwargs over *args is when you have a keyword or named arguments

# below, you can only add two arguments:
def addition(a, b):
    return a + b


print(addition(2, 2))  # 4

# The add_integers function is an improvement,
# but you still have to create a list of the arguments ahead of time:
# list_integers is our function parameter
# to make the parameter "list_integers" optional
# we can assign a default value to it => list_integers=[1, 2, 3]


def add_integers(list_integers=[1, 2, 3]):
    total = 0
    for x in list_integers:
        total += x
    return total


# Quick Recap about Python Data Structure
# List:
my_list = [20, 20, 30, 40]

# Set: Python will always filter the "set", using the value one time
my_set = {1, 2, 1, 3, 1, 2, 2, 3}  # 1 and 2 and 3 => total will be only 6!
my_set = {10, 10, 10}  # python will treat {10, 10, 10} as {10}

print(f"the length of my_set is: {len(my_set)}")  # 1
# Try it here:
total = 0
for x in my_set:
    total += x

print(f"total of my_set: {total}")


# Dictionary
my_dictionary = {
    "num1": 10,
    "num2": 10,
    "num3": 10,
    "num4": 10,
}

# a Tuple:
my_tuple = (10, 20, 30, 40)  # 10,20,30,40


# Creating my list of integers:
int_list = [1, 2, 3, 4]
# int_list is our function argument
print(add_integers(int_list))  # 10

# we don't pass any argument
print(add_integers())  # 6

# passing an array:
print(add_integers([10, 20, 30]))  # 60

# passing a tuple
print(add_integers((100, 200, 300)))  # 600

# passing a set
print(add_integers(my_set))  # 10

# passing a set again
print(add_integers({20, 20, 20, 20}))  # 20

# passing a tuple element but without ()
# print(add_integers(100, 200, 300))  # 600
# We will have this error: TypeError: add_integers() takes from 0 to 1 positional arguments but 3 were given

# The solution
# using: *args

# Rename *args to something suitable: integers
# *integers => allowing us to use as many integers as we like when calling the function (not only one)
# this only "one" parameter => takes only one argument
# but with using the "*" => will make this "one" parameter accept many coma seperated arguments


def add_many_integers(*integers):
    total = 0
    for x in integers:
        # As it is a "tuple" you can use the in keyword to iterate
        total += x
    return total


# print(add_many_integers(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 45

# Notice if we don't add the * to our function parameter "integers"
# We will have this error: TypeError: add_many_integers() takes 1 positional argument but 9 were given
# If you don't like to use the *arg: => add_many_integers((1, 2, 3, 4, 5, 6, 7, 8, 9))
my_other_tuple = 10, 20, 30, 40, 50
print(type(my_other_tuple))  # <class 'tuple'>
total = 0
for number in my_other_tuple:
    print(number)  # 10
    print(type(number))  # int
    total += number

print(f"The total of my_other_tuple numeric values is {total}")

# passing a variable of tuple data structure to our function:

# This print will give us an error:
# print(add_many_integers(my_other_tuple))
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

# passing a variable of list data structure to our function:
# let's try to pass => int_list = [1, 2, 3, 4]

# This print will give us an error:
# print(add_many_integers(int_list))
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# This print will give us an error:
# print(add_many_integers([1, 2, 3, 4]))
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'

my_other_tuple = "I", "like", "learning", "Python", "language"
print(type(my_other_tuple))  # <class 'tuple'>
# To double check, let's try to repeat the same code/logic for finding the total:
combine = ""
for x in my_other_tuple:
    combine += x+" "

# I like learning Python language
print(f"the result of my_other_tuple: {combine}")


# We have this function named "concatenate_words"
# that accept any data structure: list, tuple, set, or a dictionary
# and return the total of the values inside any structure
def concatenate_any_words(words):
    # because we are adding string values => we will concatenate them
    # that why the initial of our container has an "empty string"
    result = ""

    # Below we are creating a variable named "data_structure":
    # This "data_structure" could be any one of these data structure type:
    # data_structure: dict
    # data_structure: list
    # data_structure: set
    # data_structure: tuple
    data_structure = words
    # if the words.values() exists (no error) => it means it's a dictionary data structure
    # else => it could another python data structure: list, set, tuple

    # To recap:
    # using isisinstance() function to check if "words" is instance of the class "Dictionary"
    # isisinstance() function => returns either True or False
    # Please refer to our previous lecture
    if isinstance(words, dict):
        data_structure = words.values()

    for arg in data_structure:
        result += arg
        result += " "
    return result


# List (array in JS):
all_words1 = ["Hi", "Hello", "Good morning", "Good evening"]

# Dictionary (JSON in JS):
all_words2 = {
    "greet1": "Hi",
    "greet2": "Hello",
    "greet3": "Good morning",
    "greet4": "Good evening",
}

# Set:
all_words3 = {"Hi", "Hello", "Good morning", "Good evening"}

# Tuple:
all_words4 = ("Hi", "Hello", "Good morning", "Good evening")
# or without ()
all_words4 = "Hi", "Hello", "Good morning", "Good evening"

# Calling/invoking our function
# 1) passing our list
print(concatenate_any_words(all_words1))
# 2) passing our dictionary
print(concatenate_any_words(all_words2))
# 3) passing our set
print(concatenate_any_words(all_words3))
# 4) passing our tuple
print(concatenate_any_words(all_words4))

# All the 4 print statement will output the same message:
# Hi Hello Good morning Good evening
# greet1 greet2 greet3 greet4 <=> we want the keys of the dictionary not its value
# Good morning Hello Hi Good evening
# Hi Hello Good morning Good evening


# use **kwargs

# function uses **kwargs but renamed as **words.
# In this case, we have passed in many strings as named arguments,
# and as this is a dictionary within the function, we have iterated over the dictionary values.
def concatenate_words(**words):
    result = ""
    # As **kwargs is a dict you need to iterate over .values()
    for arg in words.values():
        result += arg
        result += " "
    return result


print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))

# Challenge: Splat! *args & **kwargs Challenge:
"""
Steps:
Define the make_string function:
1. Create a function named make_string, that uses * correctly with a parameter: strings
2. The function should return a string of all the values supplied joined, and separated by a space.
3. The function should return the correct string, no matter how many arguments are passed into the function when it is called, and it will be tested using a different number of arguments

Call the make_string function:
1. Outside the make_string function, declare a variable named my_string
2. Assign the value returned from the make_string function to the my_string variable
3. Call the make_string function with the following values: "Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth".
4. Print the value of the my_string variable to the terminal

Remember when you pass these values into the function, the *strings converts them into a tuple, So you will be working on a tuple inside the function.
 

Define the get_age function:
============================
1. Create a function named get_age, that uses ** with a parameter: data
2. The function should return the value of the age key-value pair passed into the function or return the string: "no age provided" if there is no age key-value pair passed into the function.


Call the get_age function:
==========================
1. Outside the get_age function, declare a variable named pats_age
2. Assign the value returned from the get_age function to the pats_age variable.
3. when calling the get_age function, pass it the following key values pairs name="pat", level=4, age=33, occupation="postman".
4. Print the value of the pats_age variable to the terminal

Remember when you pass these key value pairs into the function, the **data converts them into a dictionary, So you will be working on a dictionary inside the function.
"""
