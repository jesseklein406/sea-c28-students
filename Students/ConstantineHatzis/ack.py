from __future__ import print_function


def ack(m, n):
    """Return the ouput of the Ackermann function for two numbers greater than
        zero."""
    if m < 0 or n < 0:
        result = None
    else:
        if m == 0:
            result = n + 1
        elif m > 0 and n == 0:
            result = ack(m-1, 1)
        elif m > 0 and n > 0:
            result = ack(m-1, ack(m, n-1))
    return result

# If ack is run with m > 3, the recurssion limit will be reached, unless it is
#  m = 3, n = 0

if __name__ == "__main__":
    # Test values from the Wikipedia page for the Ackermann function
    test_values = ([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 5, 7, 9, 11],
                    [5, 13, 29, 61, 125]])

    for m in range(4):
        for n in range(5):
            assert ack(m, n) == test_values[m][n]

    # If an assert fails, and exception will be thrown and this following print
    # will not executre.
    print(u"All Tests Pass")
