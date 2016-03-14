#!/usr/bin/env python

"""This python module is meant to be run as a script which generates
four text files. 'new_story.txt' is a new Shelock Holmes-like story
built using the method laid out in CodeKata #14 using trigrams.
'new_story_4_gram.txt' uses a similar method but with 4-grams instead,
'new_story_5_gram.txt' uses 5-grams. 'new_story_3_characters.txt' uses
a 3 character dict key to generate a new word. This modules loads
'sherlock.txt' from the current directory, but it can be set to take
any text."""

import io
from random import random
import math

f = io.open("sherlock.txt", encoding="utf-8")    # Open './sherlock.txt' by default or change to a different text file path
story = f.read()
story_list = story.split(u" ")    # Split up the story into a list of words and/or newlines and empty strings for simpler processing

last_words_3gram = u" ".join(story_list[-2:])
last_words_4gram = u" ".join(story_list[-3:])
last_words_5gram = u" ".join(story_list[-4:])

story_dict = {}   # Initialize a dict which will pair words to their preceding n-gram or 3-character keywords

for i in xrange(len(story_list)):    #Use a for loop to it iterate through the list in its entirety
    
    key_words_3_gram = u" ".join(story_list[i:(i + 2)])    # Set keyword to the first pair of words during first iteration
    key_words_4_gram = u" ".join(story_list[i:(i + 3)])
    key_words_5_gram = u" ".join(story_list[i:(i + 4)])

new_story = u"So there I was in the streets of"    # Use any arbitrary string to kick off the story, so long as it has valid keywords
new_story_list = new_story.split(u" ")             # Build the story as a list for computing efficiency

while True:
    key_words = u" ".join(new_story_list[-2:])     # In the while loop, check to see if story ending filler has been appended. If not, append a
    if key_words == last_words_3gram:                # new randomly keyed word.
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"    # Add this after the filler, which is useful to show that the script completed as
                                                          # expected. If desired, add some code to crop out the filler.

new_story_file = io.open("new_story.txt", "w", encoding="utf-8")
new_story_file.write(new_story)
new_story_file.close()

new_story = u"So there I was in the streets of"
new_story_list = new_story.split(u" ")

while True:
    key_words = u" ".join(new_story_list[-3:])    # Run the same code for the other n-grams
    if key_words == last_words_4gram:
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story_4_gram.txt", "w", encoding="utf-8")
new_story_file.write(new_story)
new_story_file.close()

new_story = u"So there I was in the streets of"
new_story_list = new_story.split(u" ")

while True:
    key_words = u" ".join(new_story_list[-4:])
    if key_words == last_words_5gram:
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story_5_gram.txt", "w", encoding="utf-8")
new_story_file.write(new_story)
new_story_file.close()
