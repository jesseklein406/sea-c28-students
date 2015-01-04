#!/usr/bin/env python
"""The test file for 'series.py'

Run this with py.test to check conditions in file.
"""

from rot13 import rot13

def test_rot13():
    #This is all the punctuation on a normal keyboard.
    #It is unaffected by "rot13()".
    punctuation =  "_ ',.?/:;<>[]{}|`~!@#$%^&*()-=+"
           
    assert rot13(punctuation) == punctuation
    
    #These two sets of letters map onto each other"
    
    lower_half = "abcdefghijklmABCDEFGHIJKLM"
    upper_half = "nopqrstuvwxyzNOPQRSTUVWXYZ"
        
    assert rot13(lower_half) == upper_half
    assert rot13(upper_half) == lower_half

