#!/usr/bin/env python

class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if not content:
            self.children = []
        else:
            self.children = [content]

    def append(self, new_content):
        self.children.append(new_content)

    def render(self, file_out, ind=''):
        file_out.write(u'<%s>\n' % self.tag)
        for child in self.children:
            file_out.write(ind + unicode(child)+'\n')
        file_out.write(u'</%s>' % self.tag)


# meep = Element()
# meep.append('hey there')

# print meep.children



