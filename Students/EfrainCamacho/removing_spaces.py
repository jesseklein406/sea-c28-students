#!/usr/bin/python
#removing spaces for assignment - Session10


import sys
import io

def clean_file():
    """Ask user to re-rwite exisiting file or create new open


    Removes white spaces from being and end of each line. Adds a newline character
    so that the final text is spaced out."""


    user_input = raw_input(u"Save over file (y or n)")
    while user_input != 'y' and user_input != 'n':
        user_input = raw_input(u"whoops try entering 'y' or 'n'")

    original_file = sys.argv[1]
    text = io.open(original_file, 'r+')
    text_lines = text.readlines()
    text.close()

    # strip lines
    final_lines = map(lambda s: s.strip()+"\n", text_lines)
    ##
    #final_lines = [s.strip()+"\n" for s in lines]

    if user_input == 'y':
        output = io.open(original_file, 'r+')
        output.writelines(final_lines)
        output.close()
    else:
        output = io.open('new_text.txt', 'w+')
        output.writelines(final_lines)
        output.close()

clean_file()
