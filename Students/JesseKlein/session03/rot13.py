#!/usr/bin/env python

def rot13(string):
    string = unicode(string)
    
    for i in string:
        if ord(i) >= ord(u"A") and ord(i) <= ord(u"z"):
            if ord(i) >= ord(u"A") and ord(i) <= ord(u"M") or ord(i) >= ord(u"a") and ord(i) <= ord(u"m"):
                string[i] = unichr(ord(i) + 13)
            if ord(i) >= ord(u"N") and ord(i) <= ord(u"Z") or ord(i) >= ord(u"n") and ord(i) <= ord(u"z"):
                string[i] = unichr(ord(i) - 13)
    
    string = str(string)

    return string

if __name__ == "__main__":
    for i in "_ ',.?/:;<>[]{}|`~!@#$%^&*()-=+":
        
        assert rot13(i) == i

    lower_half = "abcdefghijklmABCDEFGHIJKLM"
    upper_half = "nopqrstuvwxyzNOPQRSTUVWXYZ"

    for i, j in zip(lower_half, upper_half):
        
        assert rot13(i) == j
        assert rot13(j) == i

    print(u"All Tests Pass")
