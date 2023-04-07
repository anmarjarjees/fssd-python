# For Loops:
# For loops allow us to iterate over a predefined set of data
# and will perform a task for each item in a given collection
# NOTE: for loop can iterate over a sequence that is a list, tuple, dictionary, set or string

# in JS:
# for (let count=1; count<11; count++)
# {
# write the code
# }

# In Python:
# you do not require an indexing variable to be set
# the "in" keyword is used in a for-loop

# Below is our JS array:
# let sports = ["Basketball", "Football", "Tennis", "Chess", "Swimming", "Running"];

# In Python we use the plain english word "List" to refer to an array variable:
# below is a list (array in JS)
# Like any other language, lists (arrays) in python are also 0 based index
languages = ["HTML", "CSS", "JavaScript"]

# Task: You need to loop and print each item (element) in "languages" list (array):
# In JS:
# for (var i=0; i<languages.length; i++) {
#     console.log(languages[i]);
# }

# for any_variable_name in a range() function
# language is just a variable name, you can put x, y, etc...
# languages is our list variable
for language in languages:
    print(languages)


# We can also loop through a string!
my_current_subject = "Python Fundamentals"

# Like JS, Python string characters have index values that start with 0

# for loop to print every single character in the string variable my_current_subject
for character in my_current_subject:
    print(character)

# Or do it in the same line:

# instead of creating a new variable:
# centre_name = "Code Institute"
# for character in centre_name:
print("")
for character in "Code Institute":
    print(character)


# The range() function:
# we need to loop from min 1 to maximum 10 (from 1 to 10)
# we need to use range() function to give us the range of numbers from 1 to 10
# When we quickly need to generate a sequence of numbers, we can use the range() function
# the "long syntax" range(1,11) to specify the starting value
for count in range(1, 11):
    print(f"Count number (for loop1): {count}")

# use the "short syntax" range(11) will start from 0 by default
# output: 0 to 10
for count in range(11):
    print(f"Count number (for loop2): {count}")

# In JS we used for loop to print: 0 2 4 6 8 10
# we incremented our loop counter by 2 => i +=2
#   for (let i = 0; i < 11; i += 2) {
#             document.write(i + "<br>");
#         }

# range(value1,value2,value3)
# value1 is the starting number
# value2 is the maximum number to reach -1 (value2 will not be included)
# value3 is the increment (if it's positive) / decrement (if it's negative)
# range(0,11,2)
# 0: the starting value will be 0
# 11: the last value will be 10
# 2: the loop counter will be incremented by +2
# using range to output even numbers from 0 to 10:
for even_number in range(0, 11, 2):
    print(f"Even number (for loop3): {even_number}")

# using range to output odd numbers from 9 going down to 1:
# Going/starting form the highest value to the lowest one
# We have to use the -
for odd_number in range(9, 0, -2):
    print(f"Odd number (for loop4): {odd_number}")

# Your last challenge of this topic is to:
# Use the range() function to print the numbers from 0 to 255, inclusive.
for number in range(256):  # We need to remember putting 256 to get the max value of 255
    print(number)


# Task: Print 1 to 10
# You can try it using pythontutor
# In JS:
# var count = 1;
# while (count<11) {
#     console.log(count);
#     count++;
# }

# ***********
# While Loop:
# ***********
# we use while loops that will run while some condition is True
# In Py:
count_num = 1
while count_num < 11:  # this while loop will stop when count_num value became 11
    print(f"Count number: {count_num}")
    # in Py: we don't increment/decrement operators count_num++
    # Solution1: using the full formula
    # count_num = count_num + 1
    # Solution2: using the shorthand
    count_num += 1

# Example:
play_game = True

while play_game:  # this while loop will stop when play_game value became False
    # while loop will keep running while play_game = True
    continue_playing = input(
        "Would you like to continue playing the game? y/n ")
    # We have two options either y or n, plus one extra option: the user might enter invalid value
    # if then elif then else

    # We can determine if the user will input "y" or "Y"
    # if continue_playing=="y" or continue_playing=="Y":
    # OR: using the lower() method for the string (object-class)
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("We will stop the game.")
        # we need to stop this while loop by changing play_game value to be False
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")
# Python-Specific Core Concepts => Python Iteration => While Loops Challenge

# Nested Iteration:
i = 2
while i < 10:
    j = 2
    while j <= i/j:  # while 2 <= 1
        if not i % j:
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1

# The output:
# 2 is a prime number
# 3 is a prime number
# 5 is a prime number
# 7 is a prime number
