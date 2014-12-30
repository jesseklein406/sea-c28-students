def ackermann(m, n):
    """Return the Ackermann function evaluated for given values m and n."""
    if m is 0:
        return n+1
    elif (n is 0) and (m > 0):
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


if __name__ == "__main__":
    m = [[1, 2, 3, 4, 5],
         [2, 3, 4, 5, 6],
         [3, 5, 7, 9, 11],
         [5, 13, 29, 61, 125]]
    for y in range(4):
        for x in range(5):
            assert ackermann(y, x) == m[y][x]
        
    print "All Tests Pass."