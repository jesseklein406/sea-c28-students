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


if __name__ == '__main__':
    assert [function_builder(5)[i](0) for i in xrange(5)] == [0, 1, 2, 3, 4]

