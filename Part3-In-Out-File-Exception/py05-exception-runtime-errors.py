# Python error messages are called exceptions
# When an error occurs ==> an exception is raised
# All exceptions are instances/object of a class "BaseException"

# The exceptions can be generated:
# either by the interpreter while running the code
# or by functions in the code

# As a developer, you can raise these exceptions to deal with errors caused by "incorrect user input"
# Python has some specific categories for exception, example:
# "ZeroDivisionError" raised when the second argument of a division or modulo operation is zero

# The fallback solution:
# "RuntimeError":" raised when an error does not fall into one of these specific categories of Python
# an associated string will explain what has gone wrong

# this function has the parameter "n" that accept a numeric value
def choices(n):
    # will print text to the terminal if 1 or 2 is entered
    # what happens if a user enters another number or a string instead?
    # In the else, we have used the keyword "raise" to raise a "RuntimeError" exception if this happens
    if n == 1:
        print("First item chosen")
    elif n == 2:
        print("Second item chosen")
    else:
        raise RuntimeError


choices(3)
# The output:
#   raise RuntimeError
# RuntimeError

# For more details: https://docs.python.org/3/library/exceptions.html#RuntimeError
