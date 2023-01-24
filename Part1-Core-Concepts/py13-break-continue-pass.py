# Break, Continue, and Pass

# The "break" statement allows you to exit from the loop based on an external condition.
# The loop will finish at that point

# Break: Allows us to break out of a loop (while and for)

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

# break (stop) the loop
counter = 0
while counter < len(fruits):
    print(fruits[counter])
    counter += 1  # In python we don't have counter++ as we used to have in JS
    break

print("****************")

# Task: Print all the fruits till we reach the "peach" fruit
# We need to break our loop (Don't print) when the value is "peach"
counter = 0
while counter < len(fruits):
    # You want to break (stop) the loop when we reach the element named "peach"
    if fruits[counter] == "peach":
        break

    print(fruits[counter])
    counter += 1  # In python we don't counter++ sa we used to have in JS

print("****************")

# Let's do it using for loop:
# using the break with for loop
# remember that fruit is just a variable that will represent each element in fruits list
for fruit in fruits:
    if fruit == "peach":
        break
    print(fruit)

print("*********************")
print("***** Continue: *****")

# Continue: Allows us to skip an iteration in a loop (Jump the current iteration)
# The continue allows you to skip over part of the loop based on an external condition.
# However, the program will go back to the beginning of the loop and continue.

# Task: Print all the fruits except the "peach" fruit
# Our list has these values: ["apple", "banana", "peach", "pear", "plum", "orange"]
# We need to skip our loop (Don't print) when the value is "peach"
# and just continue (jump) to the next element in our list
counter = 0
while counter < len(fruits):
    # You want to jump the current iteration of the loop when we reach the element named "peach"
    if fruits[counter] == "peach":
        counter += 1
        # continue: means don't complete the code (ignore the rest: ignore the loop counter)
        # just return to the while loop
        continue  # will ignore all the lines of code that written after!!!

    print(fruits[counter])
    counter += 1  # In python we don't have counter++ as we used to have in JS

# apple
# banana
# pear
# plum
# orange

print("********* Without using 'continue' keyword: ************")
# Yes, we can do the same logic without using the "continue" python keyword:
# Task: Print all the fruits except the "peach" fruit
counter = 0
while counter < len(fruits):
    # You want to break (stop) the loop when we reach the element named "peach"
    if fruits[counter] != "peach":
        print(fruits[counter])
    counter += 1

# The pass statement allows you to handle the condition without the loop being affected in any way.
# The loop will carry on as normal.
# The pass statement is frequently used when developing to allow code to run
# before you have fully figured out the logic you intend.

# This loop will print from 0 to 9
print("Using pass with for loop:")
for number in range(10):
    if number == 5:
        # Yes I want to add my code later!
        # The pass statement is used as a placeholder for future code
        # the solution, using the keyword "pass"
        pass
    print(f'Number is  {number}')

# The output
# Number is  0
# Number is  1
# Number is  2
# Number is  3
# Number is  4
# Number is  5
# Number is  6
# Number is  7
# Number is  8
# Number is  9

print('Left the loop')

# break => Both JS and Py => Exits the entire loop
# continue => Both JS and Py => Skips the current iteration
# pass => Python only => Skips the current code block

# In JavaScript , there is no pass statement ,
# but you can accomplish the same thing by leaving the
# curly braces empty and inserting a code comment to let the reader know that nothing is supposed
# the same example using: JavaScript (You can use PythonTutor)
# for number in range(10):
# for(let number=0; number < 11; number++) {
#     if (number == 5) {
#       // I don't have the time to write my code
#       // I don't have the instructions
#       // Just placing my if condition
#     }
#     console.log('Number is '+number)
# }

# You can check more about using "pass" keyword in Python:
# W3Schools Link: https://www.w3schools.com/python/ref_keyword_pass.asp
