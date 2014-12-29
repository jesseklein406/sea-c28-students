#!/usr/bin/env python
"""Use this module to access the 'count_evens' function"""

def count_evens(nums):
    """Use this function to get a count of even numbers in a list.

    Input list of numbers as the only argument. Return integer.
    """
    return len(filter(lambda x: not x % 2, nums))    # Bind evens to True

