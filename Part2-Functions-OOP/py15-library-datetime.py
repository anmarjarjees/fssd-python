# datetime:
# built-in library
# Provides classes for manipulating dates and times

# NOTE:
# There is no date data type in Python.
# The built-in datetime library allows you
# to manipulate dates and times.

from datetime import datetime

# Getting the current date and time
x = datetime.now()

# Display the current date and time
print(x)  # 2022-01-20 17:21:13.839093

# The date contains a year, month, day, hour, minute, second and microsecond.
# The library contains methods to access that data.
print(x.year)  # 2022

# strftime() method:
# to get a readable string from the datetime object.
# this method takes a parameter format
# to return the string as you would like to display it to your user.
print(x.strftime("%A"))  # Thursday

# NOTE:
# We can also access date information with python using datetime instance methods
# such as date() and time():
the_date = datetime.now().date()
print(the_date)  # 2022-01-20

the_time = datetime.now().time()
print(the_time)  # 17:21:13.842096

# Challenge: datetime
# Steps:
# 1. Declare a variable named today
# 2. Use the relevant datetime method(s)
# to get the current date (year, month and day) and assign it to the today variable
# 3. Print the value of the today variable to the terminal.
