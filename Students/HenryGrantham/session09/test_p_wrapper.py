#!/usr/bin/env python

"""
code that tests the p-wrapper decorator defined in p_wrapper.py
can be run with py.test
"""

import p_wrapper as pw


def test_Empty():
    string = ''
    comparestring = '<p>  </p>'
    assert pw.return_a_string(string) == comparestring


def test_numbers():
    string = '12345'
    comparestring = '<p> 12345 </p>'
    assert pw.return_a_string(string) == comparestring


def test_sentence():
    string = 'This is a sentence of words.'
    comparestring = '<p> This is a sentence of words. </p>'
    assert pw.return_a_string(string) == comparestring


def test_symbols():
    string = '!@$#!@$%@$#%'
    comparestring = '<p> !@$#!@$%@$#% </p>'
    assert pw.return_a_string(string) == comparestring
