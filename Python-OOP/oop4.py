class Member:
    # Now we can enhance and improve our class by adding a "Help Text":
    # We will use this symbol """ (three double quotes) which is called a "Docstring"
    # you see this message in the tooltip when you hover the mouse over the class
    """Member Class is for accepting the following member info:
    - full_name: The Member Full Name (Mandetory)
    - dob: The Date of Birth YYYY-MM-DD (Mandetory)
    - title: The Job Title (Optional) and it's empty by default
    """

    def __init__(self, full_name, dob, title=""):
        # again: self.name and self.dob are just a variable for our class
        # any variable we create inside a class can be called "Field"
        self.name = full_name  # self.name will be the full name
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title

        # Python will split the text based on the space in between the first and the last name
        name_parts = full_name.split(' ')
        # index 0 will have the first name value
        self.first_name = name_parts[0]
        # Below we fixed the error by adding self.
        self.last_name = name_parts[1]  # index 1 will have the last name value


# Creating our object "member1" which is an instance of the class "Member"
member1 = Member("Sally Graysons", "1982-02-05")
print(member1.name)  # Sally Graysons
print(member1.dob)  # 1982-02-05
print(member1.first_name)  # Sally
print(member1.last_name)  # Graysons

# HINT: for testing the Help Text in the run time
# We can use a class function named "help()"
# The syntax: help(class_name)
# Example: let's take a help for our class member
help(Member)

# In case if you see this text with -- More -- at the end
# you can press "Enter" to keep reading more about the class:

# Help on class Member in module __main__:

# class Member(builtins.object)
#  |  Member(full_name, dob, title='')
#  |
#  |  Member Class is for accepting the following member info:
#  |  - full_name: The Member Full Name (Mandetory)
#  |  - dob: The Date of Birth YYYY-MM-DD (Mandetory)
#  |  - title: The Job Title (Optional) and it's empty by default
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, full_name, dob, title='')
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
