# Reading Data From a File

# NOTE:
# Please don't forget to get/change the full path of these two files: "data.txt" and "lyrics.txt"
# Based on where you are going to save it/create it inside your computer (folder structure)

# How to open a file for reading in Python
# Opens a file in memory so that we can read, display and manipulate the contents
# Using the Python 'open', 'read' and 'readlines' methods

# Text File is a very simple format to save data (.txt)
# You can save lines of text in the file
# then use python io to open the file and read the contents

# The python function:
# open() to open a file

# The python methods:
# readlines() which reads all the lines into a list (this method returns a list)
# readline() which reads one line at a time
# read() which reads the entire file
# seek() which moves to a particular point in a file
# close() which closes the file

# NOTES:
# 1) When you open a file, you are reading or writing
# to a particular position within the file

# 2) If you use readline (readlines) to read a line/lines,
# your location within the file is advanced by a line (by all the lines).
# The next time you read a line, the line will be read from the end of the last line.

# 3) It's also important to understand that files don't have lines.
# A file is just one long sequence of bytes (the computer's way to store characters),
# but when Python sees a line separator such as "\n",
# it interprets that as marking the break between two lines.

# Example:
# the code will open a file "data.txt"
# reads the lines it contains into a variable called "lines"
# The 'r' means that the file is opened as read-only
# open() => Open file and return a stream.

my_file = open(
    'Please Put The File Full Path Here\data.txt', 'r')
# Character Meaning:
# 'r' open for reading (default) => Yes, it's an optional parameter
# 'w' open for writing,

# If we don't specify the full path to a file to the open(),
# just its name - a relative path, we will receive this error:
# The file doesn't exist, we will have this error:
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
print(type(my_file))  # <class '_io.TextIOWrapper'>

print('printing the variable "my_file":')
print(my_file)  # an object
# the output:
# <_io.TextIOWrapper
# name='The Full Path of Your file'
# mode='r'
# encoding='cp1252'>

# through our object "my_file" we can access all the file methods!
# let's create a variable named "lines" to receive all file lines using readlines()
# lines = my_file.readlines()
# print(type(lines))  # <class 'list'>

# When printed out, we see that it's a list of strings.
# print(lines)
# ['This is the first line\n',
# 'And this is the second\n',
# 'Here is the third line\n',
# 'And here the fourth']

# Each line contains the newline character '\n'.
# This makes sense because the file "data.txt" contains four separate lines.
# The readlines() method splits the data read from the files
# at those newline characters, to create a line of strings

# let's try to use readline():
line = my_file.readline()
print(type(line))  # <class 'str'>

# When printed out, we see that it's a list of strings.
print(line)  # Just an empty string
# => Because of readlines will leave the cursor at the end of all the lines


# let's try to use read():
# 1) All of the data will be read into a single string, including the newline characters
# 2) When the string is printed to the console now,
# it just appears as text, not a list of strings
# 3) The newline characters cause the string to be displayed over several lines
read_file = my_file.read()

# close the file:
my_file.close()
# Notice that we can close the file after using any method and save it's returned value
# otherwise, if you close the file and try to access it again:
# ValueError: I/O operation on closed file.

print(type(read_file))  # <class 'str'>
print(read_file)  # Just an empty string or few lines depending on the code above


# Challenge: Reading Data from a File
# Steps:
# 1. Create a function called get_content that takes one parameter called "file",
# which will be the name of a file that we want to read.

# 2. The get_content function should:
# a. use correct methods shown in our lesson to open the file
# b. read the contents of the file
# c. then close the file
# d. and then return the contents from the function.

# 3. Create a variable "lyrics"
# and assign it the value of the return from calling the function get_content
# with the argument: "lyrics.txt"

# 4. Print the value of the lyrics variable to the terminal.


# Step1:
def get_content(file):
    # Step2 (a):
    my_file = open(file, 'r')  # the mode is "r" for reading (by default)
    # Step2 (b):
    content = my_file.read()
    # Step2 (c):
    my_file.close()
    # Step2 (d):
    return content


# Step3:
lyrics = get_content('lyrics.txt')
# NOTE: Please don't forget to specify the full path of the file "lyrics.txt"

# Step4:
print(lyrics)
