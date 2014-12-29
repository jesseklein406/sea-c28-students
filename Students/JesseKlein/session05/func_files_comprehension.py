#!/usr/bin/env python
"""Run this module from the console. Add an argument for an input file.
Use this module to remove leading and trailing whitespace from each line
of a file's contents. Save the output to a new file and filename or
overwrite the input file.
"""
import io
import sys
filename = sys.argv[1]

def clean(s):
    """Remove leading and trailing whitespace from a string.

    Enter a string as an argument. Return another string.
    """
    list_s = s.split(u"\n")
    strip_s = [unicode(str(item).strip()) for item in list_s]    # Assign modified list to another list
    cleaned_s = u"\n".join(strip_s)
    return cleaned_s


f = io.open(filename, "r+", encoding="utf-8")
f_string = f.read()
new_f_string = clean(f_string)


c = raw_input(u"Please type 1 to create a new file or 2 to overwrite the existing one: ")

while not c in ["1", "2"]:    # Validate the input
    c = raw_input(u'That is not a "1" or a "2". Pleases type either 1 or 2: ')

if c == "1":
    new_filename = raw_input(u"Please type a new filename: ")
    new_f = io.open(new_filename, "w", encoding="utf-8")
    new_f.write(new_f_string)
    new_f.close()

if c == "2":
    f.seek(0)    # Start the file over
    f.write(new_f_string)
    f.truncate()    # Trim off any old code

f.close()

