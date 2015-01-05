#!/usr/bin/env python
"""Context manager Timer to print computing time"""

import time

class Timer(object):
    """Context manager Timer to print computing time"""
    def __init__(self):
        """Construct a Timer object, no arguments passed"""
        self.tic = 0
        self.toc = 0
    def __enter__(self):
        self.tic = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.toc = time.time()
        my_time = self.toc - self.tic
        print(u"this code took %.6f seconds" % my_time)
        return True

