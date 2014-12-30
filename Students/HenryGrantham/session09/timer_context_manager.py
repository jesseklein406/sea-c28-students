#!/usr/bin/env python
# -*- coding:  utf-8 -*-

# This module contants two timer context managers, one a class and another
#     a generator function style context managers using a decorator

from __future__ import print_function
import sys
import time
from StringIO import StringIO
from contextlib import contextmanager


class Timer(object):
    """This is a timer context manager Class to time code execution.
    """
    def __init__(self, f=sys.stdout, handle_error=True):
        self.f = f
        self.start_time = time.time()
        self.handle_error = handle_error

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time() - self.start_time
        self.f.write(u"This code took {:f} seconds\n".format(end_time))
        return self.handle_error


@contextmanager
def timer(f=sys.stdout):
    """This is a timer context manager to time code execution.
    """
    start_time = time.time()
    try:
        yield object()
    except Exception as e:
        print(u"An error occured: %s" % e)
        raise e
    finally:
        end_time = time.time() - start_time
        f.write(u"This code took {:f} seconds\n".format(end_time))

if __name__ == "__main__":

    # This is a test to make sure that the context handler Class works
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")


    # This is a test to make sure that the context handler Decorator works
    with timer() as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    # This is a test to make sure that the context handler Class works
    # with a STringIO() passsed in
    f = StringIO()
    with Timer(f) as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    print(f.getvalue())
    f.close()

    # This is a test to make sure that the context handler Decorator works
    # with a STringIO() passsed in
    f2 = StringIO()
    with timer(f2) as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    print(f2.getvalue())
    f2.close()

    print(u"All tests succesful. First two are in different order than")
    print(u"last two because the timer is writing to the default sys.stdout")
    print(u"so timer output comes out on the screen right away.")
    print(u"\nThis last test makes sure exceptions handler works:")
    print(u"(only tests Class version, generator versino already tested)")

    # This test make' sure that the exception in the context handler works
    # With True passed in to ignore exceptions
    f = StringIO()
    with Timer(f, True) as t:
        l = range(500)
        i = 0
        while True:
            i += 1
            l[i] = 1
    print(u"Done Processing")
    print(f.getvalue())
    f.close()

    # This test make' sure that the exception in the context handler works
    # With False passed in to bubble up exceptions
    f = StringIO()
    with Timer(f, False) as t:
        l = range(500)
        i = 0
        while True:
            i += 1
            l[i] = 1
    print(u"Done Processing")
    print(f.getvalue())
    f.close()

    # This test make's sure that the exception in the generatorcontext
    # handler works. Tried this and it does throw an exception
    # with timer() as t:
    #     l = range(500)
    #     i = 0
    #     while True:
    #         i += 1
    #         l[i] = 1
    #     print(u"How long does this time take")



       
