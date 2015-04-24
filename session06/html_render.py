#!/usr/bin/env python

from io import open, StringIO

class Element(object):
    tag = 'html'
    indent = '  '
    def __init__(self, content=None):
        if not content:
            self.parent = []
        else:
            self.parent = [content]


    def append(self, new_string):
        self.parent.append(new_string)

    def render(self, file_out, ind =''):
        file_out.write(u'<%s>\n' % self.tag)
        for child in self.parent:
            file_out.write(ind + child + '\n')
        file_out.write(u'</%s>' % self.tag)


















