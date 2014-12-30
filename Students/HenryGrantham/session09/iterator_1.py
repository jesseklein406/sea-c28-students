#!/usr/bin/env python

"""
Simple iterator examples
"""
from __future__ import print_function

class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=20):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    This iterator acts like xrange(start, stop, step)

    It resets to the beginning at the start of any for loop.
    """
    def __init__(self, start=1, stop=20, step=1):
        self.start = start
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    # IterateMe_2 is reseting with the new loop.
    print("second version")
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print(i, end=' ')
    print('\n')
    for i in it:
        print(i, end=' ')
    print('\n')
    print("xrange")
    it2 = xrange(2, 20, 2)
    for i in it2:
        if i > 10:
            break
        print(i, end=' ')
    print('\n')
    for i in it2:
        print(i, end=' ')
    print('\n')

    # assert statement to make sure that IterateMe2 and xrange work the same.
    a = range(1, 5)
    b = range(1, 5)
    for x, y in [(x, y) for x in a for y in b]:
        iterateme = [i for i in IterateMe_2(x, 20, y)]
        itxrange = [i for i in xrange(x, 20, y)]
        print("{}=\n{}".format(iterateme, itxrange))
        assert iterateme == itxrange
    print("Tests come out fine.")
