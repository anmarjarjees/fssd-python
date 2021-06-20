# Sequences, Indexing and Lists
# Ask the user to input any string and save it into a variable named "my_string":
my_string = input(
    "Input any text and we will tell you how many characters you have in your text (the length): ")


# In JavaScript, we have the "length" property to be used with arrays and strings
# in Python we have a "function" named len() to give us the length of any text
# Let's suppose if len() was a method for string class => my_string.len()
# but len() is a function => len(my_string)
print(len(my_string))
# Remember that in JS myString.length as a property

# Like in JS we had strings and arrays to start counting from 0
# Same in Python => String and List have their index values to start from 0
print(
    f"So your first character in your text is \"{my_string[0]}\", and your second character is \"{my_string[1]}\"! Look we know everything")


# If you put only one charater => IndexError: string index out of range
# example
for one_char in my_string:
    print(one_char)


# When we have a group of items,
# we can store them in a list, so we have them all in the one place
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

print(fruits)  # output: ['apple', 'banana', 'peach', 'pear', 'plum', 'orange']

# To recap in JS:
# document.write("<ul>")
# for loop => document.write("<li>fruits[i]</li>")
# document.write("</ul>");

# or for loop:
for fruit in fruits:
    print(fruit)

# Let's print the second fruit which is in oue case is "banana" name in fruits:
print("Our second fruit is: ", fruits[1])  # Our second fruit is:  banana

# let's do the same using while loop:
# Use While loop structure to print the elements of fruits list
# Use the len() function to find the length of fruits list

# Please be advised that this loop counter will represent the index values of fruits list
# We know that computer (list in Py) is 0 based index so we need to start with 0

# Another example for looping through a list using range() function:
foods = ['bacon', 'sausage', 'egg', 'spam']

for ind in range(len(foods)):
    # In this example only the index is iterated over not the value
    print(ind, foods[ind])
print(foods)
# In this case we need to calculate the length of the foods collection
# Then we generate a range of integers equal to that length
# Then we iterate over that range of integers

# Try this challenge:
# Steps
# 1. Create a variable named users and assign it a list value of ['anna', 'chris', 'brian']
# 2. Using the range() and len() methods, create a for loop that loops over the users list.
# 3. Inside the for loop, use the capitalize() method to update each entry so that each name starts with a capital letter.
# 4. Outside the for loop, print the users list to check you have the correct output.

# While loop structure has 3 requirements (like for loop):
counter = 0  # Step 1. the initial value of our loop counter
while counter < len(fruits):  # Step 2. the condition to keep the loop running
    # print the elements of this array:
    print(fruits[counter])
    # we need NOT to foreget changing the loop counter
    counter += 1  # Step 3. the counter value has to be incremented/decremented

# Sometimes we can use while loop without a loop counter like for loop
