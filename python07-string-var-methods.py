my_string = "Hello World!"

print(my_string)

# Not only can we store strings in variables,
# but we can also use the addition and multiplication operators in Python.
# Adding strings is called concatenation.

variable_one = "Hello"
variable_two = " World"
variable_three = "!"

# result="Hello World!"
result = variable_one + variable_two + variable_three
print(result)

avg = 94
# In JavaScript: we can concatenate a variable of string data type with a variable of numeric data type
# Example in Js console.log("My avg:" + avg) # OK only in JS => My avg: 94

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
# .upper() => uppercase
# .capitalize() => change the first letter in the sentence to uppercase
# .title() => making every word starts with uppercase

# NOTE: These methods will NOT change the original string variable

my_string = "HELLO WORLD!"
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

# isalpha() => returns True if all the characters are alphabet letters (a-z)
my_code1 = "abcd123"
# False => because not all the characters are letters, we have numbers: 1, 2, 3
print(my_code1.isalpha())

my_code2 = "abcdefg"
print(my_code2.isalpha())  # True => all are letters
