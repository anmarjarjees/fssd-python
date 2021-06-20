# A date in Python is not a data type of its own,
# but we can import a module named "datetime" to work with dates as date objects.
# Module In Python Language => A Python file that contains set of libraries/functions
# you can read more: https://www.w3schools.com/python/python_datetime.asp
# Or Python Docs: https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime
# Please check the end of this file for more examples about using datetime
# We need to import this module "datetime"
# for some manipulations inside member_age(self) function

# To recap, we have seen two different ways (will be explained later in more details):
# import module_name
import datetime

# from module_name import function_name1 (library_name, object_name), function_name2, etc...
# from datetime import datetime


class Member:
    """Member Class is for accepting the following member info:
    - full_name: The Member Full Name (Mandetory)
    - dob: The Date of Birth YYYY-MM-DD (Mandetory)
    - title: The Job Title (Optional) and it's empty by default
    """

    def __init__(self, full_name, dob, title=""):
        self.name = full_name  # self.name will be the full name
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title

        # Python will split the text based on the space in between the first and the last name
        name_parts = full_name.split(' ')
        # index 0 will have the first name value
        self.first_name = name_parts[0]
        self.last_name = name_parts[1]  # index 1 will have the last name value

    # Adding another method (behaviour) to our class "a custom method: created by us (developers)":
    # This method should "return" the member age
    # so we can name it "member_age()" for example
    # This method should return the user age in "Years" based on his/her date of birth:
    # Notice that any method (function) we write inside a class
    # has to have the argument "self" at least
    # If you don't put self => Error ==> Method has no argumentpylint(no-method-argument)
    def member_age(self):
        # We can also add a brief "docstring" do describe this class method
        # (to be used by the class object)
        """Return the age of the member in years based on their date of birth"""

        # For testing:
        # print(dob) # NameError: name 'dob' is not defined
        # we need to add the keyword "self"
        # print (self.dob)

        # The logic (algorithm) for finding the person age:
        # the person age = the current date - his/her date of birth => (2021-05-06) - (1972-12-05) !!
        # to make it very simple: age = the current year - birth year => (2021) - (1972)

        # another example:
        # if the user was born in 1975
        # to find his age, we will use this formula: the current year (2021) - 1975

        """
        if use ==> import datetime
        we have to write => module_name.library/function_name
        datetime.datetime.now()

        if use ==> from datetime import datetime
        datetime.now()
        """

        # today = datetime.now()

        # datetime.datetime.now() => YYYY-MM-DD HH:MM:Seconds:M.Seconds
        # specifying the module name then the library/function name
        today = datetime.datetime.now()
        # the variable "today" will be point to the current data object

        # print(type(today))  # <class 'datetime.datetime'>
        # print(today)  # 2021-05-06 10:50:25.955543

        # Remember that we assumed that dob is a string with the pattern: YYYY-MM-DD
        # We need to take "YYYY" that represent the year only
        # from the full dob string "YYYY-MM-DD"

        # For example: self.dob = "1982-02-05" => we need to get only "1982"
        # We need to take "YYYY" that represent the year only
        # from the full "dob" string value "YYYY-MM-DD"
        # We want to take only the value of "1982" out of the full string "1982-02-05"
        dob_parts = self.dob.split('-')
        # for testing:
        # print(dob_parts) # ['1982', '02', '05']

        # The formula: the user age = The current year - the year they born
        # Based on Python docs:
        # remember that today is datetime object that has many attributes (properties) and methods
        # we can use the "year" property of our date object to return the current year:
        # the syntax: our_date_object.year

        # for testing and learning purpose:
        # print("printing the date properties")
        # print(today.time())  # 11:02:06.314691
        # weekday (0 = Monday)
        # print(today.weekday())  # 3
        # print(today.year)  # 2021

        # We will use:
        # >> "today.year" to get the current year
        # >> dob_parts[0] to get the value of index 0 which is the year => '1982'
        # We have the value of 1982 as as a string '1982'

        # The following formula will give us this error:
        # age = today.year - dob_parts[0]
        # TypeError: unsupported operand type(s) for -: 'int' and 'str'
        # How can python find : 2021 - '1982' !!!!!
        # We need to use int() to prevent this error
        age = today.year - int(dob_parts[0])

        return age


# Outside our class "Member":
# Creating our objects member1, member2, and member3
member1 = Member("Sally Graysons", "1982-02-05")  # YYYY-MM-DD
member2 = Member("Martin Smith", "1972-12-05")
member3 = Member("Alex Chow", "1975-08-01")

# Now I want to know the age of each member (print them):
print(member1.member_age())
print(member2.member_age())
print(member3.member_age())

print("******************")
print(member1.name)  # Sally Graysons
print(member1.dob)  # 1982-02-05
print(member1.first_name)  # Sally
print(member1.last_name)  # Graysons
print(member1.member_age())  # return the age

# using f-strings to print the values with other text:
print(
    f"One of our members is {member1.name} and his/her date of birth is {member1.dob}. So, his/her age is {member1.member_age()}")

print(
    f"One of our members is {member2.name} and his/her date of birth is {member2.dob}. So, his/her age is {member2.member_age()}")

print(member2.member_age())  # 48
# We can override the value of dob for member2 using just a simple assignment operator:
member2.dob = "1974-10-07"
print(member2.member_age())  # 46

member3 = Member("James Dean", "1975-12-28")
print(member3.member_age())  # return the age # 46 (not accurate at this time)

print("************************ Quick Datetime Tour *************************")
# Just for quick learning about datetime object in Python:
# we can use the datetime() class (constructor) of the "datetime" module.
today = datetime.datetime.now()  # 2020-07-10 12:07:00.549117

# The date contains year, month, day, hour, minute, second, and microsecond.
# For testing:
print("today is: ", today)  # today is:  2020-07-10 12:07:00.549117
# Example: I don't want to display the ful date and time!
# We want only display the date in this format =>

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format,
# to specify the format of the returned string:
# print("today is: ", today.strftime("%B")) # May

# 2020-July-10, Thursday
# today is:  2021-May-06, Thursday
print("today is: ", today.strftime("%Y-%B-%d, %A"))


# Another example (your task): May 6, 2021 Thursday
