# module: re
# Support for regular expressions (RE).
import re

import collections
# ================================================================================
# practical thing we can do with text files is to count the occurrences of words
# It uses two standard libraries:
# - "re" module
# - "collections" module

# The "re" module will allow us to identify the words in the file using regular expressions
# The "collections" module allows us to count occurrences of words

# We can do it in two lines:
# my_file = open('Please place here the full path\data.txt', 'r')

# text = my_file.read().lower()

# or all in one line (method chaining)

# below we are chaining 3 methods at the same time!
# open() method will produce a file object
# then we use read() method of the file object => will produce a string
# then we can use the lower() method of string object => convert all letters to lower case
# finally assign the result to the variable "text"
text = open(
    'Please place your file path here\data.txt', 'r').read().lower()

# Just for testing:
print(text)
# The output:
# this is the first line
# and this is the second
# here is the third line
# and here the fourth

# The findall method is used below to parse the string "text" and find words.
# Using the "Regular Expression" pattern: '\w+'
# The pattern for a word is ' our RE pattern '.
# The '\w' denotes 'not whitespace'
# The '+' denotes 'one or more
words = re.findall('\w+', text)

print(type(words))  # <class 'list'>

count = 1
for word in words:
    print(f"Word#{count} is: {word}")
    count += 1

# The "Counter" method of collections:
# will count how many occurrences there are of each word
# The most_common method will limit the results to the top 10 words
# When this is printed, we get a list of tuples!
# where each tuple contains a word and a number of occurrences.
print(collections.Counter(words).most_common(10))
# The output:
# [('the', 28), ('to', 21), ('i', 15), ('a', 13), ('and', 12), ('he', 12), ('of', 11), ('her', 11), ('you', 11), ('be', 10)]
