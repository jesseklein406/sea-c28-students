from __future__ import print_function

def ack(m, n):
    """Return a result of the Ackermann function based on two inputs.
    
    Keyword arguments:
    m -- nonnegative integer
    n -- nonnegative integer
    """
    # Check for negative inputs
    if m < 0 or n < 0:
        return None
    # Ackermann series
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

# Test to verify that results for input pairs
# return a value that matches expected Ackermann result.
# Task note: When a value of m is >3 a max recur depth is exceeded.

if __name__ == '__main__':
    ack_series = [
    (0, 0, 1),
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 5),
    (1, 0, 2),
    (1, 1, 3),
    (1, 2, 4),
    (1, 3, 5),
    (1, 4, 6),
    (2, 0, 3),
    (2, 1, 5),
    (2, 2, 7),
    (2, 3, 9),
    (2, 4, 11),
    (3, 0, 5),
    (3, 1, 13),
    (3, 2, 29),
    (3, 3, 61),
    (3, 4, 125)
    ]

    for m, n, result in ack_series:
        assert ack(m, n) == result

    print (u"All Tests Pass")