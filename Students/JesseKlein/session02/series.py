def fibonacci(n):
    """Return the nth term in the Fibonacci series."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """Return the nth term in the Lucas series."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, optional1 = 0, optional2 = 1):
    """Return the nth term of a series beginning with two optional parameters"""
    if n == 0:
        return optional1
    if n == 1:
        return optional2
    if n > 1:
        return sum_series(n - 2, optional1, optional2) + sum_series(n - 1, optional1, optional2)

if __name__ == "__main__":
    assert(fibonacci, lucas, sum_series)

