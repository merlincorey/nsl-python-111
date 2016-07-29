'''Python 101 Review function prompts.
Create the review_local.py file with your local changes, which will automatically be imported.'''

def factorial(n):
    return str(n)

try:
    from review_local import *
except ImportError:
    pass
