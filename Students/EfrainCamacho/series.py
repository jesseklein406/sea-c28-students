def fibonacci(x):
    """Return the nth number in the fibbonachi sequence"""
    if x == 0 or x < 0:
        return None
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

def lucas(x):
    """Return the nth number in the lucas sequece"""
    if x == 0 or x < 0:
        return 0
    elif x == 1:
        return 2
    elif x == 2:
        return 1
    else:
        return lucas(x - 1) + lucas(x - 2)

def sum_series(x,y = 0,z = 1):
    """Return the nth number in the Lucas or Fibbonacci sequence"""

    """If inputs dont correspond to first numbers of Lucas or fibbonachi
    return number times 5"""
    if y == 0 and z == 1:
        return fibonacci(x)
    elif y == 2 and z == 1:
        return lucas(x)
    else:
        return x * 5

if __name__ == '__main__':
    #lucas number test n = 1,2,5,7
    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(5) == 7
    assert lucas(7) == 18
    #fib number test n = 1,2,5,7
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(5) == 3
    assert fibonacci(7) == 8
    #sum_series number test: see if default is fib for 1,2,5,7
    assert sum_series(1) == fibonacci(1)
    assert sum_series(2) == fibonacci(2)
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7) == fibonacci(7)
    #sum_series number test: see if imput (_,2,1) matches lucas
    assert sum_series(1,2,1) == lucas(1)
    assert sum_series(2,2,1) == lucas(2)
    assert sum_series(5,2,1) == lucas(5)
    assert sum_series(7,2,1) == lucas(7)
    print (u"All Tests Pass")
