#!/usr/bin/env python
"""This module is intended to be run as a script in a Python interpreter"""

#Task 1

print(u"Task 1")

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

print(u"Task 2")

dict2 = dict(zip(range(16), (hex(i) for i in range(16))))

print(u"Dictionary: " + unicode(dict2))

