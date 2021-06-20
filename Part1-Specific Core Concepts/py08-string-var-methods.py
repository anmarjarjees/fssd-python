my_string = "Hello World!"

print(my_string)

# Not only can we store strings in variables,
# but we can also use the addition and multiplication operators in Python.
# Adding strings is called "concatenation".

variable_one = "Hello"
variable_two = " World"
variable_three = "!"

# result="Hello World!"
result = variable_one + variable_two + variable_three
print(result)

avg = 94
# In JavaScript: we can concatenate a variable of string data type with a variable of numeric data type
# Example in Js console.log("My avg:" + avg) # OK only in JS => My avg: 94
# Because JS will implicitly convert the numeric data type to a string

# In Python we CANNOT do it!
# We can NOT concatenate a variable of string data type with a variable of numeric data type
# print("My average: " + avg)
# The output => TypeError: can only concatenate str (not "int") to str

# Override our variable my_string
my_string = "boo"

result = my_string * 2
print(result)  # booboo
# Python takes the string and will append the same string to the end of the first variable
# as many times as we multiply it by, which in this case is 2.

nice = "very nice! " * 3
print(nice)  # very nice! very nice! very nice!

# ***************
#  String Methods
# ***************

# We use string methods by using a dot (.) after the string variable,
# followed by the method name and a pair of brackets [like Js, functions and methods end with ( and )].

# .lower() => lowercase (Review: in JavaScript .toLowerCase())
# .upper() => uppercase (Review: in JavaScript .toUpperCase())
# .capitalize() => change the first letter in the sentence to uppercase
# .title() => making every word starts with uppercase

# NOTE: These methods will NOT change the original string variable

my_string = "HELLO WORLD!"
print(my_string.capitalize())  # Hello world!
print(my_string)  # HELLO WORLD!

my_string_lower = my_string.lower()
# this variable "my_string_lower" will be always in lowercase unless if we change it
print(my_string_lower)


one_more = "NICE WEATHER"
one_more.lower()  # A temporary change only on this line
# just on the next line one_more will return to its original value which is all in Capital
print(one_more)  # NICE WEATHER
# OR:
print(one_more.lower())  # nice weather

my_string_2 = "hElLo WorLD"
my_string_2_upper = my_string_2.upper()
print(my_string_2_upper)

my_string_3 = "good morning everyone!"
my_string_3_capitalize = my_string_3.capitalize()
print(my_string_3_capitalize)  # capitalize the first letter of the first word
# Output: Good morning everyone!

my_string_4 = "one more time good morning everyone!"
my_string_4_title = my_string_4.title()
print(my_string_4_title)  # capitalize every first letter of each word
# Output: One More Time Good Morning Everyone!

# .replace("text1","text2") => replace text1 with text2
# if "text1" doesn't exist, no replace will take place
my_paragraph = "Hi there, I like to learn JavaScript, it's very good idea to learn JavaScript if you want to work as a programmer!"

my_paragraph2 = my_paragraph.replace("JavaScript", "Python")
print(my_paragraph2)
# Output: Hi there, I like to learn Python, it's very good idea to learn Python if you want to work as a programmer!
# replace will NOT change the original string inside the variable "my_paragraph"
print(my_paragraph)

# isalpha() => The .isalpha() method checks to see if the variable my_string is fully alphabetic
# returns True if all the characters are alphabet letters (a-z)
my_code1 = "abcd123"
# False => because not all the characters are letters, we have numbers: 1, 2, 3
print(my_code1.isalpha())  # False

my_code2 = "abcdefg"
print(my_code2.isalpha())  # True => all are letters

my_code2 = "12"
print(my_code2.isalpha())  # False

my_code2 = "90.78"
print(my_code2.isalpha())  # False

# We can use this method object_name.isalpha() to validate the user input
# if it's a number or sting
# In JS we used a function named "isNaN()" to determain if the value is number or not
# isNaN(myTestVariable)

print("the string method join(): ")
print("=====================")
# Python String join() Method
# join() =>	concatenates string
# W3schools:
# The join() method takes all items in an "iterable"* and joins them into one string
# A string must be specified as the separator
# Iterable variables/data types => lists, tuples, dictionaries

# Examples:
full_title_tuple = ("Microsoft", "Visual Studio Code", "IDE")
full_title = " ".join(full_title_tuple)
print("Our current app: "+full_title)


# Let's create a tuple varaible "mition":
motion = ("jump", "walk", "run")
print(type(motion))
print((motion))
new_string = "ing ".join(motion)
print(new_string)

# Important Conclusion:
# Can you see why the new string does not end with "running"?
# Join in python is analogous to the usage in English.
# If you join two items together with glue, then you would only apply glue to the inner surfaces.

# On more example:
# Join all items in a dictionary into a string, using a the word " and " as separator:
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values
myDict = {
    "name": "John",
    "country": "Norway"
}

mySeparator = " and "
joined_string = mySeparator.join(myDict)

print(joined_string)

# The .split() method:
# splits the string at the character you've specified and returns the new strings as a list
# The .strip() method strips any empty space before or after a string and returns the trimmed string
# W3schools:
# The split() method splits a string into a list
# You can specify the separator, default separator is any whitespace
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one


# Example1: Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
split_result1 = txt.split()
print(type(split_result1))  # <class 'list'>
print(split_result1)  # ['welcome', 'to', 'the', 'jungle']

# Example2: Split the string, using comma, followed by a space, as a separator:
txt = "Hello!, we are studying Python, our next module is about Flask Framework"
split_result2 = txt.split(", ")
print(split_result2)
# ['Hello!', 'we are studying Python', 'our next module is about Flask Framework']

# Example3: Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
split_result3 = txt.split("#")
print(split_result3)  # ['apple', 'banana', 'cherry', 'orange']

# # Example4: Split the string into a list with max 2 items:
txt = "Learning Python after JavaScript is interesting!"
# setting the maxsplit parameter to 2, will return a list with 3 elements!
split_result4 = txt.split(" ", 2)
# ['Learning', 'Python', 'after JavaScript is interesting!']
print(split_result4)

# ===========================================================================
# string methods:
# Method	Description
# capitalize()	Capitalizes the first character of the string
# center()	Centers string
# count()	Returns a count of times a specified value occurs in the string
# encode()	Returns an encoded version of the string (use decode() to decode)
# endswith()	Returns True if the string ends with a specified suffix
# expandtabs()	Sets the tab size in spaces of the string
# find()	Returns the lowest index position of where a specified character was found
# index()	Searches for a specified value and returns the position of where it was found or an error if not found
# isalnum()	Returns True if all characters are alphanumeric
# isalpha()	Returns True if all characters are alphabetic
# isdigit()	Returns True if all characters are digits
# islower()	Returns True if all characters are lower case
# isspace()	Returns True if all characters are whitespace
# istitle()	Returns True if the string is titlecased
# isupper()	Returns True if all characters in the string are upper case
# join()	concatenates string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# partition()	Returns a tuple where the string is parted into two strings and the separator
# replace()	Returns a string where a old value is replaced with a new value
# rfind()	Searches highest index in the string for a specified value
# rindex()	Same but with error if nothing found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into uppercase
# zfill()	Fills the string with a specified number of 0 values at the beginning
