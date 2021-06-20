# Catching Generic Errors With the keyword: "as"
# the keyword "as" => Allows access to the attributes of the exception object
# Using: With except Exception as err syntax

# As we have learnt => The built-in exceptions contain information about the error
# We only tried to just display the exception in the terminal.
# But the exception object includes the error message and also additional arguments

# Example:
def encode_name(name):
    try:
        # encode('ascii') => using American Standard Code for Information Interchange
        # encode() => by default => using UTF-8 => no problem
        name = name.encode('ascii')
        # you can learn more about encode(): https://www.w3schools.com/python/ref_string_encode.asp
        print("name:", name)

        # We can use this nice trick to know exactly what's the exception type:
        """
        except Exception as e:
            print(type(e))  # <class 'UnicodeEncodeError'>
            # 'ascii' codec can't encode character '\xe9' in position 2: ordinal not in range(128)
            print(e)
        """

    # We have passed the "UnicodeError" exception to a variable e (by convention as short for exception)
    # the variable "e" will be the exception object to help us access all the exception properties/attributes
    except UnicodeError as e:
        # for testing and learning:
        print("the argument e info:")
        print(type(e))  # <class 'UnicodeEncodeError'>
        # 'ascii' codec can't encode character '\xe9' in position 2: ordinal not in range(128)
        print(e)
        # Using the additional arguments of the exception object:
        # .object
        # .start
        # .encoding
        # .reason
        # The link: https://docs.python.org/3/library/exceptions.html#UnicodeError
        print("the argument e properties:")
        print(e.object)  # Stéfan
        print(e.start)  # 2
        print(e.encoding)  # ascii
        print(e.reason)  # ordinal not in range(128)
        print(
            f'The name {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason}')
        print("name:", name)

        print("items:")
        print(e.args)  # ('ascii', 'Stéfan', 2, 3, 'ordinal not in range(128)')
        for value in e.args:
            print(value)
        # The output:
        # ascii
        # Stéfan
        # 2
        # 3
        # ordinal not in range(128)

        # for key, value in e.args:
        #     print(key, value)


encode_name("alex")  # b'alex'
encode_name("!@#$%^&*()")  # b'!@#$%^&*()'
encode_name("-=_>><</|\\")  # b'-=_>><</|\\'
encode_name('Stéfan')
# The error before using exception:
# UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 2: ordinal not in range(128)
# The output:
# The name Stéfan has a character at position 2 that cannot be encoded in ascii due to ordinal not in range(128)

# Another Example:
# In the below, there is no file "book.txt", so the except block runs.
try:
    my_file = open('data.txt')
    first_str = my_file.readline()  # will only return the first string
except Exception as e:
    print(type(e))  # <class 'FileNotFoundError'>
    print(e)  # [Errno 2] No such file or directory: 'data.txt'
    print("Error in loading the file 'data.txt'")
    # pass

# since we know the exception name
try:
    my_file = open('data.txt')
    first_str = my_file.readline()  # will only return the first string
except FileNotFoundError as e:
    print(type(e))  # <class 'FileNotFoundError'>
    print(e)  # [Errno 2] No such file or directory: 'data.txt'
    print("Error in loading the file 'data.txt'")

    print("items:")
    print(e.args)  # (2, 'No such file or directory')
    for value in e.args:
        print(value)


# going to LMS example:
try:
    my_file = open('data.txt')
    first_str = my_file.readline()  # will only return the first string

# Using The "OSError" exception: for operating system errors such as file not found
# The exception "OSError" is passed to variable "e"
# so we have access to object property named "args" for arguments
# which means we have access to all the exception object arguments
except OSError as e:
    print("e.args:")
    # e.args is a tuple that contains two values: error number and text message
    print(e.args)  # (2, 'No such file or directory')
    # The link: https://docs.python.org/3/library/exceptions.html#OSError
    # Then we are passing the arguments (e.args) to a tuple with variable names "errno" and "strerror"
    # "errno" => the numeric error code
    # "strerror" => the corresponding error message
    errno, strerror = e.args
    # We could also have used the filename argument, for example.
    print(f"There is an I/O error number, {errno}: {strerror}.")

# The output:
# There is an I/O error number, 2: No such file or directory.

# Challenge: Catching Generic Errors With "as"
# Steps:
# 1. Create a function named: append_to_list it should take two parameters named: ls, val

# 2. Inside the Function:
# 3. Add a try block
# 4. Inside the try block it should append the val to the ls
# 5. Add a except block, which is to catch AttributeError as e
# 6. Inside the except block it should print out, either e.object or e.args[0],
# you need to figure out which.
# 7. After the try except blocks it should return the ls variable
# 8. Outside the function call the append_to_list function, passing in the arguments: values, 4

# The function should print out the error message,
# but it should not change the the values variable,
# as a tuple was passed into a function expecting a list
