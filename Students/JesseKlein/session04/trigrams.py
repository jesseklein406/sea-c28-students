#!/usr/bin/env python

import io
from random import random
import math

f = io.open("sherlock.txt", encoding="utf-8")
story = f.read()
story_list = story.split(u" ")

story_dict = {}

for i in xrange(len(story_list[:])):
    key_words = u" ".join(story_list[:2])
    if len(story_list) > 2:
        story_dict.setdefault(key_words, []).append(story_list[2])
    elif len(story_list) == 2:
        story_dict.setdefault(key_words, []).append(u"lorem")
    else:
        key_words += u" lorem"
        story_dict.setdefault(key_words, []).append(u"ipsum")
    story_list.pop(0)

new_story = u"So there I was"
new_story_list = new_story.split()

while True:
    key_words = u" ".join(new_story_list[-2:])
    if key_words == u"lorem ipsum":
        break
    new_story_list.append(story_dict[key_words][int(math.floor(random() * len(story_dict[key_words])))])

new_story = u" ".join(new_story_list) + u" -- THE END"

new_story_file = io.open("new_story.txt", "w", encoding="utf-8")
new_story_file.write(new_story)

