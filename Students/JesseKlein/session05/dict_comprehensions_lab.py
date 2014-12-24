#!/usr/bin/env python
"""Run this module as a bash script"""


# Problem 1

print(u"\nProblem 1")

food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs))


# Problem 2

print(u"\nProblem 2")

numbers = dict([(x, hex(x)) for x in xrange(16)])

print(numbers)


# Problem 3

print(u"\nProblem 3")

numbers = {x: hex(x) for x in xrange(16)}

print(numbers)


# Problem 4

print(u"\nProblem 4")

new_food_prefs = {item: food_prefs[item].count(u"a") for item in food_prefs}

print(new_food_prefs)


# Problem 5

print(u"\nProblem 5")

s2 = {i for i in xrange(21) if not i % 2}

s3 = {i for i in xrange(21) if not i % 3}

s4 = {i for i in xrange(21) if not i % 4}

print(s2, s3, s4)

list_of_sets = [{i for i in xrange(21) if not i % j} for j in xrange(2, 21)]    # Print sets through modulo 20

print
print(list_of_sets)

