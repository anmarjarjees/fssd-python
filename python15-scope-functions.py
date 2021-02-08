# The scope of a variable (Exactly the same concept in any programming language)
# if you define a variable outside any function, this variable will be global
# if you define a variable inside a function,
# this variable can be used/read/recognized only inside its function
# If we declare a variable inside a function,
# then that variable will not be accessible by the global scope
# so is known as the local scope.
# it's global because we created it outside the function in the main script
my_global_variable = "World"


def print_message():
    print(f"Hello {my_global_variable}")


print_message()  # Hello World


def show_info():
    my_local_variable = "Everyone"
    print(f"Hello {my_local_variable}")


show_info()

# below is an error, we are accessing a variable with a local scope
# print(f"Good morning {my_local_variable}")

# below is just an example of using raw_input() function for Python 2.x
# Remember since Jan 2020, Python ver 2.x.x became obsolete
# name = raw_input("Input your name:") # NameError: name 'raw_input' is not defined
# age = raw_input("Input your age:")
# With Python 3.x we use print()

# In JS we know that function can return a value using "return" keyword
# The same in python, we can use "return" to return a value and terminate the function


# Task: Create a function named "find_average"
# This function accepts two arguments (2 numeric values)
# This function will "return" the average of these two variables (numbers)
def find_average(first_num, second_num):
    # avg = (first_num+second_num)/2
    # return avg
    # Like in JS, we can place our formula in return keyword
    return (first_num+second_num)/2
    # print("Sorry, you will not see this message!") # Unreachable code


print(find_average(90, 93))  # 91.5
