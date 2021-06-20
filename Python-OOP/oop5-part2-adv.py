# Important Note:
# This file name is oop5-part2-adv (for adding more advanced features)
# just because I used a more complex way to get the uer age exactly based on the day, month, and year!
# In this file the member_age() will give us the user age in days then we can get the user age in years
# but we can import a module named datetime to work with dates as date objects.
# you can read more: https://www.w3schools.com/python/python_datetime.asp

# We can import datatime in this pattern: import module_name
# import datetime

# Or importring the datatime using this pattern: from module_name import class_name, function_name
from datetime import datetime


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

    # This function should "return" the age
    def member_age(self):
        # We can also add a brief "docstring" do describe this class method
        # (to be used by the class object)
        """Return the age of the member in years based on their date of birth"""

        # we don't need to pass any parameter to this function
        # as we will calculate based on the self.dob field value that we received in __init()__
        # Since we are going to work with Dates, We need to import the datetime module
        # First we need to get the today date:
        today = datetime.now()  # instead of typing datetime.datetime.now()
        print(type(today))  # <class 'datetime.datetime'>
        print(today)  # 2021-05-06 12:10:26.709542

        # Strings are Arrays (to review):
        # you can read more: https://www.w3schools.com/python/python_strings.asp
        # Like many other popular programming languages,
        # strings in Python are arrays and each character has its unique index starting with 0
        # So a single character is simply a string with a length of 1.
        # example:
        # my_letters = "abc"
        # print(len(my_letters)) # 3
        # Square brackets can be used to access elements of the string.
        # We can think/assume that my_letters="abc" is like my_letters=["a","b","c"]
        # print(my_letters[2])  #

        # Remember that we input/insert that dob is a string of with the pattern: YYYY-MM-DD
        # Step1: We need to:
        # convert the dob from being a normal string "YYYY-MM-DD" into a date object
        # so from this string "YYYY-MM-DD" we need to extract the "year"
        # We have two ways:
        # 1) using split() method as we did in oop5-part1 file (longer/commonly used way)
        # 2) using string slicing with these symbols [] (shorter way)

        # for more practice, I will use the second way "slicing a string":
        # Slicing String in Python:
        # You can return a range of characters by using the slice syntax.
        # Specify the start index and the end index, separated by a colon, to return a part of the string.

        # Example:
        # greeting = "Hi and Hello, World!"
        # Get the characters for the word "Hello" out of the full text "Hello, World!"
        # We need to know the starting index and the ending index of the word "Hello"
        # from position 7 (staring index) to position 11 (the ending index):
        # The slicing pattern => my_string[ starting_index : ending_index+1 ]
        # this will give us 7 to 11 (12 will not be included)
        # print(greeting[7:12])
        # the output will be "Hello" Notice that the last index 12 will not be included

        # to get only the year from "YYYY-MM-DD",
        # we need to count from index 0 till index 4 (index 4 is not included) => index 0,1,2,3

        # Getting the year from "self.dob"
        dob_year = int(self.dob[0:4])
        # for testing:
        # print(dob_year)  # for example: 1982
        # double check:
        # <class 'int'> which means its a "integer" data type
        # print(type(dob_year))

        # Review:
        # Getting the current year from our date object variable "today":
        # current_year = int(today.strftime("%Y"))
        # Or:
        # current_year = today.year
        # The variable "current_year" is an integer value
        # print(type(current_year)) # <class 'int'>
        # the basic solution
        # age = current_year-dob_year
        # print(f"the member age is: {age}")

        # OR: to be more accurate 100% we can convert the string "YYYY-MM-DD"
        # into a real date object for the member's birth day

        # To do this task, we need to take each value individually:

        # 1. taking the value of YYYY and saving it into a variable: dob_year
        # => to represent the member's year (already done above)

        # 2. taking the value of MM and saving it into a variable: dob_month
        # => to represent the member's month

        # 3. taking the value of DD and saving it into a variable: dob_day
        # => to represent the member's day

        # We can use the same logic we used to get the year for getting the month and the day
        dob_month = int(self.dob[5:7])
        dob_day = int(self.dob[8:10])

        # After getting the 3 values of Year, Month, and Day individually
        # We can convert them into a valid Python object of "Datatime"
        # So we can deduct the current date object from the dob object
        # tinking like object - object :-)

        # Creating a new object named "dob_obj" based on the values of YYYY, MM, and DD
        # The pattern/syntax: our_date_obj = datetime(1972,06,12)
        # Example:
        """
        dob_obj = datetime(1972, 6, 12)
        print(type(dob_obj))  # <class 'datetime.datetime'>
        print(dob_obj) # 1972-06-12 00:00:00
        """

        dob_obj = datetime(dob_year, dob_month, dob_day)
        # print(type(dob_obj)) # <class 'datetime.datetime'>

        # Now we end-up by having two date objects:
        # - the variable "today" of Datetime object => has the value for the current date and time
        # - the variable "dob_obj" of Datetime object => has the value for user's born date (no time)
        # The time is set to: Zeros
        # this will help us to run this formula: today - dob_obj

        # we can easily calculate the difference
        # between today and the dob of the user:
        # we are saying: date_object1 (which is the current date) - date_object2 (The member's DOB)

        # If we know how many days the user has been living
        # we can find his age exactly!

        # To review what we have covered before:
        # We used this formula to find how many days the user has been living:
        # days = age * 365

        # In our current situation:
        # In this case we can use this formula to find how many years the member has been living:
        # age = days / 365
        # The question: How to find how many days the user has been living
        # We CANNOT say: today (the current date object) - self.dob (just a string)

        # Finding the user's age in days:
        # Let's run the basic formula below just for learning:
        age_in_days = today - dob_obj
        print('age in days: ', age_in_days)
        # age in days:  14335 days, 13:04:36.702372
        print(type(age_in_days))  # <class 'datetime.timedelta'>

        # To conclude, in Python: date_object1 - date_object2 will return
        # the difference in days (how many days)
        # the difference time (the current time - the other time)

        # In Math:
        # since in one year we have 365 days
        # age = days / 365
        # so the age in years = the age in days / 365
        # age = age_in_days / 365
        # print(f"Age: {age}") # Age: 39 days, 6:36:42.116642 !!!!!!

        # out of this returned result (value):  16566 days, 13:19:28.071355
        # as programmers, we need only the value of how many days: 14160
        # Solution: using the "days" property => age_in_days.days
        print(age_in_days.days)  # 16566
        age = age_in_days.days / 365  # 45.38630136986301

        # Notice that age will be a float value: 38.794520547945204
        # Let's just make it an integer (whole number)
        # like in JS: parseInt(38.79) => the result will be 38
        # the same in Py: int(38.79) => the result will be 38
        return int(age)


# Creating our object "member"
member1 = Member("Sally Graysons", "1982-02-05")

print(member1.name)  # Sally Graysons
print(member1.dob)  # 1982-02-05
print(member1.first_name)  # Sally
print(member1.last_name)  # You will see an error
print(member1.member_age())  # return the age

member2 = Member("James Dean", "1975-12-28")
print(member2.member_age())  # return the age # 45 (the accurate age)
