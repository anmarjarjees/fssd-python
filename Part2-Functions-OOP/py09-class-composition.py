# Class Composition:
# In object-orientated programming, two significant concepts are:
# - inheritance
# - composition.

# Inheritance:
# is what we have used up until now in this lesson.
# For example, a subclass Parrot inherits from a Bird class.
# The inheritance relationship, in this case, is that a Parrot is a Bird.
# Any code where you use class Bird you could equally use class Parrot without changing the desired outcome of your program.

# Composition:
# is where one class contains the object of another class.
# In this case, we could have a Bird class and a Tail class.
# The composition relationship here would be that a Parrot has a tail so would inherit from both Bird and Tail.
# However, a Kiwi does not have a tail, so would only inherit from Bird.
# That way, you can have a Duck and a Parrot class that reuse Tail but are themselves not derived from each other.
# A Parrot is not a Duck, but both of them have a Tail.
# With composition, you cannot use class Tail interchangeably with Bird.
# The Tail class is not a subclass of Bird.

# Mixin and Composite:
# The purpose of both mixin and composite is to reduce the amount of unnecessary duplication of code.
# With the Bird example, you can have many bird subclasses, but if some of them share certain properties,
# then there is the opportunity to move them into a class with a composite relationship.
# You could, for example, reuse the Tail class in another program where you have a Reptile base class.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Engine:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        self.fuel = fuel

# InternalCombustion class has a composition relationship with Engine


class InternalCombustion(Vehicle, Engine):
    def __init__(self, make, model, capacity, fuel):
        Vehicle.__init__(self, make, model)
        Engine.__init__(self, capacity, fuel)


# Electric inherits from Vehicle.
class Electric(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)


# The volkswagen has an engine, but it is not an engine.
volkswagen = InternalCombustion("Volkswagen", "Golf", 1.7, "Diesel")

# Electric inherits from Vehicle. Therefore the tesla object is a Vehicle
tesla = Electric("Tesla", "X")

# The Engine class could be reused for a PowerBoat class without PowerBoat and InternalCombustion being derived from one another.
# ============================================================================================================================= #


class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, fname, sname, no_of_years):
        # instance attribute
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"First Name: {self.fname}\n Surname: {self.sname}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"

# Updating the example of the "Simple Human Resources Applications"
# The first additional class is ExternalContract for employees
# who are not direct employees of the company but are contract employees.


class ExternalContract:
    """
    Class for contract employees
    """

    def __init__(self, contract_cost):
        # This has an instance attribute to take the cost of the contract
        self.contract_cost = contract_cost

    def cost(self):
        """
        Returns the contract cost added to the salary
        """

        # It also has a method that returns that added to the employee salary.
        return self.contract_cost + 30000

# Here we have also included the HolidayMixin. This class uses composition and mixin.


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """

    def calculate_holidays(self, no_of_years):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class. 
    """

    def __init__(self, fname, sname, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, fname, sname, no_of_years)

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

    def details(self):
        """
        Method to return direct developer details as a string
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


# Finally, we have the ContractDeveloper class.
# This is for developers who are not direct employees.
# This has a composition relationship with ExternalContract.
# A contract developer has an external contract.
# A direct developer does not.
# You can reuse this ExternalContract for any other job class you create.
class ContractDeveloper(HolidayMixin, Employee, ExternalContract):
    """
    Class is subclass of Employee, composition relationship
    with ExternalContract and using HolidayMixin
    """

    def __init__(self, fname, sname, no_of_years, prog_language, contract_cost):
        self.prog_language = prog_language
        self.contract_cost = contract_cost
        Employee.__init__(self, fname, sname, no_of_years)

    # The method details for ContractDeveloper inherits from Employee but also provides for the cost of the contract.
    def details(self):
        """
        Returns inherited details plus contract cost
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n Contract cost: {ExternalContract.cost(self)}'


# We have instantiated two developers: one direct "dev" and one contract "contractor"
# See how their details differ.
# Also, we use the method from the mixin to see how much annual leave they have accrued.
# For the direct developer, you can also call the method to see their salary.
dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
print(dev.details())
print(dev.calculate_holidays(dev.no_of_years))
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects.
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays(contractor.no_of_years))


# Challenge: Class Composition & Mixins
# Steps
# 1. Create a mixin called TicketMixin and give it a docstring description of Mixin to calculate ticket price based on age
# 2. Inside the mixin, define a method named calculate_ticket_price that takes the self argument and an age argument
# 3. Inside the method, write the code to return an integer ticket price based on the value of the age argument. If the age is less than 12, the price is 0. If the age is less than 18 the price is 15. If the age is less than 60 the price is 20. And if the age is 60 or over the price is 10.
# 4. Define a class named Customer that inherits the TicketMixin. Give it a docstring description of Create instance of Customer
# 5. Inside the Customer class, define an __init__() method that takes the self argument, and two more arguments: name and age
# 6. Create instance attributes for name and age from the arguments passed to the method.
# 7. Inside the Customer class, define a method named describe which takes the self argument.
# 8. Inside the describe method, build a string with the name and age instance attributes, and the returned value from the calculate_ticket_price method. The string should have this format: "<name> age <age> ticket price is <price>"
# 9. Outside the class definition
# 10. Create a variable named: customer and assign it an instance of the Customer class which should take the values "Ryan Phillips", 22
# 11. print the returned value from the describe method of the customer object to the terminal
# Note in the test a selection of customers will be created with different ages to check that the describe method and TicketMixin class work correctly
