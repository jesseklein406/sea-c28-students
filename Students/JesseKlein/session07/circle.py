#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    """Create a new Circle object.
    
    All of the attributes are properties. The area is read-only.
    Attributes:
    radius -- radius of the circle
    diameter -- diameter of the circle
    area -- area of the circle
    """
    def __init__(self, r):
        """Construct a new Circle object.

        Positional arguments:
        r -- radius of new circle
        """
        self._radius = r
        self._diameter = self.radius * 2.0
        self._area = math.pi * self.radius ** 2.0
        
    
    def __add__(self, self_plus_this):
        new_circle_radius = self._radius + self_plus_this._radius
        new_circle = Circle(new_circle_radius)
        return new_circle
    
    
    def __mul__(self, self_times_this):
        new_circle_radius = self._radius * self_times_this
        new_circle = Circle(new_circle_radius)
        return new_circle
        
        
    def __str__(self):
        new_string = "Circle with radius: %.6f" % self._radius
        return new_string
    
    
    def __repr__(self):
        printable = "Circle(%i)" % self.radius
        return printable
    
    
    def __cmp__(self, another):
        return cmp(self._radius, another._radius)
    
    
    def getradius(self):
        return self._radius
    
    
    def setradius(self, new_r):
        Circle.__init__(self, new_r)
        
        
    radius = property(getradius, setradius, doc=u"radius getter/setter")


    def getdiameter(self):
        return self._diameter


    def setdiameter(self, new_d):
        Circle.__init__(self, new_d/2.0)
        
        
    diameter = property(getdiameter, setdiameter, doc=u"diameter getter/setter")


    def getarea(self):
        return self._area


    area = property(getarea, doc=u"area getter")
