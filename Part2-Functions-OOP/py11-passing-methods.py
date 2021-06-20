# Methods are functions within a class so in the same way functions are passed around so are methods.
# A method itself is an object, this will allow us to pass a method around from superclass or mixin to subclass
# And this will avoid repetition by reusing existing methods

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


class Parrot(Bird):
    def __init__(self, color):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.color = color


parrot = Parrot('blue')
print(parrot.color)

"""
Because of the inheritance, 
The method "description" has been passed from the superclass to the subclass 
and is available for use by an object instantiated from the subclass.
"""
# we can use the description method belonging to the Bird class
# with an instance of the Parrot class
print(parrot.description())

# Challenge: Passing Methods Around
# Steps:
# 1. Create a class named Employee that takes arguments for name and annual_salary
# 2. Give the class a doc string of: Creates an instance of Employee
# 3. Inside the Employee class define a method called calculate_monthly_salary that returns the value of one-twelfth of the annual_salary
# 4. Create a class called CustomerServiceEmployee that inherits from the Employee class and takes the arguments: name, annual_salary, department
# 5. Give the class a doc string of: Creates an instance of CustomerServiceEmployee
# 6. Inside the CustomerServiceEmployee create an __init__ method giving it the correct arguments
# 7. Within the __init__ method add the super().__init__ method giving it the correct arguments.
# 8. Outside of the CustomerServiceEmployee class:
# 9. Declare a variable cs_manager and assign it an instance of the class CustomerServiceEmployee using the arguments: "Kelly Johnson", 42000, "Customer Service"
# 10. Declare a variable kellys_monthly_salary and assign it a value using the method calculate_monthly_salary
# 11. Print the value of kellys_monthly_salary to the terminal.
