# Functions
# We’ve used plenty of different Py built-in functions at this point,
# like print(), input(), range(), and len()
# We learn to create our own custom functions

# In JS:
# function printMessage() {
#     console.log("Hello World!");
# }
#
# printMessage()

# In Py: we also need to create the function then call it later
def print_message():
    print("Hello world!")


# call/run the function:
print_message()  # Hello world!
print_message()
print_message()
print_message()

# Parameters and Arguments
# We might need our functions to perform actions on specific pieces of data.
# In this case, we would use arguments to pass that part of data to the function


def show_content(name):
    print(f"Hello {name}!")


show_content("Alex")
show_content("Martin")

# show_content() # error because this function needs an argument
# TypeError: show_content() missing 1 required positional argument: 'name'

# another example:
# Task: create function to receive the value of user's age
# if the user's age is equal to or greater than 18 print "Go to classroom#18"
# else print "Go to classroom#12"

# we can set a default value for age argument in case if we didn't pass any value to the function
# this default value of 10 will be used if the user didn't pass any value


def user_age(age=10):
    if age >= 18:
        print("Go to classroom#18")
    else:
        print("Go to classroom#12")


# saving our time by hard coding the age value
your_age = 20
user_age(your_age)  # Go to classroom#18

# below we are not passing any value, the age will be equal to 10 (by default)
user_age()  # Go to classroom#12

# Because Python is weakly data type
# user_age("How are you") # age = "How are you"
# TypeError: '>=' not supported between instances of 'str' and 'int'
# Python can't solve this question: is How are you >= 18 ???
