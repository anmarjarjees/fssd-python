# Scope - Local vs Global Variables:
# By defining variables inside or outside functions
# The scope of a variable (Exactly the same concept in any programming language)
# if you define a variable outside any function, this variable will be "global"* (Treat this sentence carefully)
# if you define a variable inside a function,
# this variable can be used/read/recognized only inside its function
# If we declare a variable inside a function,
# then that variable will not be accessible by the global scope (outside the function)
# so is known as the local scope (this variable can be accessed/used locally inside its function).
# it's global because we created it outside the function in the main script


my_global_variable = "World"


def print_message():
    # yes we can access the variable  "my_global_variable"
    print(f"Hello {my_global_variable}")


print_message()  # Hello World


def show_info():
    my_local_variable = "Everyone"
    print(f"Hello {my_local_variable}")


show_info()

# below is an error, we are accessing a variable with a local scope
# print(f"Good morning {my_local_variable}")
# NameError: name 'my_local_variable' is not defined

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

# Enclosing Scope:
# In Python (like other programming languages) you create functions inside functions,
# so a local scope variable in a parent function is also available in the child function.
# If you use the variable from the parent function in the child function,
# then the scope is neither local nor global.
# A Python variable scope that is neither local nor global is referred to as nonlocal.
# This is called the "enclosing scope"

# Examples:
# Creating a function that accepts two parameters:
# 1) a list (array) of numbers
# 2) a numeric value of 1 or 2:
# -- if it's "1" => return the total
# -- if it's "2" => return the average

# the function can return the total or the average the numbers based on the user choice:


def total_avg(any_list, formula=1):
    # Creating a "nonlocal" variable named "result"
    # this variable will hold the final result of either the total or the average
    result = 0  # in python we can't declare a variable without the assignment operator and a default value
    # In JavaScript we can do it => let result;
    # So the "result" has what's called "Enclosing Scope"

    # Creating an inner (child) function just to change the value of "result" and return it to the main function
    def total():
        # result = 0
        # OK to print the "result"
        print(f"Test the value of result: {result}")
        # we can access the variable "result" that was declared in the parent function
        # inside the child function
        total = result  # OK to receive the value of the "result"
        # the normal/basic logic for finding the total using for loop:
        for number in any_list:
            # using this formula: result += number
            # UnboundLocalError: local variable 'result' referenced before assignment
            total += number
        return total

    # going back to our main (parent) function:
    if formula == 1:
        # calling our child function => total()
        result = (total())
    elif formula == 2:
        # calling our child function again => total()
        result = (total()/len(any_list))
    else:
        result = None  # similar to the keyword "null" in JavaScript

    return result


my_exams = [90, 89, 92, 88, 91]
# finding the average:
print(f"average: {total_avg(my_exams, 2)}")  # average: 90.0

my_items = [12.75, 10.67, 5.29, 3.61]
# finding the total:
print(f"total: {total_avg(my_items, 1)}")  # total: 32.32

my_numbers = [9, 6, 12, 11, 10, 8]
print(total_avg(my_numbers, 3))  # None

# The same logic in JavaScript:
"""
// The Code in JavaScript: Use PythonTutor: http://pythontutor.com/

function total_avg(any_list, formula=1) {
  
  let result = 0;
  
  function total() {
    for (let i=0; i<any_list.length; i++) {
      result += any_list[i];
    }
    return result;
  }
  
    if (formula == 1) return (total())
    else if (formula == 2) return (total()/any_list.length)
    else return null
  
}

let my_exams = [90, 89, 92, 88, 91];
console.log("Average: "+ total_avg(my_exams, 2))

let my_items = [12.75, 10.67, 5.29, 3.61];
console.log("Total: "+ total_avg(my_items))

console.log("Total: "+ total_avg(my_items,3))   
"""
