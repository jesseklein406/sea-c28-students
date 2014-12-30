#! /usr/bin/env python

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print fruits


def get_answer1():
    """Return user input for fruit and checks to see 

    
    if all characters are alphabets"""
    keepgoing = True
    while keepgoing:
        checka1 = raw_input("name a fruit  ")
        if checka1.isalpha():
            keepgoing = False
            return checka1
        else:
            print "Thats not a fruit!"
            pass

    return checka1


answer1 = get_answer1()


fruits.append(answer1)
print fruits


def get_answer2():
    """Return user input for fruit number and check 


    if number is between 1 and 5"""
    keepgoing = True
    while keepgoing:
        answer2 = int(raw_input("please provide a number between 1-5  "))
        if answer2 > 0 and answer2 < 6:
            keepgoing = False
            return answer2
        else:
            print "Try again"
        return answer2 

answer2 = get_answer2()

print fruits[answer2 -1], answer2

fruits = ["Banana",] + fruits
print fruits

fruits.insert(0,"Watermellon")
print fruits

def search_p(fruits):
    """Return fruits with starting letter uppercase P"""

    for fruit in fruits:
        if fruit[0] == "P":
            print fruit
        else:
            pass

search_p(fruits)

"""double_fruits = fruits * 2
print double_fruits - ran out of time for bonus"""

print fruits

fruits2 = fruits[:-1]
#copy list for excersise 2

print fruits2
fruit_to_delete = raw_input("name a fruit from the list to delete  ")
fruits2.remove(fruit_to_delete)
print fruits2

def do_you_like(fruits):
    """Return list of fruits you like - remoes those you do not"""

    for fruit in fruits:
        keepgoing = True
        while keepgoing:
            uinput = raw_input("do you like {}? (yes/no)".format(fruit.lower()))
            if uinput == "yes":
               keepgoing = False
            elif uinput == "no":
                fruits.remove(fruit)
                keepgoing = False
            else:
                pass


do_you_like(fruits2)

print fruits2

def switching_it_up(fruits):
    """Return list with all valuse reversed"""

    
    fruits3 = fruits[:]
    for idx, fruit in enumerate(fruits3):
        fruits3[idx] = fruits3[idx][::-1]
    print fruits3
    print fruits


switching_it_up(fruits)






