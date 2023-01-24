# Python String Output Format:
# We can format out output using any one from the following 3 ways:

# First Simple Example:
your_num = 10

# Output: "Your number is 10"

# First Way: Concatenating (like JS) with the symbol "+", using str() function [only if needed]:
# remember that "your_num" has numeric value
# Python CANNOT concatenate numeric data types with strings using +
# we need to use the built-in function named "str()"
print(str(your_num) + "is equal to 10")

# Second Way: Using %s
print("%s is equal to 10" % your_num)

# Third Way: The "modern" way: using f-strings
print(f"{your_num} is equal to 10")
# NOTE: It is also valid to use the capital letter F
# The only consideration required to use f-strings is your version of python,
# which needs to be version 3.6 or above

# Let's take this example:
# we have 4 variables:
first_name = "Alex"  # string value and string data type
last_name = "Chow"  # string value and string data type
program_name = "FSSD"  # string value and string data type
age = 28  # numeric value and numeric data type

# Task output: "Alex Chow is one of our FSSD program students. His age is 28, good luck Mr. Chow!"
# Now, we can't use this way by typing the text literally! We need to use our variables:
print("Alex Chow is one of our FSSD program students. His age is 28, good luck Mr. Chow!")

# First Way: using str() function [if needed] with the concatenating symbol +:
print(first_name + " "+last_name + " is one of our " +
      program_name + " program students. His age is "+str(age)+", good luck Mr. "+last_name+"!")

# Second Way: Using %s
# print("%s is equal to 10" % your_num)
print("%s %s is one of our %s program students. His age is %s, good luck Mr. %s!" %
      (first_name, last_name, program_name, age, last_name))

# Third Way: The "modern" way: using f-strings
# print(f"{your_num} is equal to 10")
print(f"{first_name} {last_name} is one of our {program_name} program students. His age is {age}, good luck Mr. {last_name}!")
