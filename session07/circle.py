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