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
        file_out.write('\n' + ind + u'<%s>' % self.tag)
        for child in self.children:
            try:
                child.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(ind + unicode(child)+'\n')
        file_out.write('\n' + ind + u'</%s>' % self.tag)


class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'


