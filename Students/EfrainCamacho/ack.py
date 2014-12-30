def ack(m,n):
    """Return the value of the Acherman Function for inputs less than 5"""
    if n < 0 or m < 0:
        return 'try again'
    elif m > 5:
        return "value too large"
    elif m == 0:
        return n+1 
    elif m > 0 and n ==0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m, n-1))

def real_values(x,y):
    """Return check values of Ackerman function"""
    if x == 0:
        return y + 1       
    elif x == 1:
        return y + 2
    elif x == 2:
        return 2 * y + 3
    elif x == 3:
        return 2 ** (y + 3) - 3
    else:
        print ("Out of Range")
        return None

if __name__ == '__main__':
    #test function for values m: 0-3 and n: 0-4
    for x in range (4):
        for y in range(5):
            assert ack(x, y) == real_values(x, y)
    print (u"All Test Pass")