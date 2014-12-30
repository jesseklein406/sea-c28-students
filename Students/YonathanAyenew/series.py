

# Fibonacci Series

def fibonacci(n):
    """ Using looping technique, start with integers 0 and 1."""
    a, b = 0, 1
    for i in range (n-1):
   	    a, b = b, a + b
    return a

# Lucas Numbers

def lucas(n):
	""" Using looping technique, start with integers 2 and 1. """
    a, b = 2, 1
    for i in range (n-1):
        a, b = b, a + b
    return a

# Sum_Series function

def sum_series(n):
    """ Start with any two integers to begin looping technique. """
    a, b = 0, 1
    for i in range (n-1):
        a, b = b, a + b
    return a	


if __name__ == '__main__':
    if a, b = 0, 1:
        assert "This is a Fibonacci Series"

    elif a, b = 2, 1:
        assert "This is a Lucas Series"

    else:
        assert "This is a Sum Series"
  