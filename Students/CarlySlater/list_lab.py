#!/usr/bin/env python

fruit = [u'apples', u'pears', u'oranges', u'peaches']
for i in fruit:
    print i

#ask the user for a number and display the number back to the user and the fruit corresponding to that number (ona 1-is basis)


fruit.append(raw_input(u'Please add a fruit:     '))
for i in fruit:
    print i

usernumber = input(u'choose a number from 1 to 5:     ')

print usernumber
print fruit[(usernumber-1)]

print ""
fruit = ([u'kiwi'] + fruit)
for i in fruit:
    print i
print ""
fruit.insert(0, u'pomelo')
for i in fruit:
    print i
print ""
print u'all the fruits that begin with the Letter P:    '
print ""

#display all fruits beginning with P:
for i in fruit: 
    if u'p' == i[0] : 
        print i
print ""
print ""
print ""

#PART 2 of the ASSIGNMENT:

print "And now, Part 2:"
print ""
print ""
# this is to differentiate the parts of the assignment while running it

for i in fruit:
    print i

print ""
print ""


print u'If we remove the last fruit from list, our list looks like this:'

fruit.pop(-1)
#remove the last fruit from the list
print ""

for i in fruit:
    print i

print ""
print ""

badfruit = (raw_input(u'Type the name of a fruit on this list that you\'d like to remove:     ')) 
if badfruit in fruit:
    fruit.remove(badfruit)
print ""
print "VOILA!! the fruit you removed is gone."
print ""
for i in fruit:
    print i

print ""
print ""

#PART 3 of the ASSIGNMENT:

print "And now, Part 3:"
print ""
print ""


for i in fruit[:]: 
    question = "Do you like %s ?    " %i 
    answer = raw_input(question)
    while answer != "yes" and answer != "no":
        answer = raw_input("Please answer 'yes' or 'no' ") 
    if answer == "no":
        fruit.remove(i)
    else:
        continue


print ""
for i in fruit:
    print i

print ""
print ""


