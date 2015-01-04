#!/usr/bin/env python
"""The test file for 'series.py'

Run this with py.test to check conditions in file.
"""

from series import fibonacci, lucas, sum_series

def test_fibonacci():
    my_list = []
    for i in xrange(9):    # Test first nine cases
        my_list.append(fibonacci(i))
    
    wiki = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    
    assert my_list == wiki


def test_lucas():
    my_list = []
    for i in xrange(9):    # Test first nine cases
        my_list.append(lucas(i))
    
    wiki = [2, 1, 3, 4, 7, 11, 18, 29, 47]
    
    assert my_list == wiki


def test_sum_series():
    my_list = []
    for i in xrange(9):    # Test first nine cases
        my_list.append(sum_series(i))    # Use default case
    
    wiki = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    
    assert my_list == wiki

