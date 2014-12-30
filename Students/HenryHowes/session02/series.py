def fibonacci(n):
    """Return the nth value in the fibonacci series, where each value is the sum of the previous two values, beginning with 0 and 1."""

    if n < 1:
        raise ValueError('n must be greater than 0')

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)


def lucas(n):
    """Return the nth value in the lucas series, where each value is the sum of the previous two values, beginning with 2 and 1."""

    if n < 1:
        raise ValueError('n must be greater than 0')

    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas (n-2)

def sum_series(n, first=0, second=1):
    """Return the nth value in the sum series where each value is the sum of the previous two values.
       
       Keyword arguments:
       first -- specifies the first value in the series (defaults to 0)
       second -- specifies the second value in the series (defaults to 1)
       """

    if n < 1:
        raise ValueError('n must be greater than 0')
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series (n-2, first, second)

if __name__ == "__main__":

    #test whether the first eight values returned by fibonacci() 
    fibonacci_first_eight = [0,1,1,2,3,5,8,13]  

    for number in range(1,9):
        assert fibonacci(number) == fibonacci_first_eight[number-1]

    #test whether the first eight values returned by lucas are the same as the lucas series
    lucas_first_eight = [2,1,3,4,7,11,18,29]

    for number in range(1,9):
        assert lucas(number) == lucas_first_eight[number-1]

    #test sum_series with different parameters
    for number in range(1,9):
        ##test whether calling sum_series() without parameters returns the same value as fibonacci(), given n
        assert sum_series(number) == fibonacci(number)

        ##test whether calling sum_series() with the parameters 2,1 returns the same value as lucas(), given n
        assert sum_series(number, 2, 1) == lucas(number)


    ##test whether calling sum_series() with different parameters returns the expected result
    assert sum_series(3,first=5,second=4) == 9
    assert sum_series(4,first=3,second=3) == 9
    assert sum_series(5,first=6,second=7) == 33


    print(u"all tests passed")







