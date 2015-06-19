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
    About as simple an iterator as you can get:
    returns the sequence of numbers from start to stop
    ( like xrange(start , stop ,step))
    """
    def __init__(self, start, stop, step=1):
        self.start = start
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        if self.current > self.start:
            self = IterateMe_2(self.start, self.stop, self.step)
            return self
        else:
            return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


# if __name__ == "__main__":
#     # print "first version"
#     # for i in IterateMe_1():
#     #     print i


