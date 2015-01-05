#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
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
    An iterator that emulates xrange
    
    Attributes:
    start -- start the iteration at this number
    stop -- iterate until this number is reached
    step -- increment by this number
    current -- current location in iterable
    Methods:
    next -- increment by one step and gives output
    """
    def __init__(self, *args):
        """Construct an IterateMe_2 iterator object
        
        Positional arguments:
        start -- start the iteration at this number, equals 0 if not given before stop argument
        stop -- iterate unitl this number is reached, equals 5 if nothing given
        step -- increment by this number, equals 1 if not given after values for other two arguments
        """
        self.stop = (args[1:2] or args or (5,))[0]    # Default to 5
        self.start = (args[:-2] or args[:-1] or (0,))[0]    # Default to 0
        self.step = (args[2:3] or (1,))[0]    # Default to 1
        self.current = self.start - self.step
    
    def __iter__(self):
        self.current = self.start - self.step    # Reset for each call to iterate like xrange
        return self
    
    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print "first version"
    for i in IterateMe_1():
        print i
