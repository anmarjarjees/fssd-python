# Break and Continue
# Break: Allows us to break out of a loop (while and for)

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

# break (stop) the loop
counter = 0
while counter < len(fruits):
    print(fruits[counter])
    counter += 1  # In python we don't counter++ sa we used to have in JS
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

# using the break with for loop
# remember that fruit is just a variable that will represent each element in fruits list
for fruit in fruits:
    if fruit == "peach":
        break
    print(fruit)

print("*********************")
print("***** Continue: *****")

# Continue: Allows us to skip an iteration in a loop (Jump the current iteration)
# Task: Print all the fruits except the "peach" fruit
# We need to skip our loop (Don't print) when the value is "peach"
# and just continue (jump) to the next element in our list
counter = 0
while counter < len(fruits):
    # You want to break (stop) the loop when we reach the element named "peach"
    if fruits[counter] == "peach":
        counter += 1
        # continue: means don't complete the code (ignore the rest: ignore the loop counter)
        # just return to the while loop
        continue  # will ignore all the lines of code that written after!!!
    print(fruits[counter])
    counter += 1

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
