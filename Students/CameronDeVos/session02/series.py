from __future__ import print_function

def fibonacci(n):
    """Return the nth value of the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Return the nth value of the Lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, x=0, y=1):
    """Return the nth value in a series based on its first two values.

    Keyword arguments:
    n -- the spot in series
    x -- the 1st number in series, default aligned with fibonacci series
    y -- the 2nd number in series, default aligned with fibonacci series
    """
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)

# Test to verify that the fibonacci, lucas, and sum_series
# return expected results

if __name__ == '__main__':
    fibonacci_series = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5)
    ]

    lucas_series = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11)
    ]

    # Test the fibonacci and sum_series functions with fibonacci series
    for n, result in fibonacci_series:
        assert fibonacci(n) == result
        assert sum_series(n) == result

    # Test the lucas and sum_series functions with lucas series
    for n, result in lucas_series:
        assert lucas(n) == result
        assert sum_series(n, 2, 1) == result

    print (u"All Tests Pass")
