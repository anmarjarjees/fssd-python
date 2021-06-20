# Decorators in OOP
# A decorator is a way in Python to add new functionality to an existing method without modifying its structure.
# This is useful as you do not need to create new functionality in your code if a decorator already exists for that purpose.
# Which a software design pattern that is used to alter methods (functions) by warpping them in the decorators

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

    def __init__(self, kind, call, category):
        """
            Important Note About Private Properties/Methods:
            ===============================================
            We have an instance variable called "_fowl_types" with information about the species.
            This instacne variable "fowl_types" has the "__" before its name:
            We don't want to accidentally corrupt this information. 
            Classes should only share what data is needed. 
            This is known as Encapsulation and Separation of Concerns. 
            To mark fowl_types as private and only available to other methods in the class, 
            we have prefixed the name with a dunder. 
            Now we cannot access it but the new method within the class named fowl_types() can.
        """
        self._fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                            'turkey, grouse, chicken, New World quail and Old World quail,\n'
                            'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                            'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.category = category
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)

    @property
    def fowl_types(self):
        return self._fowl_types[self.category.lower()]

    """
    The return in the description method now uses that method to display the information on fowl types. However, for this to work, we need to give read-only access.
    A built-in decorator already exists in Python for that purpose.
    Therefore we can wrap the fowl_types() method in a @property decorator. 
    Try removing it to see what happens.
    """

    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.category}. {self._fowl_types[self.category.lower()]}'


mute = Fowl('Swan', 'honk', 'Waterfowl')
print(mute.description())
print(mute.fowl_types)
