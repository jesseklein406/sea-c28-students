def fibonacci(n):
    """Return the nth value of the Fibonacci series."""
    
    return sum_series(n)

    
def lucas(n):
    """Return the nth value of the Lucas number series."""
    
    return sum_series(n, 2, 1)


def sum_series(n, a=0, b=1):
    """Return the nth value of a series of sums.
    Generate a series n terms long by adding the most recent two terms.
    Dictate the number of terms with parameter n, 
    and first and second terms with 'a' and 'b' respectively.
    'a' and 'b' are 0 and 1 by default."""
    
    series = [a, b]
    if n < 1:
        return None
    if n <= 2:
        return series[n-1]
    else:
        for x in range(n-2):
            series[0], series[1] = series[1], series[0]
            series[1] = series[0] + series[1]
        return series[1]

        
if __name__ == "__main__":
    #the nth number of the fibonacci series should be generated
    #by a call on sum_series(n)
    #compare the first 10 numbers of the fibonacci series to the
    #output of the function for n = 1 to 10
    #if the function sum_series passes these tests, then the functions
    #fibonacci and lucas will similarly perform as expected
    fibonacci_check = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(len(fibonacci_check)):
        assert fibonacci_check[i] == sum_series(i+1)
    
    #the nth number of the lucas numbers should be generated
    #by a call on sum_series(n, 2, 1)
    #compare the first 10 numbers of the lucas numbers to the output
    #of the function for n = 1 to 10
    lucas_check = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    for i in range(len(lucas_check)):
        assert lucas_check[i] == sum_series(i+1, 2, 1)
    
    #check if the function returns None for negative values of n
    assert sum_series(-1) == None