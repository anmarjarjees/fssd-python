# Third Party Libraries:
# Libraries created for Python => Pre-written code

"""
In addition to the built-in libraries, 
as Python is open source, anyone can create software and share it with the community.
A library is a collection of modules that have some common functionality. 
There is a Python Package Index (pypi.org) where these open source projects are shared.
"""

# Python Frameworks Modules, and Libraries:
# - NumPy
# - pandas
# - Scrapy
# - django


# using/importing a third-party library named numpy.
# It is a widely used library for scientific computing.
# It extends the abilities of Python into scientific computing

# NOTE: We can give the package name an alias (np in this case),
# so we don’t have to type it out each time.
# **************************************************************

# NOTE:
# If you were trying this on your computer,
# you would have to install numpy locally as it is a third-party library
# rather than a built-in library installed with Python.
# Otherwise, receiving error: ModuleNotFoundError: No module named 'numpy'
# **********************************************************************
import numpy as np

# creating a simple one-dimensional array
a = np.array([1, 2, 3])

print(a)

# Challenge: Third Party Libraries
# Steps:
# 1. At the top of the python file,
# import the parser function from the "dateutil" module

# When you import this and click run,
# it could take under a minute to install this package
# before your program will show the output .
# So make sure your program works before attempting to run tests and submit.
