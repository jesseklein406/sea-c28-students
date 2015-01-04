#!/usr/bin/env python
"""The test file for 'ack.py'

Run this with py.test to check conditions in file.
"""

from ack import ack, wiki, my_list

def test_ack():
    for i in xrange(4):
        for j in xrange(5):
            my_list.append(ack(i, j))
    
    assert wiki == my_list
