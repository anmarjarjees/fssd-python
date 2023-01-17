# os.path()
# built-in module in the os library
# Provides functions for manipulating path names

# import the os library:
import os

# os.path() method allows you to dynamically create path names
# so you can connect to files on the operating system
# and save files where you intend to.

# This is how you would join two paths in your code
print(os.path.join('/home/runner/', 'os'))

# In the steps below:
# taking the absolute path and joined it with the current working directory.
path = "/home/runner/os/main.py"

# Splits the path into a pair (head, tail) where the tail is the end of the pathname
# The tail is after the / and the head is the pathname up to that point
(dirname, filename) = os.path.split(path)
print(f'The directory path is {dirname}')
# The directory path is /home/runner/os

print(f'The filename is {filename}')
# The filename is main.py

# Splits the filename into a pair (root, ext)
# The root is before the dot and the ext contains the dot with the suffix after it
(module, extension) = os.path.splitext(filename)

print(f'The module is {module}')
# The module is main

print(f'Its file suffix is {extension}')
# Its file suffix is .py

# read more: https://docs.python.org/3/library/os.path.html
