#!/usr/bin/env python
"""Python example of a class"""


class Element(object):
    tag = u"html"
    indent = "    "

    def __init__(self, content = None, **kwargs):
        if content == None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = ''.join(' {} = "{}"'.format(k, v) 
            for k, v in kwargs.items())

    def append(self, content):
        self.contents.append(content)

    def render(self, file_out, ind = ""):
        file_out.write("{}<{}{}>\n \n".format(ind, self.tag, self.attributes))

        for text in self.contents:
            try:
                text.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write('{}{}\n'.format(ind + self.indent, text))


        file_out.write("{}</{}>\n".format(ind, self.tag))


class Html(Element):
    tag = u'html'

    def render(self, file_out, indent = ""):
        """Places string containg !DOCTYPE at the start of the text
        
        Html has to be called at the start"""
        file_out.write('<!DOCTYPE html>\n')

        Element.render(self, file_out, indent)


class Body(Element):
    tag = u'body'

class P(Element):
    tag =u'p'

class Head(Element):
    tag = u'head'



class OneLineTag(Element):
    tag = u''

    def render(self, file_out, indent = ""):
        """Return output as a single line - versus the standard two lines"""


        file_out.write('{}<{}{}>{}</{}>\n'.format(indent, self.tag, self.attributes, self.contents[0], self.tag))

class Title(OneLineTag):
    tag = 'title'

class A(OneLineTag):
    tag = u'a'

    def __init__(self, html_address, text):
        "Overide OneLineTag module to return link and text"
        OneLineTag.__init__(self, text, a=html_address)
        
class Ul(Element):
    tag = u'u1'

class Li(Element):
    tag = u'li'

    
class H(OneLineTag):
    def __init__(self, h_counter, header):
        """Modifies Element module to return header counter if provided"""


        self.tag = u'h' + str(h_counter)
        Element.__init__(self, header)

class SelfClosingTag(Element):
    def render(self, file_out, indent=""):


        file_out.write('{}<{}{} />\n'.format(indent, self.tag, self.attributes))

class Hr(SelfClosingTag):
    tag = u'hr'

class Br(SelfClosingTag):
    tag = u'br'

class Meta(SelfClosingTag):
    tag = u'meta'

