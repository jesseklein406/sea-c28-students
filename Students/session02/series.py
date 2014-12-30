 
def fibonacci(n):
    """ returns n-th Fibonacci no """
   
    # HELLO Cris and TA team - i struggled with ths for few days and finally
    # resorted to the old fashioned paper and pencil way VS using the
    # fancy: fibonacci(n-2) + fibonacci(n-1) <-- i do not groak that (yet!)
    
    #print 'type fibonacci is', type(fibonacci)
    seed1=0
    seed2=1
    #print seed1,seed2, 'seeds'
    if n==0:
        return seed1
    elif n==1:
        return seed2
    #print n,'n inside fn'
    for n in range (2,n+1):
        #print n, 'n inside for loop'
        latest = seed1+seed2
        #print 'latest', latest
        seed1=seed2
        #print 'new seed1', seed1
        seed2=latest
        #print 'new seed2', seed2
        n=n+1
        #print 'new n', n
    return latest
   
#n=int(raw_input('enter the pos in Fib series you want nth:..-->'))
#print 'and the', n, 'th fib # is', fibonacci(n)
 
 
def lucas(n):
    """ returns n-th Lucas no """
   
    seed1=2
    seed2=1
    #print seed1,seed2, 'seeds'
    if n==0:
        return seed1
    elif n==1:
        return seed2
    #print n,'n inside fn'
    for n in range (2,n+1):
        #print n, 'n inside for loop'
        latest = seed1+seed2
        #print 'latest', latest
        seed1=seed2
        #print 'new seed1', seed1
        seed2=latest
        #print 'new seed2', seed2
        n=n+1
       #print 'new n', n
    return latest
   
#n=int(raw_input('enter the pos in Lucas series you want nth:..-->'))
#print 'and the', n, 'th Lucas # is', lucas(n)
 
 
def sum_series (n,seed1,seed2):
    """ returns n-th value of Fibonacci or Lucas depending on the seeds provided """
   
    #seed1=2
    #seed2=1
    #print seed1,seed2, 'seeds'
    if n==0:
        return seed1
    elif n==1:
        return seed2
    #print n,'n inside fn'
    for n in range (2,n+1):
        #print n, 'n inside for loop'
        latest = seed1+seed2
        #print 'latest', latest
        seed1=seed2
        #print 'new seed1', seed1
        seed2=latest
        #print 'new seed2', seed2
        n=n+1
        #print 'new n', n
    return latest
   
n=int(raw_input('enter the pos in series you want nth:..-->'))
seed1=int(raw_input('enter seed1.-->'))
seed2=int(raw_input('enter seed1.-->'))
 
print 'and the', n, 'th # n series with seeds', seed1, seed2, 'is', sum_series(n, seed1,seed2)