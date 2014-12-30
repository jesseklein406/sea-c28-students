#!/usr/bin/env python

"""
Generators for:

Sum of integers
Doubler
Fibonacci sequence
Prime numbers

"""
from math import sqrt


def intsum():
    """Generates numbers that are in the sequence 0 + 1 + 3 + 6 + 10 + 15 +
    """
    i = 0
    sum = 0
    while True:
        yield sum
        i += 1
        sum = sum + i


def intsum2():
    """Generates numbers that are in the sequence 0 + 1 + 3 + 6 + 10 + 15 +
    """
    n = 1
    while True:
        yield (n * (n - 1)) / 2
        n += 1


def doubler():
    """Generates numbers where each value doubles the last value
    """
    i = 1
    while True:
        yield i
        i *= 2


def fib():
    """Generates numbers in a fibonacci sequence: f(n) = f(n-1) + f(n-2)

    f2 represents n - 2 and f1 represents n - 1
    """
    f2, f1 = 0, 1
    while True:
        yield f1
        f2, f1 = (f1, f1 + f2)


def prime():
    """Generates prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """
    n = 2
    while True:
        # This is special case of only even number that is prime
        if n == 2:
            yield 2
        else:
            # This line rules out all even numbers after 2
            if n % 2:
                # Only has to test up to sqrt of n (then add one for range)
                if not [i for i in range(3, int(sqrt(n)) + 1) if n % i == 0]:
                    # print("%i is divisable by %i" % (n, i))
                    yield n
        n += 1



def square():
    """Generates a sequence of squares.
    """
    n = 1
    while True:
        yield n ** 2
        n += 1


def everythirdpowerofthree():
    """Generates a sequence every third number to the third power.
    """
    n = 1
    while True:
        if n % 3 == 0:
            yield n ** 3
        n += 1

if __name__ == "__main__":

    g = prime()
    for i in range(10):
        print g.next()
