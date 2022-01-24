# random()
# built-in library
# Provides pseudo random numbers

import random

# generate a random float, integer or choice
print(f'A random float between 0 & 1.0: {random.random()}')
print(f'A random int between 0 & 10: {random.randrange(11)}')
print('A random choice from a list: ' +
      random.choice(['paper', 'scissors', 'rock']))
deck = ['hearts', 'diamonds', 'spades', 'clubs']

# You can also shuffle existing data structures:
random.shuffle(deck)
print(deck)

# read more: https://docs.python.org/3/library/random.html

# Challenge: io
# Steps:
# 1. import random
# 2. Define a function named ten_rand_nums (that takes no parameters)
# and that returns a list of 10 random integers between 0 and 100
# 3. Call the ten_rand_nums function
# and assign the returned value to a variable named result
# 4. Print the value of the result list to the terminal
# 5. Use the shuffle method of the random library to shuffle the result list
# 6. Print the value of the result list to the terminal again
