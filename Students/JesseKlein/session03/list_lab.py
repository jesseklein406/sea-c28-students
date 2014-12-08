#!/usr/bin/env python

#Series 1

list1 = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

print(u"\nSeries 1")
print(list1)

list1.append(u"%s" % raw_input(u"Please add another fruit to this list: "))

print(list1)

index = raw_input(u"Please enter an index number (1-5): ")

print (u"%s: " % index + list1[int(index) - 1])

list1 = [u"Grapes"] + list1

print(list1)

list1.insert(0, u"Pineapples")

print(list1)

for item in list1:
    if item[0] == "P":
        print(item),

print("\n\n")

#Series 2

list2 = list1[:]

print(u"Series 2")
print(list2)

list2.pop();

print(list2)

list2 *= 2

while True:
    fruit = u"%s" % raw_input(u"Please provide a fruit to delete: ")
    if fruit in list2:
        list2.remove(fruit)
        list2.remove(fruit)
        break

print(list2)

print("\n")

#Series 3

list3 = list1[:]

print(u"Series 3")
print(list3)

new_list3 = []

for item in list3:
    answer = raw_input(u"Do you like %s? " % item.lower())
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

i = 0

for item in list4_copy:
    list4_copy[i] = u""
    for letter in item:
        list4_copy[i] = letter + list4_copy[i]
    i += 1

list4.pop();

print(list4)
print(list4_copy)

