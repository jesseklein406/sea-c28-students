def ack(m,n):
    """ returns the ackermann function """
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

def real_stuff(x,y):
    if x < 0 and y < 0:
        return None
    elif x == 0:
        return y + 1
    elif x == 1:
        return y + 2
    elif x == 2:
        return (2 * y) + 3
    elif x == 3:
        return 2 ** (y + 3) - 3

if __name__ == '__main__':
    for a in range (4):
        for b in range (5):
            assert ack(a, b) == real_stuff(a, b)
print (u"All Tests Pass")
