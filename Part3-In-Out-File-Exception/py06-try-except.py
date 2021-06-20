# Try-Except Statements

# A result to consider:
# ---------------------
# In the previous example of using the keyword "raise" with the exception class "RuntimeError"
# we saw that we could raise an error when a user does something unexpected, but the program still crashed!

# Action to take:
# ---------------
# It is better to catch and handle these exceptions in such a way that your application continues to run!

# Python Solution:
# ----------------
# Python has a "try" block in which you put code where you anticipate an error could occur
# Example if there might be an issue caused by a users input or corrupt data in a file.

# The program runs any code after the try statement in the usual manner
# if an error occurs rather than raise an exception in the terminal,
# it runs code in a following except block

# After the except statement, you write the code for what you want to do in cases where an error occurs
# Examples of errors:
# If this is user input => it might just be a message to the user that the data was invalid and please try again
# If it is data from a file => then you might just skip the bad data points and carry on

"""
try:
    writing your normal code
except:
    writing another code if something goes wrong
"""

#  In summary:
# >> the "try" block allows you to test a code block for errors
# >> The "except" block enables you to handle the errors.

# Similar to JavaScript:
"""
try {
    writing your normal code
} 
catch {
    writing another code if something goes wrong
}
"""

# NOTES:
# >> Please Comment/Uncomment this code based on which part of the file you want to run or test:
# >> You can provoke an error by trying CTRL + C in the terminal.
# # Application is running == then ==> CTRL + C == Output message ==> "KeyboardInterrupt"
# This HotKey: CTRL + C will interupt (stop) the application

# Example:
# While True => going into infinite loop
"""
while True:
    # Try Block:
    # ----------
    # The "Try" code block of two statements:
    # - asking the user to enter a number
    # - printing their number
    try:
        # keep asking the user to enter a number => then printing this number
        # The two statements are wrapped in a "try" block
        # They run exactly as though the try block was not there as long as the user enters numbers
        x = int(input('Enter an integer number.'))
        print(f'Number is {x}')  # if the user input invalid value
        # z = x/0
        # The error message: ZeroDivisionError: division by zero
        # The error message: ValueError: invalid literal for int() with base 10: 'sf'
        # The same error of the user input a text or decimal value
        # Based on this error message of, we know the exception is "ValueError"

    # Except Block:
    # -------------
    # If the user enters a letter, for example, there is an error
    # The "except" block code will run (to be explained in more details)

    # We can write it by just using the generic syntax "except"
    # except:
    # We can write it by a specific exception
    # except ExceptionName:

    # Adding "ValueError" to the except statement
    # This is one of the "built-in" exceptions in Python
    # It is MORE SPECIFIC than "RuntimeError"
    # that's why it's used here as we know in this case, an inappropriate value input causes an error
    # If you run the code now, you will see the exception is raised, and the except code block is run.
    except ValueError:
        # In this case, we just print "Not a number",
        # but crucially the code keeps running and asks the user for input again.
        # In this case, the error is caught and handled without crashing our application! :-)
        print('Not a valid input (has to be an integer numeric value)')
"""

# Challenge: Try/Except Statements:
# *********************************
# Steps:
# 1. Create a function named: get_val that takes a single parameter named "key"

# 2. Within the function:
# 3. Create a try block and inside the try block, and using the key return the value for that key from the cars dictionary.

# 4. Create an except block and inside the except block return None. This will run if it encounters an error in the try block

# 5. Outside the function:
# 6. Create a variable named: ford which should be assigned the return value from calling the function get_val and passing it the argument "ford"

# 7. print the variable ford

# 8. Create a variable named: hyundai which should be assigned the return value from calling the function get_val and passing it the argument "hyundai"

# 9. print the variable hyundai

# 10. Run the code to check your expected output.
# ***********************************************

# Try & Except Statements (more about exception):
# ***********************************************
# In the previous code example, we handled the error
# by telling the user that they had not entered a number
# No exception was raised just printing a short message to the user so there is no record of the error

# As a developer, you might want to record the incidence of this error, so perhaps you can improve your UX.# In a case where it is not user data entry but a file!
# you might want to record how many data points are bad.
# To do this, you can raise an exception in the except block.

# In some cases, you may anticipate more than one type of error
# Python allows you to have multiple except statements.

# Example:
# we have three except blocks:
# If more than one is valid => the first exception raised is the one you'll see
# Note: You can use the CTRL-C to stop the loop as we did above
while True:
    try:
        """
        z =x/y
        x will be the numerator
        y will be the denominator
        """
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
        # Thinking as programmers/developers:
        # our application will crash if:
        # if the user input invalid values: strings or decimal numbers
        # if the denominator value is 0

        # NOTE: We cannot put the default except before the more specific one(s)
        # the code below for the default (general) except will generate this error
        # SyntaxError: default 'except:' must be last
        """
        except:
            print("Someting goes wrong!")
        """

    # Checking if inappropriate values (invalid values) have been entered:
    # Using a specific python exception category "ValueError":
    except ValueError:
        print("Both values have to be integers.")

        # Checking for division by zero:
        # Using a specific python exception category "ZeroDivisionError":
    except ZeroDivisionError:
        print("Please enter a valid denominator (has to be more than 0).")

        # If another error occurs that the first two except blocks don’t catch
        # Then the third block which uses a general exception catches it:
        # we can use:
        # either => except Exception:
        # or => except:
    except Exception:
        print('Another error has occurred')
        # for learning and testing:
        print(type(Exception))  # <class 'type'>
        print(Exception)  # <class 'Exception'>
