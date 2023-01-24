# Basic Math With Arithmetic Operators:
# + => Addition => result = a + b => 2 + 2 = 4

# - => Subtraction => result = a - b => 2 - 2 = 0

# * => Multiplication => result = a * b => 2 * 5 = 10

# / => Division => result = a / b => 10 / 2 = 5

# ** => Exponentiation => result = a ** b => 2 ** 3 = 8

# % => Modulo (returns the remainder)
# - The remainder is 0 for even numbers
# - The remainder is 1 for odd numbers
# result = a % b => 10 % 4 = 2

# // => Floor Division (Python only, returns the rounded down quotient)
# result = a // b => 10 // 3 = 3

# Important Note:
# An important thing to note is that when we use the division operator,
# the result is always a float. Even if the division returns a whole number,
# it will be returned as a float.

print(4 / 2)  # output 2.0

print(5 * 2)  # output 10

print(15/3)  # 5.0

print(18/2)  # 9.0

# Notice that the result here are 5.0 and 9.0
# The point accommodates the possibility that the result
# might not be a whole number

print(9/4)  # 2.25

# to summarize:
# In Python 3, whenever we use the division operator,
# the result will always be a float.


# Exponent:
# Exponent means to the power of.
# the result of 2 to the power 3
# find: 2 * 2 * 2
# in Py: 2**3 => 2 to the power of 3 => 2 * 2 * 2
print(2 ** 3)  # 2 * 2 * 2 => output is 8

# Modulo:
# The modulo operator divides the first number by the second and returns the remainder.
# Modulo % => to return the remainder of division
# Example:
# 5 / 5 => the answer will be 1
# 5 % 5 => the answer will be 0
print(4 % 2)  # the remainder is 0 because: even number % 2 => 0

# A common use for the modulo operator is when we need to find out
# if numbers are odd or even.
# An even number is always divisible by 2 so % 2 will always return:
# 0 for even
# and 1 for odd
# As we did in JavaScript

# more example of exponent **
# find the result of 4 to the power of 2
# 4 * 4
print(4**2)  # output 16
# or
print(4 * 4)  # output 16

# 5 to the power of 10!
print(5**10)


# Floor Division, the symbol is // to be explained later

# BEDMAS

# print the average of these two numbers 90 and 93:
print((90+93)/2)  # 91.5

print((1+1)**3)  # (1+1) => 2 ** 3 => 2 * 2 * 2 = 8

# Also using PEDMAS or BEDMAS basic rule for Math operation that computer also follows


# the symbol for floor division //
# It rounds the number down to the nearest whole number.
print(15//3)  # output (int): 5
print(18//2)  # output (int): 9

print(14/3)  # output: 4.666666666666667 # Yes, later we will round() function
print(14//3)  # 4 #  return 4 (without any decimal points)


# int number + float number => the result will be float
print(4 + 4.0)  # 8.0

# Currency Converter:
# Let’s say that 1 euro is equal to 1.11 in USD
# Q) how many USD one would get for 25 euro
# A) multiply 25 by 1.11

# Hint
# Create a variable to be used multiple times
# if the rate is changed we can just change this variable value:
usd = 1.11
print(25 * usd)

print(35 * usd)

print(75 * usd)

# the output:
# 27.750000000000004
# 38.85
# 83.25000000000001

# round() function:
# ******************
# Below we will use round() function to make these number very friendly

# syntax round( the number we need to round, number of decimal points )
# we have to specify: he number we need to round
# optional: number of decimal points
my_complex_number = 7.6666666666666
# nesting functions:
print(round(my_complex_number, 2))  # 7.67

euro = 25
total_usd = round(euro * usd, 2)
print(total_usd)  # 27.75

# your task to write the equation of converting Feh to Cel or vice-versa

# Task1:
# Step1: declare or define a variable, feh_degree, to contain any integer number
# which is the value in feh

# Step2: write the equation and use round function
# To convert Fahrenheit to Celsius simply do: (Fahrenheit - 32) * 5/9
# modify the equation below based on the formula:
feh_to_cel_equation = 0

# output the feh_to_cel_equation variable
print(feh_to_cel_equation)

# Task2:
# Step1: declare or define a variable, cel_degree=, to contain any integer number
# which is the value in cel

# Step2: write the equation and use round function
# Convert Celsius to fahrenheit by applying the following formula: Celsius * 9/5 + 32
# modify the equation below based on the formula:
cel_to_feh_equation = 0

# output the cel_to_feh_equation variable
print(cel_to_feh_equation)


# ===========================
# Incrementing & Decrementing
# ===========================
# The Increment/Decrement arithmetic operator is placed before the assignment operator
# The ways these operators work is by combining the arithmetic operator with the = assignment operator,
# += => Addition And
# The += is used:
# 1) to increment a variable by adding a value
# 2) and reassigning the result to the variable

# -=
# *=
# /=
# **=
# %=
# //=

# Examples:
variable_one = "hello "
variable_two = "world"

variable_one += variable_two
print(variable_one)
print(variable_two)

x = 2
x **= 3
print(x)  # 8
