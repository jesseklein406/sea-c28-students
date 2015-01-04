#!/usr/bin/env python
"""This module encrypts text by mapping the front half of the alphabet
with the back half. Each letter is mapped to the letter 13 letters away
using the rot13 function with text as input. The rot13 function is
its own inverse"""

def rot13(string):
    
    #This boolean switch remembers the type of the string passed for later
    bool = False
    
    if type(string) == str:
        string = unicode(string)
        
        #Turn on the switch
        bool = True
    
    string2 = u""
    
    for i in string:
        
        #This conditional contains both sets of the front half of the alphabet
        if ord(i) >= ord(u"A") and ord(i) <= ord(u"M") or ord(i) >= ord(u"a") and ord(i) <= ord(u"m"):
            i = unichr(ord(i) + 13)
        
        #This conditional contains both sets of the back half of the alphabet
        elif ord(i) >= ord(u"N") and ord(i) <= ord(u"Z") or ord(i) >= ord(u"n") and ord(i) <= ord(u"z"):
            i = unichr(ord(i) - 13)
        
        string2 += i
    
    #Only convert if the switch says so
    if bool:
        string2 = str(string2)

    return string2

if __name__ == "__main__":
    
    #This is all the punctuation on a normal keyboard.
    #It is unaffected by "rot13()".
    punctuation =  "_ ',.?/:;<>[]{}|`~!@#$%^&*()-=+"
           
    assert rot13(punctuation) == punctuation
    
    #These two sets of letters map onto each other"
    
    lower_half = "abcdefghijklmABCDEFGHIJKLM"
    upper_half = "nopqrstuvwxyzNOPQRSTUVWXYZ"
        
    assert rot13(lower_half) == upper_half
    assert rot13(upper_half) == lower_half
    
    print(u"All Tests Pass")

