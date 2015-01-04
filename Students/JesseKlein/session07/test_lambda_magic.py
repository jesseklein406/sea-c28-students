#!/usr/bin/env python
"""The test file for 'lambda_magic.py'

Run this with py.test to check conditions in file.
"""

from lambda_magic import function_builder

def test_function_builder():
    my_list = []
    for i in xrange(4):
        for j in xrange(4):
            my_list.append(function_builder(4)[i](j))
    
    expected_values = [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6]

    assert my_list == expected_values

