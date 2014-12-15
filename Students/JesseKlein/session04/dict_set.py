#!/usr/bin/env python
"""This module is intended to be run as a script in a Python interpreter"""

#Task 1

print(u"\nTask 1")

dict1 = dict([(u"name", u"Chris"), (u"city", u"Seattle"), (u"cake", u"Chocolate")])

print(u"Dictionary: " + unicode(dict1))

dict1.pop(u"cake")

print(u"Dictionary: " + unicode(dict1))

dict1[u"fruit"] = u"Mango"

print(u"Dictionary keys: " + unicode(dict1.keys()))
print(u"Dictionary values: " + unicode(dict1.values()))
print(u'Key "cake" in dictionary: ' + unicode(u"cake" in dict1.keys()))
print(u'Value "Mango" in dictionary: ' + unicode(u"Mango" in dict1.values()))

#Task 2

print(u"\nTask 2")

dict2 = dict(zip(range(16), (unicode(hex(i)) for i in range(16))))

print(u"Dictionary: " + unicode(dict2))

#Task 3

print(u"\nTask 3")

#Use a string to present some meaning for the value
dict3 = dict(zip(dict1.keys(), ((u'Number of "a"s = ' + unicode(i.count(u"a"))) for i in dict1.keys())))

print(u"Dictionary: " + unicode(dict3))

#Task 4

print(u"\nTask 4")

#Include 'if not' statement in for loop
s2 = set(i for i in range(21) if not i % 2)
s3 = set(i for i in range(21) if not i % 3)
s4 = set(i for i in range(21) if not i % 4)

print(u"s2: " + unicode(s2))
print(u"s3: " + unicode(s3))
print(u"s4: " + unicode(s4))

print(u"s3 is a subset of s2: " + unicode(s3.issubset(s2)))
print(u"s4 is a subset of s2: " + unicode(s4.issubset(s2)))

#Task 5

print(u"\nTask 5")

set5 = set(list(u"Python"))
set5.update(u"i")

print(u"Set: " + unicode(set5))

frozenset5 = frozenset(list(u"marathon"))
print(u"Frozenset: " + unicode(frozenset5))

print(u"Union of set and frozenset: " + unicode(set5.union(frozenset5)))

print(u"Intersection of set and frozenset: " + unicode(set5.intersection(frozenset5)))

