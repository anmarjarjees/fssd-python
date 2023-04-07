fruits = ['apple', 'orange', 'banana', 'pear', 'plum']
# Slicing Lists
# Here we’ve added [0:2] to the end of our list which is called slice notation.
# It works like a combination of indexing and range.
# First, we indicate the index at which we wish to start.
# Then after the colon (:), we use the index at which we want to stop.
# Similar to the range function, the stop value is the everything up to, but not including, that value.
# Here it will, therefore, include everything up to index 2, except for index two itself.
# If we wanted to start at the very beginning of a list, we could just say [:2].

# Example 1: We want to take the two first items/elements in the list fruit:
# ["apple", "banana"]
print(fruits[0:2])  # ['apple', 'banana']

my_fav_fruits = fruits[0:4]
print(my_fav_fruits)  # ['apple', 'banana', 'peach', 'pear']

# We will use print:

# Will start from index 0 by default
print(fruits[:2])  # ['apple', 'banana']

# Will start from index 4 and will continue till the rest by default
print(fruits[4:])  # ['plum']

# Without specifying the starting index and the end index
# Will take all the array elements by default
print(fruits[:])  # ['apple', 'banana', 'peach', 'pear', 'plum', 'orange']

# Will start from index 0
# Remember that index 4 will not be included (it will stop by index 4)
# so it will count from index 0 to index 3
# The last value 2 will start from 0 +2
# index 0 => 'apple' and plus 2 index 2 => peach and plus 2 index 4 (not included)
print(fruits[0:4:2])  # ['apple', 'peach']

print(fruits[0:4:3])  # ['apple'.'pear']

some_fruits = fruits[1:4]  # the elements in index 1, 2, 3
print(some_fruits)  # ['banana', 'peach', 'pear']

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(letters[0:6])  # ['A', 'B', 'C', 'D', 'E', 'F']
print(letters[0:])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(letters[0:7])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# The following code will take the items with these indexes: 0, 2, 4, 6
print(letters[0:7:2])  # ['A', 'C', 'E', 'G']

# Tuples: provide us with another means (format) of storing collections of data
# Tuples are also 0 based index
my_tuple = ("Hello", "World")  # it's ( ) not [ ] like a list
# to access any element in teh tuple structure we use the [ ]
print(my_tuple[1])  # World

my_languages = ("HTML", "CSS", "JavaScript", "Python")
print(my_languages)  # ('HTML', 'CSS', 'JavaScript', 'Python')
print(f"Our current programming language is: {my_languages[3]}")
# output: Our current programming language is: Python

# we can loop through the tuple structure as we did with list (array):
for language in my_languages:
    print(language)

# using method count():
# W3schools link: https://www.w3schools.com/python/ref_tuple_count.asp
print(my_languages.count("HTML"))

rand_nums = [100, 200, 100, 500, 600, 200, 100, 300]
print(rand_nums.count(100))  # 3
