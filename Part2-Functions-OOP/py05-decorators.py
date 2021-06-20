# Decorators: A software design pattern
# Is used to alter (modify/change) functions
# By wrapping the function in the decorator

# A decorator: is a way in Python to add new functionality
# to an existing function (or a class) without modifying its structure.
# Decorator == decorates ==> Normal Function


# Normal Function with Normal Call in two steps (creating then calling):
def say_hi():
    print("Hi, world!")


say_hi()


# Applying a Decorator:
# decorators are used to modify the behavior of function or class.
# In Decorators:
# - functions are taken as the argument into another function]
# - and then called inside the wrapper function

# Creating/Defining a decorator

# this first function will represent the "Decorator", let's name it "my_decorator"
# it accepts one parameter that represents the function that we need to invoke
def my_decorator(func):
    def wrapper():  # this second function will represent warpper to wrap our function
        # 1. Printing this text
        print("The function has not been called yet. Let's call it.")
        # 2. Run the function
        func()
        # 3. Printing this text
        print("The function was called and has returned a result.")
    # return the warpper() function
    return wrapper

# Invoking our decorator using the "@" symbol + the decorator name
# Notice if you use the "@" with a decorator name that has not been defined, you will receive this error:
# @my_decorator NameError: name 'my_decorator' is not defined
# decorator can accept argument if it was defined with parameters


@my_decorator
def say_hello():
    # We don't want to modify this function, just keep it as simple as printing "Hello, world!"
    # print("This line will be printed here before the main message")
    print("Hello, world!")
    # print("This line will be printed here after the main message")


say_hello()


# Another Example (Using our two function for converting Fah to Cel or Cel to Fah):


# We have a decorator that defines what units you want to display in our function results
# It is demonstrated with our two functions:
# - to calculate the temp (converting) value in C or F
# - to calculate the temp (converting) value in F or C

# this first function will represent the "Decorator", let's name it "define_units"
# it accepts one parameter that represents the function that we need to invoke
def define_units(measure_unit):
    # this second function will represent warpper to wrap our function
    def decorator_define_units(func):
        # the "func" parameter will represent either either one of these two arguments:
        # in the first call/invoke: the function "convert_cel_fah"
        # in the second call/invoke: the function "convert_fah_cel"
        # testing:
        print(f"type of func parameter inside the function: {type(func)}")
        print(f"the value of func parameter inside the function: {func}")
        # don't forget: In Python function is itself an object
        # adding an attribute (property or method) which is a property named "measure_unit_property"
        # The argument "measure_unit" defined in the decorator can be used to receive our test input
        # In this case the function as an object has a property we can use this: function_name.measure_unit_property
        func.measure_unit_property = measure_unit
        # yes we can add any "property" as we need:
        func.empty_string = ""
        func.is_valid = True

        return func

    return decorator_define_units


@define_units(' Fah Degree')
def convert_cel_fah(cel_temp):  # Convert Celsius to Fahrenheit
    #  the formula: value in F = (value in C * 9/5) + 32
    return (cel_temp + 9 / 5) + 32


@define_units(' Cel Degree')
def convert_fah_cel(fah_temp):  # Convert Fahrenheit to Celsius
    #  the formula: value in F = (value in C * 9/5) + 32
    return (fah_temp + 9 / 5) + 32


# for learning and testing:
# we are calling our function "convert_cel_fah" and access its properties
print(convert_cel_fah.measure_unit_property)
print(convert_cel_fah.empty_string)
print(convert_cel_fah.is_valid)

# For quick demo we are hard coding the values instead of asking the user:
temp = 35  # assuming my value in Cel
print(
    f'The Fah result of {temp} Cel. degree is {convert_cel_fah(temp)}{convert_cel_fah.measure_unit_property}')
# basic output before using a decorator: The Fah result of 35 Cel. degree is 68.8
# final output after using a decorator: The Fah result of 35 Cel. degree is 68.8 Fah degree
# requirements: adding this text at the end of the result "Fah degree"

temp = 45  # assuming my value in Fah
print(
    f'The Cel result of {temp} Fah. degree is {convert_fah_cel(temp)}{convert_fah_cel.measure_unit_property}')
# basic output before using a decorator: The Cel result of of 45 Fah. degree is 78.8
# final output after using a decorator: The Cel result of 45 Fah. degree is 78.8 Cel degree
# requirements: adding this text at the end of the result "Cel degree"

# Decorators Challenge:

# Steps
# 1. Define a function named print_article_title that takes one parameter called title.
# 2. Above where the print_article_title function is defined, add the @add_author decorator
# 3. Inside the print_article_title function return a string that says "Article Title: " and the value of the title argument. The format of the string should be "Article Title: <title>"
# 4. Outside the function
# 5. Create a variable named: result and assign it the return value from calling the print_article_title function and passing it an argument: "Python Decorators"
# 6. print result


# This decorator accepts one parameter which the function to be attached to
def add_author(func):
    """
    Decorator to add string with author information
    to print after decorated function runs
    """
    def wrapper(*args):
        r = func(*args)
        return f"{r}\nBy Code Institute"
    return wrapper

# write your code here

# When we invoke our decorator, we just need to write its name without any argument
# only if the argument is the function itself

# Above the print_article_title function, add the @add_author decorator


@add_author
# Define a function named print_article_title that takes one parameter called title.
def print_article_title(title):
    # return a string that says "Article Title: " and the value of the "title" argument.
    # The format of the string should be "Article Title: <title>"
    # if the title is "Python Fundamental" => it should return: "Article Title: Python Fundamental"

    # either using this return statement:
    # return "Article Title: "+title
    # or using this one:
    return f"Article Title: {title}"


# Create a variable named: result and assign it the return value
# from calling the print_article_title function and passing it an argument: "Python Decorators"
result = print_article_title("Python Decorators")

#  print result:
print(result)
