class Member:
    # *********************************************
    # NOTE: Class Attribute vs Instance Attribute
    # Class Attribute:
    # ----------------
    # a variable created within (inside) the class,
    # but outside the constructor function (__init()__),
    # it is shared between (can be accessed by) all objects/instances of this class

    # Instance Attribute:
    # -------------------
    # a variable created within within the constructor function (__init()__),
    # An instance attribute is only accessible from the scope
    # of an object instantiated from the class scope
    # ******************************************************************

    # we are modifying Python Class hidden built-in function (method) named: __init()__
    # We are passing the argument "title" with a default of just an empty string
    def __init__(self, full_name, dob, title=""):
        # again: self.name and self.dob are just a variable for our class
        # any variable we create inside a class using the keyword "self" can be called "Field"
        self.name = full_name  # self.name will be the full name of the member
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title
        # for fun:
        self.any_thing = "I don't know!"

        # Our Task:
        # Create two class fields (variables inside a class):
        # one is named "first_name" to get the member's first name
        # second one is named "last_name" to get the member's last name
        # Remember that we have only the full name of any member
        # saved into this field: self.name
        # We cannot use these assignment:
        # self.first_name = name
        # self.last_name = name

        # We need to customize this init function to:
        # split the full name into two parts
        # assign the first part to a field named "self.first_name"
        # assign the second part to a field named "self.last_name"

        # After getting the user full name,
        # let's try to split it into first and last name
        # Adding more feature to the same __init__() method
        # Extract first name and last name (split the first name from the last name):
        # We will use a built-in method to split a text named split()
        # This method works like split() in JavaScript and explode() in PHP
        # Remember that this string method returns a list (an array)
        # and each text value will be placed on its unique index!!!!
        # my_string.split(' ')

        # Just to review split() quickly:
        # number ="1,2,3,4,5"
        # remember that split() returns a list
        # number_list = number.split(",")
        # number_list = ["1","2","3","4","5"]

        # example: full_name = "Alex Chow"
        # the delimiter is just a space between Alex and Chow

        # Note:
        # name_parts is just a temporary local variable to be used within this method ONLY
        # It's NOT a class field and that's why we don't need to add self to it
        # We don't want any one to override this variable "name_parts"
        # This variable will take its value out of the split() method
        name_parts = full_name.split(' ')
        # for testing:
        print(name_parts)  # ['Sally', 'Graysons']

        # Python will split the text based on the space in between the first and the last name
        # name_parts = [ 'The value of the first name', 'The value of the last name' ]
        # example:
        # full_name= 'Martin Smith'
        # we use: name_parts = full_name.split(' ')
        # name_parts = ['Martin','Smith']
        # 'Martin' will be in index 0
        # 'Smith' will be in index 1

        # based on the array (list) named "name_parts"
        # we will create the new fields for this class:
        # now using the same keyword "self" to create two new object fields:

        # Look at this mistake:
        # any variable we declare inside any function which inside our class
        # will become a local variable to be used only within the same function
        # which we cannot access its value outside this function __init__():
        # first_name = name_parts[0]
        # last_name = name_parts[1]

        # Solution: to make these two local variables global
        # We can use the same idea by adding "self" keyword
        # self.first_name
        # self.last_name
        # index 0 will have the first name value
        self.first_name = name_parts[0]

        # To summarize
        # Any class field that is written inside a function (method):
        # has to start with the keyword "self" then "." => self.
        # now for learning let's try to omit the keyword "self"
        # from the last_name field to see what will happen
        # So below we are just assign the value of the last name into a simple python variable named "last_name"
        # Which can only be accessed within the method body (a local scope variable)
        # index 1 will have the first name value
        last_name = name_parts[1]
        # self.last_name = name_parts[1]

    # Examples of "Class Attribute"
    # Note:
    # below "info" is a "global" class variable
    # (created inside the class but NOT inside any method)
    # which means it's not written or declared inside any Class function
    # for this reason we CANNOT attach the keyword "self" to it
    # but this class variable (field) "info" can be accessed with the class object
    # For now, let's just assign a fixed value (string) for learning purpose
    info = "CBC Club's Member"


# Creating our object "member1"
member1 = Member("Alex Chow", "1975-10-22")
print(member1.name)  # Alex Chow
print(member1.dob)  # 1975-10-22
print(member1.info)  # CBC Club's Member

# Let's try if we can change its value:
member1.info = "CP24 Club's Member"
print(member1.info)  # CP24 Club's Member


# Creating another object "member2"
member2 = Member("Sally Graysons", "1982-02-05")
# we can test:
print(member2.name)  # Sally Graysons
print(member2.dob)  # 1982-02-05
print(member2.info)  # CBC Club's Member


# Creating another object "member3"
member3 = Member("Kate Graysons", "1980-07-05", "Job Developer")
# we can test:
print(member3.name)  # Kate Graysons
print(member3.dob)  # 1980-07-05
print(member3.job_title)  # Job Developer

# we can test:
print(member2.name)  # Sally Graysons
print(member2.dob)  # 1982-02-05
print(member2.info)  # CBC Club's Member

print(member2.first_name)  # Sally

print(member2.last_name)  # You will see an error
# AttributeError: 'Member' object has no attribute 'last_name'
# Because we didn't attach last_name field (attribute) to the object (itself)
# by using the keyword "self"
# Solution: We do need to attach the keyword "self" to the variable last_name
# to make it an official true "global" object field (attribute)

# **********************************************************************************
# ************ But I will leave the error in this page as a reminder :-)************
