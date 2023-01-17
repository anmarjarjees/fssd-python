# Object Oriented Programming (OOP)
# In real world,  an architect uses "blueprint" to create identical buildings, houses, cars, etc..
# Classes (Blueprint) and Objects (samples from the blueprint)
# Class is like a template for creating objects
# Class is used by programmer to recreate an object and its functions repeatedly
# object is the instance of class
# object has related data and functions that can be used to manipulate these data
# Python tutor

# Example from our real life:
# anything can be an object like a dog, a cat, a car, a pen, etc...
# any object like a dog can have:
# - characteristics (color, age, name, etc)
# - actions (sleep, run, etc...)
# in the programming language any object like a dog can have:
# (attributes/properties/fields) in Programming => similar to characteristics (specifications) in our life
# methods (functions) in Programming => similar to actions/behaviour in our life


# Python Classes and Objects:
# To read more: https://www.w3schools.com/python/python_classes.asp

# Life Example - Project:
# Let's assume we have a "social club" for our organization
# Create an application to track all our club members:
# So each user/member has his/her own list of info (data) saved in our system

# We will build this simple example using OOP concepts:

# General NOTES About Classes:
# * Like functions, a class does not do anything until it is executed
# * Scope also applies to classes so "global" and "nonlocal" scope have to be taken into consideration
# * A class name should start with a capital letter and should have a docstring => MyMainClass
# * Classes can contain functions (methods) and other statements.

# Make a class named "Member"
# this first example will be a very simple class
# class names start with Capital
class Member:  # <= this is the blueprint to create multiple members
    # In order for the class to work, it does need one line of code at least
    # We just want to test the idea of creating instances (objects) of this class
    # For now, we don't want to add any code (properties/methods), just an empty class
    # in Python classes CANNOT be empty like any other structure, but we can write:
    pass  # just to pass this Python condition/rule of writing something inside our class


# Class Instances:
# ****************
# You can create multiple instances (objects) of a class
# An instance is an individual object of the class in memory
# It exists live in RAM until the point it is removed


# Creating our first instance (member):
# ***********************************
# we will create our first member:
# When you create an instance of the class, it is the initializer code that runs
# That's why it's called "Initialization"
# which is the step to create an instance of a class
# Using a built-in method named "__init__" to be explained more in the next topic
# This method "__init__" will initialize a new object (without any argument)
# In other OOP languages like Java or C#: objectName = new ClassName()
# In python: objectName = ClassName()

member1 = Member()  # We initialized a new member named "member1"
# in OOP: we call member1 an "instance" of the Member class
# or we can say that member1 is an "object"

print(type(member1))  # <class '__main__.Member'>

print(type("ABC"))  # <class 'str'>

print(member1)  # <__main__.Member object at 0x0000015F7F58DFD0>

# Because our blueprint (the class "Member") is empty
# We can attach a properties/function to it on the fly

# Now to attach data to this first object "member1":
# object_name.property_name
# giving member1 a value of fist name then last name:
# Although our Class doesn't have any properties like "first_name" or "last_name"
# We can attach them to our object on the fly:

member1.first_name = "Alex"
member1.last_name = "Chow"
# our Class "Member" is empty we can add anything we want:
member1.age = 47
member1.gender = "m"

# These properties: "first_name" or "last_name" or "age" or "gender"
# which are the data that attached to an object are called "fields"
# Field: The data that is attached to an object
# Till this point, member1 has four fields: first_name, last_name, age, and gender

# now first_name and last_name fields and age are attached to the object "member1"
# let's print them using our normal way the dot notation:
print(member1.first_name)  # Alex
print(member1.last_name)  # Chow
print(member1.age)  # 47
print(member1.gender)  # m

print(member1)  # <__main__.Member object at 0x000001BA0CA74FD0>


# We can't loop through the object directly
# TypeError: 'Member' object is not iterable
"""
for field in member1:
    print(field)
"""

# you can see that we use "snake_case" (lower case with underscore) for the filed names
# as we used with Python variables , it's Python convention

# For practice
# we will create two Py variables with the same names as the member1 fields names:
# notice these are separate values, they are not attached to the member1 object
first_name = "Martin"
last_name = "Smith"
print(first_name, last_name)  # Martin Smith

# We can also change the values of the object's field
# Changing the value of "first_name" field of "member1" object to be "Alexa":
member1.first_name = "Alexa"
print(member1.first_name, member1.last_name)  # Alexa Chow


# There is no limit about how many objects (members) we can create from the Class
# creating another object named "member2"
# and give this new object "members" the first name of "Sam" and the last name "Simpsons"
# member2.first_name = "Sam"
# member2.last_name= "Simpsons"
member2 = Member()


# To summarize:
# Classes (Blueprint) are used to create objects (instances)
# Each object can have different values for the same fields (variables) names

# we will give this member first name and last name using the same fields as member1
# but the new values will be attached to member2
member2.first_name = "Sam"
member2.last_name = "Simpsons"
# we didn't give any age value to this member

print(member2.first_name, member2.last_name)  # Sam Simpsons

# We can attach any field to an object with any data type:
member2.job_title = "Teacher"

member2.favourite_singer = "Frank Sinatra"
# object_name.any_field = any value

# In the example above we have two new different fields
# that have been attached to member1 and member2
# both members have the same fields: first_name and last_name
# But member1 has the age field and the gender field
# while member2 has two different fields: job_title and favorite_singer
print(member2.favourite_singer)
# so if we try to print the wrong field for the object
# we will receive an attribute error:
# print(member1.favourite_singer)
# AttributeError: 'Member' object has no attribute 'favorite_singer'

# If create a new instance with arguments:
# member3 = Member("Sarah", "Grayson")
# TypeError: Member() takes no arguments

# Yes we can use the same idea of creating Member class but with a "dictionary" variable that contains keys and values:
# Example:
first_member = {
    'first_name': 'Martin',
    'last_name': 'Smith',
    'address': "Toronto",
}
# But using classes can give us more extra features as we will see the next files
