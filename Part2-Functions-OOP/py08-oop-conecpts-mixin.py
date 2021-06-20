# *******
# Mixins:
# *******
# In the previous examples, we created a subclass that inherited from a parent class.
# This inheritance relationship states that a Parrot is a Bird.
# It means you do not have to duplicate all the properties of a bird
# when you create a subclass.
# Anywhere in your code that you used a Bird object, you can now use a Parrot one.

# Mixin:
# > A mixin is a class that provides methods to other classes
# but is not itself a parent class.
# > You cannot create a subclass of a mixin.
# > If you find yourself creating methods in your subclasses that are very similar, then this is an opportunity to move that method into a mixin.

# Why mixin:
# The purpose of a mixin is to reduce the amount of unnecessary duplication of code.
# If you have a piece of logic that is frequently repeated in the subclasses, then move it to a mixin.


# Here we have:
# 1) a superclass with a method that returns x
# 2) two subclasses (SubClass1 and SubClass2) with methods that return y and z respectively as a tuple
# including the inherited x from their parent class.
# 3) both subclasses also use a mixin which unpacks a tuple
# and returns the values in a string with some formatting.
# The mixin has no __init__ so cannot be a superclass.
# It is just a class containing a method that you can use in any other class in your program.
class SuperClass:
    """This is the base or parent class"""

    def __init__(self, x):
        self.x = x

    def result(self):
        """Method returns a variable x"""
        return self.x


class Mixin:
    """This mixin can be used with any class"""

    def prettify_string(self, a):
        """Method that returns a string containing variables c and d"""
        c, d = a  # Unpacks the tuple a into variables c and d
        return f'{c}, {d}!'


class SubClass1(Mixin, SuperClass):
    def __init__(self, x, y):
        """Inherits x from SuperClass and extends with variable y"""
        SuperClass.__init__(self, x)
        self.y = y

    def result1(self):
        """Returns a tuple of x and y"""
        return self.x, self.y


class SubClass2(Mixin, SuperClass):
    def __init__(self, x, z):
        """Inherits x from SuperClass and extends with variable z"""
        SuperClass.__init__(self, x)
        self.z = z

    def result2(self):
        """Returns a tuple of x and z"""
        return self.x, 2 * self.z


hello = SubClass1('Hello', 'World')
world = SubClass2('Hello', 'World')

print(hello.prettify_string(hello.result1()))
print(world.prettify_string(world.result2()))

# Example: Simple Human Resources application:

# The first class is Employee which is the base class:
# > It takes the necessary information about the employees
# > and increments the employee number for each new employee added to the system


class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, name, no_of_years):
        # instance attribute
        self.name = name
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"Name: {self.name}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"


# Then we have a mixin class HolidayMixin.
# This is just a piece of logic to calculate the extra holidays you accrue the longer you work for the company.
# NOTE:
# You cannot create an instance of this class.
# As a mixin, it just contains a method to return the number of holidays a particular employee is due.
# It bases this on the number of years of service.
class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    Note that a mixin has no __init__ as you cannot create an instance of a mixin
    """

    def calculate_holidays(self, no_of_years):
        """
        Method that returns holidays as an integer if given no of years of service
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if no_of_years < 3:
            bonus = holidays + 1
        elif no_of_years <= 5:
            bonus = holidays + 2
        elif no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


# The next class is DirectDeveloper.
# This subclasses Employee but:
# > takes an additional parameter of prog_language,
# > allowing you to specify which programming language this developer uses.
class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class but also inheriting from HolidayMixin
    """

    def __init__(self, name, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, name, no_of_years)

    # There is a method here to calculate the salary and give a bonus to Python developers as they are most in demand.
    # The details method inherits from the Employee class and adds additional information about the programming language.
    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def get_details(self):
        """
        Method to return direct developer details as a string
        Uses details() method inherited from Employee super class
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


# We have instantiated two developers here, one Python and one php.
# See how their details differ.
# Also, we use the method from the mixin to see how much annual leave they have accrued.
# You can also call the method to see their salary. Try adding some other developers and see the employee numbers increase.
# Try different programming languages and years of service to see how the salary or holiday benefits change.
eric = DirectDeveloper("Eric Praline", 2, "python")

# Prints out all the attributes of your eric instance using get_details method from DirectDeveloper
# If you use the details method from Employee then the Programming Language will not print
print(eric.get_details())
# The mixin method is usable for instance eric
print(eric.calculate_holidays(eric.no_of_years))
# Uses the calculate_salary method from DirectDeveloper
print(f'${eric.calculate_salary()}')

luigi = DirectDeveloper("Luigi Vercotti", 10, "php")
print(luigi.get_details())
print(luigi.calculate_holidays(luigi.no_of_years))
print(f'${luigi.calculate_salary()}')
