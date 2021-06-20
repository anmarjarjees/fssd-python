# Class More Features:
# Fields (Just simple python variables inside the class)
# Methods (just python functions inside the class)
# Initialization (the step to create an instance of a class)
# So a simple class can contain fields/properties and methods (functions inside class)
# Notice that Class can have a help/descriptive text to describe it (for later) so stay tuned :-)
class Member:
    # Any class has a "hidden" function (that doesn't have any parameters) named: __init__(self)
    # the double underscores (before/after) __ it's a built-in python function
    # This hidden function will run automatically when we create a new object (instance) of that class
    # This hidden function (hidden method) is being called to initialize and object from this class
    # and that's why it's called __init__ for initialization

    # The first feature to add/modify is: init method
    # init = initialization
    # The __init__ method is known:
    # as a dunder, double-underscore or magic method, and these tend to be used on classes mainly
    # They use double underscores so as not to conflict with your own defined classes

    # The initialization method is also called "Constructor" in other OOP languages like C# or Java
    # An __init__() method on its own would simply create an empty class object
    # as we did in the first example "oop1.py"
    # But it can be used to initialize the properties of the instance (set the values for a class member)
    # to create/add (modify) this method in python we use the keyword init with double underscore before and after: __init__()
    # Notice that this method are being called (invoked) automatically when we create a new instance of a class
    # This initialization method "__init__()" has two parameters (arguments)
    # The first parameter is mandatory:
    # self ==> a reference to the new created object (a reference to the object itself)
    # The "self" keyword associates functions and properties with a class
    # The other parameter(s) (arguments) are optionals: below we are adding only two: full_name and date of birth (dob)

    # Very Important Rule:
    # ********************
    # Any method (function) we create inside a class
    # HAS to have an argument named "self" (it's mandatory)
    # "self" is a python keyword that refers to the object itself
    # In JavaScript we have used the keyword "this" that refers to the this object

    # def __init__() is like our example function Member(full_name,dob) in JS
    def __init__(self, full_name, dob):
        # the moment we create (initialize) a new object (instance)
        # we can insert to this object the full_name field and dob field in just one line!

        # inside this method, we need first to store these values to fields in our object
        # we have to use the pattern: self.field_name = the function parameter (the argument)

        # Properties (Fields):
        # ----------
        self.name = full_name  # one single string value that contains both first and last name
        self.dob = dob  # YYYY-MM-DD

        # Be carful that self.dob on left-hand side is the object (class) field
        # this field is used to store (receive) the dob value on the right-hand side
        # while the dob on right-hand side is the value we provide (we pass to the __init()__ method)
        # when we create a new object (new Member)
        # You can think that "self" is like "this" in JavaScript

    # And we can add/create our own function (methods) to this class
    # In any programming language, function inside a class is named "method"
    # So a method is a function that is within a class or object
    # Notice below, our custom method "print_name()" has to have the parameter/argument "self"
    # If we don't put "self" we will receive this error "Method has no argument"
    # Method in Coding Like Behaviour in Life:
    # ----------
    def print_name(self):
        # print(self) # <__main__.Member object at 0x000002630A604FD0>

        # print the value of the "name" field for the object itself:
        print(self.name)

    # Just for more practice:
    def hello(self):
        print("Hello World!")

    # Notice we used in oop1.py:
    # pass
    # because our class was empty


# Now our class is done, it's the time to create a new object of that class:
# Very Important Note:
# In this time when we create an object we must specify two values (arguments) inside the paranthesis
# The reason why is because we modified the default autorun method "__init__(self)"
# We changed this function (method) signiture to make it accepting two parameters as required values
# So we CANNOT just create a new object by typing member1 =Member() as we did in app1.py, we will receive an error
# For testing:
# this code will generate an error of missing the two values for full_name and dob
# member1 = Member()
# TypeError: __init__() missing 2 required positional arguments: 'full_name' and 'dob'

# We are initializing a new member (an instance of class Member)
member1 = Member("Sally Graysons", "1982-02-05")
# we can test:
print(member1.name)  # Sally Graysons
print(member1.dob)  # 1982-02-05

member2 = Member("Kate Willson", "1980-12-15")
print(member2.name)  # Kate Willson
print(member2.dob)  # 1980-12-15

member1.print_name()  # Sally Graysons
# member1 = Member("Alex Chow","2000-11-10")

member2.print_name()


# Notice that hello() is a normal function here
# hello() is a function that belongs to our class "Member"
# So hello() is a "method"
# based on what have learned before: object_name.method_name()
member1.hello()  # Hello World!
member2.hello()  # Hello World!

# calling a function (method) named display() that we don't have in our class!!
# member2.display()
# AttributeError: 'Member' object has no attribute 'display'


# Q) What if we want to print the first name or the last name only:
# A)
# print(member1.first_name)
# - the answer error: AttributeError: 'Member' object has no attribute 'first_name'
# - To fix it we need to add these two fields/attributes/Class variables:
# >> first_name
# >> last_name
# to our class

# - yes we can add these two fields to our class
# or we can attach them on the fly to any object (Bad Way!)
# - So below is a kind of mess! we will fix it in the next file
member2.first_name = "Martin"
member2.last_name = "Martinos"
print(member2.first_name)  # Martin
print(member2.last_name)  # Martinos

member2.print_name()  # We will not see "Martin Martinos" we still have "Kate Willson"

# Q) How can we get the first name and last name out of the full name?
# You can check the next file "oop3.py"

# NOTE: The same rules and concepts that we have learnt before:
# The dot notation can also be used to modify the properties of objects
# with the use of the assignment operator
# Example:
# changing the name of "Kate Willson" to be "Kate Jameson"
member2.name = "Kate Jameson"
member2.print_name()  # Kate Jameson

# Keyword: del
# The "del" keyword can be used to delete a property or an object
# Try creating and editing other instances of the Member class
# Examples:
del member1.name
# member1.print_name()
# Error => AttributeError: 'Member' object has no attribute 'name'
