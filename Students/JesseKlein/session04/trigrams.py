#!/usr/bin/env python

import io
from random import random
import math

f = io.open("sherlock.txt", encoding="utf-8")
story = f.read()
story_list = story.split(u" ")

story_dict = {}

for i in xrange(len(story_list)):
    key_words_3_gram = u" ".join(story_list[i:(i + 2)])
    key_words_4_gram = u" ".join(story_list[i:(i + 3)])
    if i < (len(story_list) - 3):
        story_dict.setdefault(key_words_3_gram, []).append(story_list[i + 2])
        story_dict.setdefault(key_words_4_gram, []).append(story_list[i + 3])
    elif i == (len(story_list) - 3):
        story_dict.setdefault(key_words_3_gram, []).append(story_list[i + 2])
        story_dict.setdefault(key_words_4_gram, []).append(u"lorem")
    elif i == (len(story_list) - 2):
        story_dict.setdefault(key_words_3_gram, []).append(u"lorem")
        key_words_4_gram += u" lorem"
        story_dict.setdefault(key_words_4_gram, []).append(u"ipsum")
    else:
        key_words_3_gram += u" lorem"
        story_dict.setdefault(key_words_3_gram, []).append(u"ipsum")
        key_words_4_gram += u" lorem ipsum"
        story_dict.setdefault(key_words_4_gram, []).append(u"dolor")


new_story = u"So there I was doing Sherlock Holmes things when all of a sudden"
new_story_list = new_story.split()

while True:
    key_words = u" ".join(new_story_list[-2:])
    if key_words == u"lorem ipsum":
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story.txt", "w", encoding="utf-8")
new_story_file.write(new_story)

new_story = u"So there I was doing Sherlock Holmes things when all of a sudden"
new_story_list = new_story.split()

while True:
    key_words = u" ".join(new_story_list[-3:])
    if key_words == u"lorem ipsum dolor":
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story_4_gram.txt", "w", encoding="utf-8")
new_story_file.write(new_story)

