# Below: we have imported the division function from the helpers.py module,
# by using "from helpers import division"
# which allows us to use the division function
from helpers import division

# using the division() syntax directly
print(division(4, 2))

# Notice that we do not have access to the mod function
# unless we also add a from helpers import mod statement in main.py.
# so the code below will generate an error:
# print(mod(4, 2))

list_integers = [1, 2, 3, 4, 5]
# The code below will also generate errors:
"""
addition = helpers.add_integers(list_integers)
print(addition)

multiplication = helpers.multiply_intergers(list_integers)
print(multiplication)
"""
