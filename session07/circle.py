#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, x):
        self._radius = x
        self._diameter = x * 2

    def _getradius(self):
        return self._radius

    def _setradius(self, value):
        self._radius = value
        self._diameter = value * 2

    radius = property(_getradius, _setradius)

    def _getdiameter(self):
        return self._diameter

    def _setdiameter(self, value):
        self._diameter = value
        self._radius = value / 2

    diameter = property(_getdiameter, _setdiameter)

    def _getarea(self):
        return math.pi * self._radius**2

    area = property(_getarea)

    ##extra credit
    @classmethod
    def from_diameter(cls, y):
        c = cls(x=y/2)
        c.diameter = y
        c.radius = y / 2
        return c

    def __str__(self):
        return 'Circle with radius: %.6f' % self.radius

    def __repr__(self):
        return 'Circle(%i)' % self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    # def __le__(self, other):
    #     return self.radius <= other.radius

    def __lt__(self, other):
        return self.radius < other.radius



