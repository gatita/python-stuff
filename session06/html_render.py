#!/usr/bin/env python

class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if not content:
            self.children = []
        else:
            self.children = [content]

        self.attributes = kwargs

    def append(self, new_content):
        self.children.append(new_content)

    def render(self, file_out, ind=''):
        if self.attributes:
            file_out.write('\n' + ind + u'<%s ' % self.tag)
            for k, v in self.attributes.items():
                file_out.write(u"%s='%s' " % (k,v))
            file_out.write(u'>')
        else:
            file_out.write('\n' + ind + u'<%s>' % self.tag)

        for child in self.children:
            try:
                child.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(' ' + unicode(child))
        if self.tag == 'li' or self.tag == 'p':
            file_out.write(u'</%s> ' % self.tag)
        else:
            file_out.write('\n' + ind + u'</%s> ' % self.tag)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, file_out, ind=''):
        file_out.write('\n' + ind + u'<%s>' % self.tag)
        file_out.write(unicode(self.children))
        file_out.write(u'</%s>' % self.tag)

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def render(self, file_out, ind=''):
        file_out.write('\n' + ind + u'<%s/>' % self.tag)

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    def __init__(self, link, content=None):
        Element.__init__(self, content)
        self.url = link
        self.linkText = content

    def render(self, file_out, ind=''):
        file_out.write('\n' + ind + u'<%s ' % self.tag)
        file_out.write("href='%s'>%s" % (self.url, self.linkText))
        file_out.write(u'<%s/>' % self.tag)

class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None):
        OneLineTag.__init__(self, content)
        self.level = level
        self.title = content

    def render(self, file_out, ind=''):
        file_out.write('\n' + ind + u'<%s%s>' % (self.tag, self.level))
        file_out.write(u'%s' % self.title)
        file_out.write(u'</%s%s>' % (self.tag, self.level))







