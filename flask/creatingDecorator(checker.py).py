""" a decorator is just another function, which takes a function object as an argument
Note:
 1.A decorator is a function
 2.A decorator takes the decorated function as an argument
 3.A decorator returns a new function
 4.A decorator maintains the decorated function’s signature"""

from flask import session
# Note: When creating your own decorators, always import, then use, the “functools” module’s “wraps” function.
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # * means expand values and ** means expand to a dictionary of key and values
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are not logged in'

    return wrapper


""" note: When a decorator is applied to an existing function, any calls to the existing function are replaced by calls
 to the function returned by the decorator."""

# General template to create a decorator
"""
from functools import wraps 
def decoraor_name(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
    # 1. Code to execute before calling the decorated function.
    
    # 2. Call the decorated function as required, returning its results if needed
        return func(*args, **kwargs)
    # 3. Code to execute instead of calling the decorated function.
    return wrapper
"""
