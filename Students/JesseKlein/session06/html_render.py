#!/usr/bin/env python

class Element(object):
    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [unicode(content)]
        else:
            self.content = content
	self.indent = u"  "
        self.tag = u""
        self.attributes = kwargs


    def append(self, text):
        if type(text) in [str, unicode]:
            if self.content:
                if type(self.content[-1:][0]) == type(text):
                    self.content[-1:][0] = type(text)("").join([self.content[-1:][0], text])
                else:
                    self.content.append(text)
            else:
                self.content = [unicode(text)]
        else:
            if self.content:
                self.content.append(text)
            else:
                self.content = [text]
                

    def render(self, file_out, ind=u""):
        stuff = []
        for i in xrange(len(self.content)):
            if type(self.content[i]) in [str, unicode]:
                if i == 0:
                    stuff.append(u"".join([ind, self.indent]))
                elif not isinstance(self.content[i - 1], OneLineTag) or isinstance(self.content[i - 1], Title):
                    stuff.append(u"".join([ind, self.indent]))
                stuff.append(unicode(self.content[i]))
                if i == (len(self.content) - 1):
                    stuff.append(u"\n")
                elif not isinstance(self.content[i + 1], OneLineTag) or isinstance(self.content[i + 1], Title):
                    stuff.append(u"\n")
            else:
                self.content[i].render(file_out, ind)
                file_out.seek(0)
                line = file_out.readline()
                while line:
                    stuff.append(u"".join([self.indent, unicode(line)]))
                    line = file_out.readline()
                file_out.seek(0)
                file_out.truncate(0)

        ind = u"".join([ind, self.indent])

        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u">\n", u"".join(stuff), u"</", self.tag, u">\n"])


class Html(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = u"html"


class Body(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = u"body"


class P(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = u"p"


class Head(Element):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = u"head"


class OneLineTag(Element):
    def render(self, file_out, ind=u""):
        stuff = []
        for item in self.content:
            if type(item) in [str, unicode]:
                stuff.append(unicode(item))
            else:
                item.render(file_out, ind)
                file_out.seek(0)
                line = file_out.readline()
                while line:
                    stuff.append(unicode(line))
                    line = file_out.readline()
                file_out.seek(0)
                file_out.truncate(0)
        
        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u">", u"".join(stuff), u"</", self.tag, u">", u"\n" if self.tag in [u"title"] else u""])


class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.tag = u"title"

class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.indent = u"  "
        self.tag = u""
        self.attributes = kwargs

        
    def render(self, file_out, ind=u""):
        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u" />\n"])

