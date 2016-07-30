'''
Python 101 Review function prompts.
Create the review_local.py file with your local changes, which will automatically be imported.
You can do so by simply copying this file and editing the function bodies.

Each function has a docstring with information about its expected operation and outputs.
'''

def square(n):
    '''The square of a number is the product of that number times itself.'''
    return n


def factorial(n):
    '''A factorial is the product of all positive integers from 1 to n.
    Where n is a positive integer.
    Factorials are used to count combinations of sets.
    Negative integers should return None.'''
    return None


def blackbox(n, m):
    '''Can you figure out the black box?'''
    return 0

###
### You can remove this from review_local.py if you want
### HOWEVER, python deals with circular imports by not allowing them
### Therefore, you can leave this in, and your review_local.py should work
###
try:
    from review_local import *
except ImportError:
    pass
