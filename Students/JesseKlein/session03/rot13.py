#!/usr/bin/env python

def rot13(string):
    
    string = unicode(string)
    string2 = u""
    
    for i in string:
        if ord(i) >= ord(u"A") and ord(i) <= ord(u"z"):
            if ord(i) >= ord(u"A") and ord(i) <= ord(u"M") or ord(i) >= ord(u"a") and ord(i) <= ord(u"m"):
                i = unichr(ord(i) + 13)
            else:
                i = unichr(ord(i) - 13)
        string2 += i
    
    string2 = str(string2)

    return string2

if __name__ == "__main__":
    punctuation =  "_ ',.?/:;<>[]{}|`~!@#$%^&*()-=+"
    print(punctuation)
    print(rot13(punctuation))
    assert rot13(punctuation) == punctuation
    
    lower_half = "abcdefghijklmABCDEFGHIJKLM"
    upper_half = "nopqrstuvwxyzNOPQRSTUVWXYZ"
    
    assert rot13(lower_half) == upper_half
    assert rot13(upper_half) == lower_half
    
    print(u"All Tests Pass")

