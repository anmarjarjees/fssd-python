# The "global" Keyword and the "nonlocal" Keyword
# *******************************************
# The variable scope is "local" by default
# You can specify otherwise with a python keyword
# Use "global" or "nonlocal" keywords when defining variables

# IMPORTANT NOTE ABOUT VARIABLES INSIDE/OUTSIDE FUNCTIONS:
# ********************************************************
# In many or most other programming languages variables are treated as global if not otherwise declared,
# Python deals with variables the other way around. They are "local", if not otherwise declared.

# Example to clarify:
# If you access a variable declared outside a function (in the main script) within a function
# and try and reassign its value.
# If you then access the global variable outside the function,
# it will still have its original value rather than the new one reassigned within the function

# declaring a new variable outside the function
my_test_var = 10

# Creating my_function()


def my_function():
    # Two times printing:

    # 1) printing before the assignment operation:  my_test_var = 7
    # Notice the print() statement below will generate an error:
    # print(f"Printing the original value my_test_var inside my_function(): {my_test_var}")
    my_test_var = 7
    # UnboundLocalError: local variable 'my_test_var' referenced before assignment

    # The solutions:
    # either placing the print() statement after the assignment statement with the value of 7
    # or remove the assignment statement => my_test_var = 7
    # Yes, unfortunately this the fact in Python! (Not like other programming languages)
    # print(f"Printing the original value my_test_var inside my_function(): {my_test_var}")

    # 2) printing after the assignment operation:  my_test_var = 7
    print(
        f"Printing the new value my_test_var inside my_function(): {my_test_var}")


# calling my_function()
my_function()  # 7


print(f"Printing my_test_var outside my_function(): {my_test_var}")  # 10
# Yes, In python, the variable will have its original value outside the function!


average = 0

# 1. Create our function


def two_numbers_average(num1, num2):
    average = (num1+num2)/2
    print(f"The average: {average}")  # The average: 91.0


# 2. invoke/call our function
two_numbers_average(90, 92)

print(f"The average: {average}")  # The average: 0

# In JavaScript is different
# because we are using let/var when we declare a NEW variable and identify its scope: local/global
"""
// Global varaible "average"
let average = 0;

function twoNumbersAverage(num1, num2){
    average = (num1+num2)/2
    // return average;
}

// calling our function that will change
// the value of our global varaible "average"
twoNumbersAverage(90,92)

// average = twoNumbersAverage(88,82) // undefined

console.log(average)
"""

# Another Example:
# declaring a variable in the global scope (outside a function) named "can_access" of boolean data type
# with the value of "False"
can_access = False


def access_validation():
    age = int(input('Enter your age: '))
    if age >= 18:
        # We may think this is updating the global variable can_access,
        # but its not as it is now considered a local variable [Yes this python life :-)]
        can_access = True
        # returning a text message
        return('You are old enough to enter')
    else:
        return('You are too young, you may not enter')


# calling our function
# access_validation()

# calling our function and its returned will be assigned to x
status = access_validation()
print(status)

# calling our variable
print(f"can_access: {can_access}")  # Will still print out False

# The two solutions for having the new assigned value replacing the old one:

# First Solution: our normal way by using the keyword "return" to return the new value inside the function
# to the main code outside the function (no need to demonstrate this way)

# Second Solution: using keywords "global" and "nonlocal" to state which scope is to be used

# setting a value for the global varaible (declared outside a function) "can_register" to "False"
can_register = False

# In this second example:
# if you input an age greater than or equal to 18
# the global variable "can_register" changes to True even in the global scope
# This is because the "global" keyword has been used


def update_access():
    global can_register
    age = int(input('Enter your age: '))
    if age >= 18:
        # The global keyword is used
        can_register = True
        return('You are old enough to enter')
    else:
        return('You are too young, you may not enter')


update_access()
# will now print True if an age >= 18 is entered
print(f"can_register: {can_register}")

# The "global" Keyword Challenge:
# Steps:
# Using what you have learned about python variable scope
# to fix the code so that the global test_passed variable is updated to True when the code runs,
# and True is printed to the terminal:
test_passed = False
answer = "friend"


def speak_friend_and_enter():
    if answer == "friend":
        test_passed = True


speak_friend_and_enter()
print(test_passed)  # False


# The "nonlocal" Keyword:
# *********************

# Example1: Before using nonlocal
# We will create two functions: the parent function and inside we will have the child function

def which_scope_example1():
    user_age = 49  # local variable user_age
    # Creating our child function inner_scope()

    def inner_scope_function():  # this child/inner function is declared locally inside "which_scope_example1"
        # Issue when we try to run this line => we will receive an error (as we had in the previous lecture)
        user_age += 1  # user_age = user_age + 1
        # UnboundLocalError: local variable 'user_age' referenced before assignment
        print(user_age)

    # Calling our inner/child function:
    inner_scope_function()


# Calling the main/parent function inside the main script:
# I had to comment this line to skip the python error
# which_scope_example1()

# The issue again that we have in Python, and how to fix it using the keyword "global":
test = 1


def testing():
    # UnboundLocalError: local variable 'test' referenced before assignment
    # Python treats the variable "test" as it locally declared
    global test
    # We cannot use the keyword "nonlocal":
    # => we only have one parent/main function
    # => and the variable test was declared with its initial value outside the testing() function
    # using this sentence: nonlocal test
    # SyntaxError: no binding for nonlocal 'test' found

    # We need to inform Python that this variable "test" is "NOT a "local variable"
    # as we already declared it and initialize it with a default value of 1
    # outside the function and in the main script (code)
    # so we can simply use the keyword "global"
    test = test + 1
    # we can use:
    return test


print(testing())  # 2

# Example2: after using "nonlocal" keyword

# Create our function

student_mark = 88


def which_scope_example2():  # The parent function
    # local variable user_age
    # Creating our child function inner_scope()
    user_age = 49

    def inner_scope_function():  # this child/inner function is declared locally inside "which_scope_example2"
        # Issue when we try to run this line => we will receive an error (as we had in the previous lecture)
        # We need to inform Python that this variable "test" is "NOT a "local variable"
        # as we already declared it and initialize it with a default value of 49
        # outside this child function but inside the main/parent function
        # so we can simply use the keyword "nonlocal"

        # Before assign any value/formula to the varaible "user_age":
        nonlocal user_age  # No longer an issue because of this
        user_age += 1  # user_age = user_age + 1
        # UnboundLocalError: local variable 'user_age' referenced before assignment
        print(user_age)

        global student_mark
        # nonlocal student_mark (this will not work in this case)
        student_mark += 1  # student_mark = student_mark + 1
        print(f"Your mark is: {student_mark}")
        # UnboundLocalError: local variable 'student_mark' referenced before assignment
        # The solution for this: global or nonlocal

    # Calling our inner/child function:
    inner_scope_function()


# Notice that We CANNOT call this child function globally
# Can be called/invoked within its parent function only:
# inner_scope_function()
# Error: NameError: name 'inner_scope_function' is not defined

# Calling our main function
which_scope_example2()  # 50 and # Your mark is: 89

# The "nonlocal" Keyword Challenge:
# Steps:
# In the code provided the age variable is defined on line 2,
# and then updated on line 4 inside the become_adult function.
# However, because of Python variable scope, the current code throws an UnboundLocalError
# Use what you have learned about local scope in this lesson
# to fix the error so that the age variable in the outer function is updated correctly to 21
# when the code runs.
# This requires only adding a line of code and not changing any of the code already supplied


def outer_function():
    age = 10

    def become_adult():
        age = age + 11

    become_adult()
    return age


result = outer_function()
# print(result)
# UnboundLocalError: local variable 'age' referenced before assignment
