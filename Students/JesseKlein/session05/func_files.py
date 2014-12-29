#!/usr/bin/env python
"""
"""
import io
import sys
filename = sys.argv[1]

def clean(s):
    list_s = s.split(u"\n")
    strip_s = map(unicode, map(str.strip, map(str, list_s)))
    cleaned_s = u"\n".join(strip_s)
    return cleaned_s


f = io.open(filename, "r+", encoding="utf-8")
f_string = f.read()
new_f_string = map(clean, [f_string])[0]

c = raw_input(u"Please type 1 to create a new file or 2 to overwrite the existing one: ")

if c == "1":
    new_filename = raw_input(u"Please type a new filename: ")
    new_f = io.open(new_filename, "w", encoding="utf-8")
    new_f.write(new_f_string)
    new_f.close()

if c == "2":
    f.seek(0)
    f.write(new_f_string)
    f.truncate()

f.close()

