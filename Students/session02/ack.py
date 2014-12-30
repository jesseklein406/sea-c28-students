def gettwogoodnums():
    """ Obtain and ensure m&n are not negative and Int b4 passing
    Also check for: blank/no input, neg, non-int...
    """
 
    m=int(raw_input('input m-->'))
    n=int(raw_input('input n-->'))
 
    assert (m>=0), 'm must be non neg'
    assert type(m) == int, "m is not an integer: %r" % m
 
    assert (n>=0), 'n must be non neg'
    assert type(n) == int, "m is not an integer: %r" % n
    #print m,n, 'm,n'
   
    #try:
    #    m >=0
    #except EOFError:
    #    print 'i think that was an accidental CR ..need a non-neg Int, pl..>'
 
    return (m,n) 
 
 
 
def acker(m, n):
    """calculate Ackermann function acker(m, n)
 
    Note: m & n: must be type(Int) AND non-negative
    """
    if m == 0:
        return n+1 # if m==0 then fn returs and rest won't be run.
    if n == 0: # if we got here, m is clearly NOT zero
        return acker(m-1, 1)
    return acker(m-1, acker(m, n-1))
 
m,n = gettwogoodnums()
 
#print m, n, 'is m and n'
 
print 'acker of m &n', m,n, 'is..->', acker(m, n)
 

if __name__ == "__main__":
    ackfor_m0=[1,2,3,4,5]
    ackfor_m1=[2,3,4,5,6]
    ackfor_m2=[3,5,7,9,11]
    ackfor_m3=[5,13,29,61,125]
    for m in range (0,4):
    
        if m==0: ackcheck=ackfor_m0
        if m==1: ackcheck=ackfor_m1
        if m==2: ackcheck=ackfor_m2
        if m==3: ackcheck=ackfor_m3
   
        for n in range(0, 5):
            #print m,n
            #print acker(m,n)
            #print ackfor_m0[n]
            if acker(m,n) == ackcheck[n]:
                print('pass for n='),n, 'while m is-->', m
                #m=m+1
 
#ackerwikipedia = [[1,2,3,4,5],[2,3,4,5,6],[3,5,7,9,11],[5,13,29,61,125]]
#print ackerwikipedia [1,1]#, 'ackerwikipedia 1,1'