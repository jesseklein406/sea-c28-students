#!/usr/bin/env python
"""Generators for some mathematical sequences

Generators:
intsum -- produce a running sum of integers
doubler -- produce values that increase by a factor of two
fib -- produce Fibonacci numbers
prime -- produce prime numbers
"""

def intsum():
    """Produce a running sum of integers, beginning at zero"""
    i = 0
    j = 0
    while True:
        i = i + j
        yield i
        j += 1


def intsum2():
    """Produce a running sum of integers, beginning at zero"""
    return intsum()


def doubler():
    """Produce values that increase by a factor of two, beginning at one"""
    i = 0
    while True:
        yield 2**i
        i += 1


def fib():
    """Produce Fibonacci numbers"""
    i = 0
    j = 1
    while True:
        i = i + j
        yield j
        i, j = j, i


def prime():
    """Produce prime numbers"""
    i = 2
    while True:
        if not 0 in [i % j for j in xrange(2, i)]:
            yield i
        i += 1

