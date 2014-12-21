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

story_dict = {}   # Initialize a dict which will pair words to their preceding n-gram or 3-character keywords

for i in xrange(len(story_list)):    #Use a for loop to it iterate through the list in its entirety
    
    key_words_3_gram = u" ".join(story_list[i:(i + 2)])    # Set keyword to the first pair of words during first iteration
    key_words_4_gram = u" ".join(story_list[i:(i + 3)])
    key_words_5_gram = u" ".join(story_list[i:(i + 4)])
    key_3_characters = u" ".join(story_list[((i - 3) if (i > 2) else 0):(i + 1)])[-3:]    # Slice the last 3 characters from a string of the
                                                                                          # last 4 words to account for spaces and single
                                                                                          # character words. For the first 3 iterations, floor
                                                                                          # the negative slice index to 0.
    
    if len(key_3_characters) == 3:    # Do not store a keyword if the first word or two happen to be less then 3 total characters inlcuding
                                      # newlines or whitespace
        
        if i < (len(story_list) - 1):
            story_dict.setdefault(key_3_characters, []).append(story_list[i + 1])    # Store the next word for all but the last iteration
        else:
            story_dict.setdefault(key_3_characters, []).append(u"xyz")               # For the value on the last word, use "xyz" as a filler
                                                                                     # keyword which can be easily identified to mark the end of
                                                                                     # the story
    
    if i < (len(story_list) - 4):
        story_dict.setdefault(key_words_3_gram, []).append(story_list[i + 2])    # Add dict values for the n-gram keywords
        story_dict.setdefault(key_words_4_gram, []).append(story_list[i + 3])
        story_dict.setdefault(key_words_5_gram, []).append(story_list[i + 4])
    elif i == (len(story_list) - 4):
        story_dict.setdefault(key_words_3_gram, []).append(story_list[i + 2])
        story_dict.setdefault(key_words_4_gram, []).append(story_list[i + 3])
        story_dict.setdefault(key_words_5_gram, []).append(u"lorem")             # Build up filler keywords at the end of the loop for the
    elif i == (len(story_list) - 3):                                             # n-grams which can be accessed. Use "lorem ipsum", "lorem
        story_dict.setdefault(key_words_3_gram, []).append(story_list[i + 2])    # ipsum dolor" and "lorem ipsum dolor sit" for the
        story_dict.setdefault(key_words_4_gram, []).append(u"lorem")             # corresponding n-grams.
        key_words_5_gram += u" lorem"
        story_dict.setdefault(key_words_5_gram, []).append(u"ipsum")
    elif i == (len(story_list) - 2):
        story_dict.setdefault(key_words_3_gram, []).append(u"lorem")
        key_words_4_gram += u" lorem"
        story_dict.setdefault(key_words_4_gram, []).append(u"ipsum")
        key_words_5_gram += u" lorem ipsum"
        story_dict.setdefault(key_words_5_gram, []).append(u"dolor")
    else:
        key_words_3_gram += u" lorem"
        story_dict.setdefault(key_words_3_gram, []).append(u"ipsum")
        key_words_4_gram += u" lorem ipsum"
        story_dict.setdefault(key_words_4_gram, []).append(u"dolor")
        key_words_5_gram += u" lorem ipsum dolor"
        story_dict.setdefault(key_words_5_gram, []).append(u"sit")


new_story = u"So there I was in the streets of"    # Use any arbitrary string to kick off the story, so long as it has valid keywords
new_story_list = new_story.split(u" ")             # Build the story as a list for computing efficiency

while True:
    key_words = u" ".join(new_story_list[-2:])     # In the while loop, check to see if story ending filler has been appended. If not, append a
    if key_words == u"lorem ipsum":                # new randomly keyed word.
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
    if key_words == u"lorem ipsum dolor":
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
    if key_words == u"lorem ipsum dolor sit":
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story_5_gram.txt", "w", encoding="utf-8")
new_story_file.write(new_story)
new_story_file.close()

new_story = u"So there I was in the streets of"
new_story_list = new_story.split(u" ")

while True:
    key_characters = u" ".join(new_story_list[-4:])[-3:]
    if key_characters == u"xyz":
        break
    new_story_list.append(story_dict[key_characters][int(math.floor(random() * len(story_dict[key_characters])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story_3_characters.txt", "w", encoding="utf-8")
new_story_file.write(new_story)
new_story_file.close()

