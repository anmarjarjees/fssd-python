# Defining Classes in Python
# It acts as a blueprint for creating objects

# NOTES
# Python is known as an object-oriented language,
# which means it has first-class support for classes.

# Unlike some other languages, for instance, Java, you're not forced to use classes,

# Python is also known as mixed-paradigm language
# in that you can use either a functional or object-orientated style.

# Classes are a good way of combining data and methods
# and are useful when dealing with hierarchies.

# They are generally used to model more complex data types
# which can't be modelled using Python's built-in data structures
# such as lists and dicts.

# >> We define a class by using the class keyword followed by the name
# >> Like functions, a class does not do anything until it is executed
# >> Scope also applies to classes so global and nonlocal scope have to be taken into consideration
# >> A class name should start with a capital letter and should have a docstring
# >> Classes can contain functions and other statements
# >> A function within a class is known as a method

class HelloWorld:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello, world!'


# The __init__() Method:
# **********************
# >> It initializes the properties of the instance
# >> It's a constructor like in C# or Java
# >> It runs when an instance of the class is created is an initializer
# >> IT is known as a dunder, double-underscore or magic method
# >> It one of these types of methods:
# >>> that are tend to be used on classes mainly
# >>> They use double underscores so as not to conflict with your own defined classes
# >> __init__() method on its own would simply create an empty class object
# >> It can take arguments

class Car:
    def __init__(self, color, make, model, fuel_type):
        # Using "self" keyword
        # for example the color of green that we assign to our object "bulitt"
        # The self keyword is used to confirm that the argument "Green"
        # for the object instance "bullitt" is a reference to the color attribute
        # of the class Car
        self.color = color
        self.make = make
        self.model = model
        self.fuel_type = fuel_type


# Initializing a Car object with attributes 'Green', 'Ford', 'Mustang' and 'Gasoline'
bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline')

print(bullitt)


# Challenge: The __init__() Method
# Steps
# 1. Using the class keyword, define a class named Customer
# 2. Inside the class, add a docstring using triple double quotes to open and close it. Inside the docstring add the comment: Creates an instance of Customer - remember to indent the docstring inside the class
# 3. Inside the class, define your __init__() method and pass it 5 arguments named self, fname, lname, email and phone
# 4. Inside the __init__ method, use the self keyword to create an attribute named fname and give it the value of the fname argument.
# 5. Inside the __init__ method, use the self keyword to create an attribute named lname and give it a value of the lname argument.
# 6. Inside the __init__ method, use the self keyword to create an attribute named email and give it a value of the email argument.
# 7. Inside the __init__ method, use the self keyword to create an attribute named phone and give it a value of the phone argument.
# 8. Un-comment the code provided so you can run your class definition to test that it works.


# write your code here


# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

# customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
# print(customer_one)
# print(customer_one.fname)
# print(customer_one.lname)
# print(customer_one.email)
# print(customer_one.phone)


# *******************
# The "self" Keyword:
# *******************
# associates functions and properties with a class
# holds references to data and behaviour of particular instances of a class
# must be the first parameter of any function in the class
# is used by python to state to what instance to assign an instance attribute


# class "Bird" has:
# >> properties of "kind" and "call"
# >> A function (or method) to describe the bird is included in the class
class Bird:
    """
    Bird class
    """

    def __init__(self, kind, call):
        # This method assigns the values to the object properties.
        # The self keyword is a reference to the current instance of the class
        # and is used to access variables that belong to the class

        # properties:
        self.kind = kind
        self.call = call

    # behaviour
    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call}"

    # another method( behaviour):
    def call(self, _call):
        print(_call)


owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())

# Challenge > The "self" Keyword:
# Steps:
# 1. Define a class named OrderItem

# 2. Inside the class, add a docstring with the text content Creates an instance of OrderItem

# 3. Inside the class, define the __init__() method and pass it four arguments of self, item, price and quantity

# 4. Inside the __init__() method, use the self keyword to build attributes for an item, price and quantity using the relevant arguments passed to the method

# 5. Outside the __init__() method but still inside the OrderItem class, define a method named description and pass it the self argument

# 6. Inside the description method, return a string using the class attributes, that describes the order item in the following format "quantity x item at price each" For example: "3 x bowtie at $10 each"

# 7. Un-comment the code provided so you can run your class definition to test that it works

# Write your code here


# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

# order_item_one = OrderItem("bowtie", 10, 3)
# print(order_item_one.description())

# order_item_two = OrderItem("Fez", 25, 1)
# print(order_item_two.description())


# Creating Class Instances:
# *************************
# > An individual object of a class in memory with values
# > It exists live in RAM until the point it is removed.

# When you create an instance of the class,
# it is the initializer code that runs. This is the __init__ method.

# To create an instance of the class,
# you need to provide the same quantity of values as there are properties
# (in this case two).
owl = Bird('Owl', 'Twit Twoo!')

# Once you have an instance of that class,
# you can access the variables and methods using the dot notation.
owl.call
owl.description()

print(owl.call)
print(owl.description())

crow = Bird('Crow', 'Caaaw!')
print(crow.description())
# The dot notation can also be used to modify the properties of objects
# with the use of the assignment operator
# The "de"l keyword can be used to delete a property or an object.
# Try creating and editing other instances of the Bird class.
owl.call = 'screech'
print(owl.description())
del owl.call
print(owl.description())

# Challenge: Creating Class Instances

# Steps
# 1. Underneath where the User class is defined, declare a variable named user_one.

# 2. Create a new instance of User where the value for username is "arnold", the value for email is "arnold@email.com" and the value for subscribed is True. Assign the class to the user_one variable.

# 3. Use a print statement to print out the value for the email attribute of the user_one object.

# 4. Update the email attribute of the user_one object to "murphy@email.com"

# 5. Use a print statement to print out the description of the user_one object.


class User():
    """
    Creates an instance of User
    """

    def __init__(self, username, email, subscribed):
        self.username = username
        self.email = email
        self.subscribed = subscribed

    def description(self):
        """
        Describes the instance of User
        """
        return f"user: {self.username}, email: {self.email}, subscribed: {self.subscribed}"


# write your code here


# Class Properties & Attributes
# *****************************
# > Data within a class

# Class Attribute:
# ****************
# > When you create a Python variable within the class but outside the constructor function
# > It is shared between all objects of this class.
# > A class attribute can be accessed as a class property or an instance property.

# Instance Attribute:
# *******************
# > When you create a Python variable within the constructor function
# > It is is only accessible from the scope of an object instantiated from the class.
# > If you try and access an instance attribute as a class property, then you will raise an AttributeError.

class Bird:
    """
    Bird class
    """
    # class attribute of "definition"
    # class attribute:
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # two instance attributes of "kind" and "call"

        # instance attributes:
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call}"


owl = Bird('Owl', 'Twit Twoo!')
# The owl object instantiated from the Bird class
# is able to access the class and instance properties with dot notation
print(owl.description())
print(owl.definition)
print(owl.call)
print(Bird.definition)
# The Bird class, however, can only access the class property.
# Trying to access "call" gives the following error;
# AttributeError: type object 'Bird' has no attribute 'call'
# print(Bird.call)

# Challenge: Class Properties & Attribute
# Steps:
# 1. Define a class named ContactInfo and give it a docstring with the text content of Creates an instance of ContactInfo

# 2. Inside the class, declare a class attribute named about and assign it the value of "Contact information for customer"

# 3. Inside the class, define the __init__() method, and give it the arguments named self, name and email.

# 4. Inside the __init__() method, create instance attributes for name and email using the name and email arguments passed to the __init__() method.

# 5. Inside the class, define another method named description, and pass it the self argument.

# 6. Inside the description method, return a string that lists the name and email of the ContactInfo instance, with a colon between the values. For example: "name: email@email.com"

# 7. Outside the class definition, print the value for the class argument named about in the ContactInfo class.

# 8. Declare a variable named contact.

# 9. Create an instance of ContactInfo with the values of "dave" for name and "lister@email.com" for email. Assign the class object to the contact variable.

# 10. Print the description from the contact object to the terminal.

# Functions + Classes: Methods
# ****************************
# A method is a function that is within a class or object
# The term method was used in our lesson like built-in methods append() for a list
# You can create your methods (functions) within your classes.
# When you create an instance of that class, then you can call the method using dot notation
# In the class instance unit, we used the description method on the object owl, which was instantiated from the Bird class.
# This is referred to as invoking the description() method

# Public Methods vs Private Methods:
# A public method is one that can be accessed within the class or outside the class through its object
# A private method is one that cannot be accessed except within the class

# NOTE:
# Not all methods in a class need to be public
# If you want to indicate to other developers that a method is private,
# then prefix the method name with an underscore


class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    # This method returns a description of the instance.
    def description(self):
        """
        describe the bird
        """
        # the "parrot" variable created in the method is local to the method
        # so it could not be used in the class.
        parrot = "Norwegian Blue"
        return f"A {self.kind} goes {self.call} and is {self.definition} It is not a {parrot}"


owl = Bird('owl', 'Twit Twoo!')

# After creating an "owl" instance, we can call that method and print the result to the terminal.
print(owl.description())

# Challenge: Functions + Classes
# Steps:
# 1. Create a class called BlogPost and give it a docstring with the following text content: Creates an instance of BlogPost

# 2. Inside the BlogPost class, create the __init__() method that accepts the following arguments: self, title, content and author.

# 3. Inside the __init__() method, create instance attributes for title, content and author using the arguments passed to the __init__() method.

# 4. Inside the BlogPost class, define a method named get_overview and pass it the self argument

# 5. Inside the get_overview method, return a string built with the title and author values from the instance so that the format of the string is "<title> by <author>".

# 6. Inside the BlogPost class, define another method named full_info and pass it the self argument

# 7. Inside the full_info method, return a string built with the title, content and author values from the instance, so that the format of the string is "Blog post: <title>. Content: <content>. Author: <author>"

# 8. Outside of the BlogPost class, create an instance of BlogPost assigned to a variable named post and pass it the following arguments: "Python Classes" for title, "Python is known as an object-oriented language..." for content and "Code Institute" for author.

# 9. Print the returned value from the get_overview method of the post object to the terminal.

# 10. Print the returned value from the full_info method of the post object to the terminal.
