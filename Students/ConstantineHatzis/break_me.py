# Assignment 1, Task 4

from __future__ import print_function


#  Cause NameError exception
def breakName():
    print(a)


#  Cause TypeError exception
def breakType():
    b = "myString"
    c = b ** 2


#  Cause AttributeError exception
def breakAttribute():
    e = 100
    f = e.length


#  Cause SyntaxError exception
def breakSyntax():
    eval("abs(pass)")


breakName()
breakType()
breakAttribute()
breakSyntax()
