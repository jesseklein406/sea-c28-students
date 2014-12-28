#!/usr/bin/env python

"""Use this module to access the 'function_builder' function
"""

def function_builder(n):
    """Generate a list of functions that increment an input value
    by a number corresponding to the index value in the list
    """
    result = []
    for i in xrange(n):
        result.append(lambda x, y=i: x + y)    # Pass y as a keyword argument and bind it to i
    return result

