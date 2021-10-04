# Python Class Inheritance:

# For more details: https://www.w3schools.com/python/python_inheritance.asp
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called "base" class.
# Child class is the class that inherits from another class, also called "derived" class.

# To recap: before talking about Inheritance in Python
# Notice below based on what we have learned/going to learn more about modules and packages:
# we can import datetime using this way (we commented it):
# import datetime

# We can import the method/object datetime from the module datetime
# so we can just type "datetime" instead of keep typing "datetime.datetime"
from datetime import datetime

# class Member is the "parent" class
# Parent class is the class being inherited from, also called "base" class.


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

    def member_age(self):
        # We can also add a brief "docstring" do describe this class method
        # (to be used by the class object)
        """Return the age of the member in years based on their date of birth"""
        # Notice that we don't have to write: today = datetime.datetime.now()
        # we can just write:
        today = datetime.now()
        dob_year = int(self.dob[0:4])
        dob_month = int(self.dob[5:7])
        dob_day = int(self.dob[8:10])
        dob_obj = datetime(dob_year, dob_month, dob_day)
        age_in_days = today - dob_obj
        age = age_in_days.days / 365
        return int(age)

    # let's add another method for just printing the member full info:
    # - the member first name
    # - the member last name
    # - the member date of birth
    # - the member job title if it's exist
    def print_main_info(self):
        print("\n******************")
        print("Member Information:")
        print("******************")
        # Quick Test for accessing the method "member_age()":
        # print(self.member_age())
        # we can use the f-string to format our output
        print(f"First Name: {self.first_name}")
        # or use the comma:
        print("Last Name: ", self.last_name)
        # or use the concatenation:
        # Notice that we need to add self. before calling any class method
        print("Date of Birth: " + self.dob +
              ". Age: " + str(self.member_age()))
        if self.job_title != "":
            print("Job Title: ", self.job_title)


# Creating a basic (derived/child/sub-class) class "Basic_Member" from the base (parent) class "Member"
# We still need to follow the naming convention by starting with Uppercase:
# We want to let this class "Basic_Member" inherits all the contents of the base class "Member"
# This child class can use (access) all the fields and methods from the parent class
#
# A "sub class" inherits all its attributes (properties and methods)
# from a "parent class" which also include the initializer method

class Basic_Member(Member):

    # we need to print the original info and an extra info about the membership
    def print_full_info(self):
        # If your class/function/if block/for loop/etc... is completely empty (doesn't have any code)
        # We have to add the keyword "pass" in Python

        # Before printing the Membership type, we still need to print all the other member's info
        # We need to use the same method "print_main_info(self)" from the parent class
        # To print the common/shared information of all the members for the following fields:
        # the full name, date of birth, and job title
        # Solution:
        # we need to call the print_main_info() in the parent class
        # by adding an extra feature which to print the membership type

        # we can call/access/invoke a method from the parent class using one these syntax:
        # >> Base_Class_Name.method_name(self)
        # >> self.method_name()

        # Example of using the first way of calling a method from the parent class:
        # NOTE: Don't forget to add the mandetory parameter "self":
        # If you don't add it: TypeError: print_main_info() missing 1 required positional argument: 'self'
        Member.print_main_info(self)

        # Then we can add one line for printing the membership:
        # We want to print the Membership Type:
        print("Membership Type: Basic")


class Standard_Member(Member):
    def print_full_info(self):
        # Example of using the second way of calling a method from the parent class:
        self.print_main_info()
        # We want to print the Membership Type:
        print("Membership Type: Standard")


class Premium_Member(Member):
    def print_full_info(self):
        Member.print_main_info(self)
        # We want to print the Membership Type:
        print("Membership Type: Premium")


member1 = Basic_Member("Sally Graysons", "1982-02-05", "Graphic Designer")

# Now let's create our objects:
# Creating our objects "member1, member2, member3"
member1 = Basic_Member("Sally Graysons", "1982-02-05")
member2 = Standard_Member("Alex Chow", "1972-09-23")
member3 = Premium_Member("Martin Smith", "1974-04-03")

# We have to call two functions to print all the information!
# member1.print_main_info()  # print the initial field, when we initialized our object
# member1.print_full_info()  # print the membership type

member1.print_full_info()

member2.print_full_info()

member3.print_full_info()

# More printing using commas (no +) :-)
# with commas no worries about adding str() for numeric values
print("**********************************************")
print("The age of member1:", member1.first_name, "is",  member1.member_age())

print("**********************************************")
print("The age  of member2:",  member2.first_name, "is",  member2.member_age())

print("**********************************************")
print("The age  of member3:",  member3.first_name, "is",  member3.member_age())
