# Subclassing & Inheritance
# *************************
# Subclassing is a useful way of creating a specialized version of a class with its methods
# but re-using existing methods and properties of the parent (or base) class.

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

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call} and is {self.definition}"


# we’ve created a Parrot class which subclasses Bird with its methods
# Yes in the subclass, we can re-use existing methods and properties of the parent (or base) class.

# To subclass/inherit from a superclass/parent:
# add the name of the parent class inside parentheses as part of the subclass name.
class Parrot(Bird):
    # We can use the existing methods on the parent class
    #  we don’t have to supply the bird "kind" or "call"
    # because that’s coded into the Parrot class.
    # They are inherited.
    def __init__(self, color):
        # To call a method on the parent class:
        # >> precede the parent method name with the parent class name
        # >> and a period
        Bird.__init__(self, 'Parrot', 'Kah!')
        # We can add specialized behaviour such as the additional property of color.
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())


print(parrot.kind)  # empty
print(parrot.call)  # empty

# Challenge: Subclassing & Inheritance
# ************************************
# Steps:
# 1. Underneath the class definition for JobListing, create a new class named SalesManager and pass it the JobListing parent or superclass class name as an argument. This means the SalesManager will be derived from the base class JobListing.

# 2. Inside the SalesManager subclass, define the __init__() method and pass it the arguments of self and salary to extend the functionality of its parent superclass.

# 3. Inside the __init__() method, use the parent JobListing class to extend the SalesManager subclass with the values of "Sales Manager" for job_title and "Sales" for the department

# 4. Inside the __init__() method, create an instance attribute for salary using the salary argument.

# 5. Outside the SalesManager class, declare a variable named sales_manager

# 6. Create a new instance of SalesManager, pass it a value of 45000 for salary and assign the new class object to the sales_manager variable.

# 7. Print the result of the description method inside the sales_manager object

# 8. Print the salary value stored in the sales_manager object


class JobListing():
    """
    Creates an instance of JobListing
    """

    def __init__(self, job_title, department):
        self.job_title = job_title
        self.department = department

    def description(self):
        return f"Job opening for {self.job_title} in {self.department} department"

# write your code here
