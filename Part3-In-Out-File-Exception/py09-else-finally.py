# Else & Finally Statements
# The try-except has an optional "else" clause

# The clause "else":
# an optional clause that can be attached to try/catch block at the end
# >> is placed after all of the "except" clauses
# >> deals with any code that must be executed in the case where the "try" clause does not raise an exception

# NOTE:
# *****
# The code placed in the try block should only be the code where you are anticipating the exception
# Any other code that should run along with it should be placed in the else block.

# There is an additional optional clause "finally":
# >> is the last clause to run
# >> It runs whether or not an exception has been raised
# >> It is intended for any 'clean-up' code that must run
# regardless of whether an exception was caught or not

# Example:

# We have a function that:
# - opens a text file
# - counts the lines
# - prints result => prints the opening line of the file
def linecount(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    # 1) The "try" block (normal code-main logic) catches if a file does not exist
    try:
        f = open(filename, 'r')
        s = f.readlines()

     # 2) The "except" block deals with the error so that the program does not crash
    except OSError as e:
        # OSError exception is used as it deals with system errors such as I/O errors
        # OSError returns an error code (errno) and message (strerror)
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")

    # 3) The else "block" deals with the code that should run in the case of no error (the file exists)
    else:
        # This is the code that does the line counting
        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
        f.close()

    # 4) The "finally" block runs whether or not the file exists
    # It runs after the try, except and else blocks
    finally:
        # This will print whether the line count has been successful or not
        print(f'Finished with {filename}.')


print("Calling linecount() function:")
linecount('gulliver.txt')
print("\n")
linecount('Please put the full path\lyrics.txt')
print("\n")
linecount('swift.txt')

# NOTE:
# When using IO, you always should close the file when you are finished working on it
# As this is such an important issue, Python has included a with statement to deal with it
# Behind the scenes, it is in effect a type of try-finally statement.

# Example:
"""
f = open(filename)
try:
    # My Code
finally:
    f.close()
"""

# In reality, what is happening is that special methods "__enter__ "and "__exit__" are used:
"""
f = open()
f.__enter__()
try:
    # My Code
finally:
    f.__exit__()
"""

# Important Conclustion: You do not need to type any of this code.
# Just use the "with open" statement as follows:
"""
with open(filename) as f:
       #My Code
"""

# Example:
print("trying with open:")
filename = "nothing.txt"
with open(filename) as f:
    # FileNotFoundError: [Errno 2] No such file or directory: 'nothing.txt'
    print(f)

# As you can see we have refactored the code to use this syntax [with open()].
# No explicit file close statement is required.

# Example:
# let's modify our previous function linecount and gave it another name "linecount2"


def linecount2(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    try:
        # using with open()
        with open(filename, 'r') as f:
            s = f.readlines()
    except OSError as e:
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")
    else:
        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
    finally:
        print(f'Finished with {filename}.')


print("Calling linecount2() function:")
linecount2('gulliver.txt')
print("\n")
linecount2('swift.txt')

# Challenge:
# Steps:
# 1. Create a function named: update_cars it should take three parameters named: data, key, val

# 2. Inside the Function:

# 3. Add a try block

# 4. Inside the try block it should have the statement: data[key]

# 5. Add a except block, which is to catch key errors as e

# 6. Inside the except block it should print out, using an f string: "No key {e} in dictionary"

# 7. Add an else block

# 8. Inside the else block set the key's value in data dictionary equal to the val

# 9. Add a finally block

# 10. Inside the finally block return the data dictionary

# 11. Outside the function call the update_cars function, passing in the arguments: cars, "mazda", 8

# The function should print out a message if the key passed in is not in the cars dictionary passed in.
# Otherwise, it should set the cars key to the value supplied.

cars = {'ford': 5, 'hyundai': 6}


# Do Not Place Code Below This Line
# This will print out the cars dictionary after the update_cars function is called
print(cars)
