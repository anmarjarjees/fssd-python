# io:
# built-in library
# Provides functions for taking data in and producing output

# In real-world applications,
# you might also be reading from and writing to files
# on the computer where the code is running.

# 1) The open() function is used to open the file "source.txt"
# and to let the computer know that this text file is currently in use by the py16-library-io.py module.
# 2) We have assigned this text file to a variable f
f = open('Part2-Functions-OOP/source.txt')

# 3) use the read() function to read the text and assign it to variable lines.
lines = f.read()

# 4) use the close() function to close the file again.
# This is to ensure that other programs will be able to access it.
f.close()
print(lines)


# Challenge: io
# Steps:
# 1. Create a variable file assigning it a value from using the open() method and passing in the file named "lyrics.txt"
# 2. Create a variable named: lyrics, assign it a value from using the file variable and using the method read() with it
# 3. Use the close() method on the file variable to close the file.
# 4. Print the value of the lyrics variable to the terminal.
