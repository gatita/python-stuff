#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, x):
        self._radius = x
        self._diameter = x * 2
        self._area = math.pi * x**2

    def _getradius(self):
        return self._radius

    def _setradius(self, value):
        self._radius = value
        self._diameter = value * 2
        self._area = math.pi * value**2

    radius = property(_getradius, _setradius)