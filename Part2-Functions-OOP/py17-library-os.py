# os:
# built-in library
# Provides functions for working with the operating system.

"""
General Notes:
- The operating system is the software that interfaces 
between the hardware and user on a computer. 

- Common operating systems would be Windows, macOS, Linux or iOS. 

- A frequent use for this would be accessing the environment variables. 
Every computer has a set of environment variables listing information 
on how the machine is set up. 
"""

# import the os library:
import os

# using the get current working directory function getcwd()
# to find the directory in which the python file is located.
print(os.getcwd())

# We can also list the files or directories listdir() within a directory.
print(os.listdir('Python-Basic/Part2-Functions-OOP/'))

# read more: https://docs.python.org/3/library/os.html


# Challenge: io
# Steps:
# 1. Create a variable file assigning it a value from using the open() method and passing in the file named "lyrics.txt"
# 2. Create a variable named: lyrics, assign it a value from using the file variable and using the method read() with it
# 3. Use the close() method on the file variable to close the file.
# 4. Print the value of the lyrics variable to the terminal.
