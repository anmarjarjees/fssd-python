# numbers: int and float
# int => whole number (no decimal points)
# float => decimal numbers (fractions)

print(15/3)  # 5.0

print(18/2)  # 9.0

# Notice that the result here are 5.0 and 9.0
# The point accommodates the possibility that the result
# might not be a whole number

print(9/4)  # 2.25

# to summarize:
# In Python 3, whenever we use the division operator,
# the result will always be a float.

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
print(round(my_complex_number, 2))  # 7.67


euro = 25
total_usd = round(euro * usd, 2)
print(total_usd)  # 27.75

# your task to write the equation of converting Feh to Cel or vice-versa

# Task1:
# Define a variable, feh_degree, to contain any integer number
# which is the value in feh

# write the equation and use round function
# To convert Fahrenheit to Celsius simply do: (Fahrenheit - 32) * 5/9
feh_to_cel_equation = 0
# output the feh_to_cel_equation variable
print(feh_to_cel_equation)

# Task2:
# Define a variable, cel_degree=, to contain any integer number
# which is the value in cel

# write the equation and use round function
# Convert Celsius to fahrenheit by applying the following formula: Celsius * 9/5 + 32
cel_to_feh_equation = 0
# output the cel_to_feh_equation variable
print(cel_to_feh_equation)
