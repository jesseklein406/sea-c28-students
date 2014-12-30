def ack(m,n):
    """Return the value of the Ackermann function"""
    if m>=0 and n>=0:
        if not m:
            return n+1
        elif m > 0 and not n:
            return ack(m-1, 1)
        else:
            return ack(m-1, ack(m, n-1))
    else:
        return None



if __name__ == "__main__":
    #Compare the output of ack to a table of expected values (from Wikipedia)

    ackermann_dict = {(0,0):1,(0,1):2,(0,2):3,(0,3):4,(0,4):5,(1,0):2,(1,1):3,
                      (1,2):4,(1,3):5,(1,4):6,(2,0):3,(2,1):5,(2,2):7,(2,3):9,
                      (2,4):11,(3,0):5,(3,1):13,(3,2):29,(3,3):61,(3,4):125}

    for m in range(4):
        for n in range(5):
            assert (ack(m,n)) == ackermann_dict[m,n]

    print(u"all tests passed")
