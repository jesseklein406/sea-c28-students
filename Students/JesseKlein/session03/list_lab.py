#!/usr/bin/env python
"""This script demonstrates the various functions associated with lists"""

#Series 1

list1 = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

print(u"\nSeries 1")
print(list1)

list1.append(u"%s" % raw_input(u"Please add another fruit to this list: "))

print(list1)

#Convert string to integer in the statement because
#index should be an integer

index = int(raw_input(u"Please enter an index number (1-5): "))

print (u"%s: " % index + list1[index - 1])

list1 = [u"Grapes"] + list1

#Print to show the user what was added by the script

print(list1)

list1.insert(0, u"Pineapples")

print(list1)

for item in list1:
    if item[0] == "P":
        print(item),

#Get some extra spacing since the newline was omitted
print("\n\n")


#Series 2
#
#Make list2 a copy of list1 using the "[:]" trick.
#list1 is the final list created in Series 1.

list2 = list1[:]

print(u"Series 2")
print(list2)

list2.pop();

print(list2)

list2 *= 2

#Run the while loop indefinitely until a match is found
while True:
    fruit = u"%s" % raw_input(u"Please provide a fruit to delete: ")
    if fruit in list2:

        #Remove it twice with the same method
        list2.remove(fruit)
        list2.remove(fruit)
        break

print(list2)

print("\n")

#Series 3

list3 = list1[:]

print(u"Series 3")
print(list3)

#Provide empty list from which to build
new_list3 = []

for item in list3:
    answer = raw_input(u"Do you like %s? " % item.lower())
    
    #Check to make sure the answer is valid
    while answer != "yes" and answer != "no":
        answer = raw_input(u"Please answer yes or no: ")
    if answer == "yes":
        new_list3.append(item)

print(new_list3)

print("\n")

#Series 4

list4 = list1[:]

print(u"Series 4")
print(list4)

list4_copy = list4[:]

#Make the index correspond to the word in the loop,
#and build the word backwards.
i = 0

for item in list4_copy:
    list4_copy[i] = u""
    for letter in item:
        list4_copy[i] = letter + list4_copy[i]
    i += 1

list4.pop();

print(list4)
print(list4_copy)

