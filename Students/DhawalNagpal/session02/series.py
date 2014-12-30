def fibonacci(n):
    """ returns fibonacci series """
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)


def lucas(n):
    """ returns lucas series """
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas (n - 1) + lucas (n - 2)

def sum_series (x,y = 0, z = 1):
    """ return either fibonacci or lucas """
    if y == 0 and z == 1:
        return fibonacci (x)
    elif y == 2 and z == 1:
        return lucas (x)
    elif x < 0:
        return None
    elif x == 1:
        return y
    elif x == 2:
        return z
    else:
        return sum_series(x-1, y, z) + sum_series(x-2, y, z)    

if __name__ == "__main__":

    # check fibonacci series

    assert fibonacci (1) == 0
    assert fibonacci (2) == 1
    assert fibonacci (3) == 1
    assert fibonacci (4) == 2
    assert fibonacci (5) == 3

    # check lucas series

    assert lucas (1) == 2
    assert lucas (2) == 1
    assert lucas (3) == 3
    assert lucas (4) == 4
    assert lucas (5) == 7
    
    # check sum_series 
    assert sum_series (5) == fibonacci(5)
    assert sum_series (4,2,1) == lucas (4)
    assert sum_series (3, 1, 2 ) == 3


