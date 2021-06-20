# A subclass refers to the class it inherits from as a superclass
# With the super() function

# Quick Review/Recap:
# Derived Class (subclass) == extends ==> Base Class (superclass)
# The class that inherits properties/method is the subclass.
# If you refer to or use the subclass in your code, it is inheriting from the superclass.

# When referring to the superclass in a subclass:
# we have explicitly used the superclass name in front of the inherited attributes or properties.
# To improve the maintainability of your code, use the super() function in place of the superclass name.
# Therefore, if you ever change the superclass
# you only then need to change the argument in the subclass definition not everywhere else in the code.

# Simple Shapes Example:
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


# square is a special type of rectangle where the width and height are the same:
# In OOP: class Square(Rectangle)
# and using super()
class Square(Rectangle):
    def __init__(self, height):
        # Below, the reference to superclass Rectangle
        # is replaced with the function super() in the subclass Square:
        super().__init__(height, height)


# Bird Classes Example:
class Bird(object):
    """
    Bird superclass
    """

    def __init__(self, kind, call):
        # instance attributes
        self.kind = kind
        self.call = call

    def description(self):
        """
        Returns description string including instance attributes
        """
        return f'A {self.kind} goes {self.call}'


class Fowl(Bird):
    """
    Subclass of the superclass Bird
    """

    def __init__(self, kind, call, type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.type = type
        # Useing of super() to denote which instance attributes are inherited from the superclass Bird.
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)

    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """

        # "super()" is also used in the subclass methods like here
        # to inherit the superclass description method to avoid repetition of code.
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.type}. {self.fowl_types[self.type.lower()]}'


class Seabird(Bird):
    """
    Subclass of Bird superclass for sea birds
    """

    def __init__(self, kind, call, diving_depth):
        # super() is used to denote what is inherited from Bird
        super().__init__(kind, call)
        self.diving_depth = diving_depth

    def get_description(self):
        """
        Returns description from superclass using super() function
        Appends additional information as a string
        """
        return f'{super().description()} and also, a {self.kind} dives to a depth of {self.diving_depth} metres.'


gannet = Seabird('Gannet', 'Squawk', 3)
print(gannet.get_description())

duck = Fowl('Mallard', 'Quack!', 'Waterfowl')
print(duck.description())


# Challenge: Superclassing
# Steps
# 1. Create a class named ShoeOrderItem that takes the BaseOrderItem class as an argument.
# 2. Give the ShowOrderItem a docstring description of Creates instance of ShoeOrderItem
# 3. Define the __init__() method which takes the self argument, and 4 other arguments: product, price, quantity and size.
# 4. Use the super(). __init__ method to access the parent BaseOrderItem class and pass it the product, price and quantity values
# 5. Define the instance attribute of size for the ShoeOrderItem class using the size argument passed to it.
# 6. Inside the ShoeOrderItem class, define a method called describe
# 7. Inside the describe method, return a string using the product, size and quantity values, and the total_price method to produce the following output format:
# Order: <product> in size <size>, quantity: <quantity>, total price: <total_price>
# 8. Outside the ShoeOrderItem class, create an instance of ShoeOrderItem named shoe_order and pass it the values of "Ladies Nike Trainers" for the product, 40 for the price, 2 for quantity and 42 for size.

# 9. Print the returned value from the describe method from the shoe_order object to the terminal.
