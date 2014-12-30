#first test case - producing TypeError
def test1(a):
    n = range[a+1]
    n.reverse
    return n[a]

#second test case - producing AttributeError
def test2(a):
    n = range(n+1)
    n.reversed
    return n[a]

#thrid test case - producing SyntaxError
def test3(a):
    n = range(n+1]
    n.reverse
    return n[a]

#forth test case - producing NameError
def test4(a):
    n = range(n+1)
    n.reverse
    return m[a]
