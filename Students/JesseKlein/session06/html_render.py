#!/usr/bin/env python
"""Load this module from 'run_html_render.py'

This module contains a set of classes that build a tree of html elements.
This module is design to take input from 'run_html_render.py'.
Classes:
Element -- provide core attributes and methods for a document element
HTML -- create an html element
Body -- create a body element
P -- create a paragraph element
Head -- create a head element
OneLineTag -- specify an element to not conain newlines,
    such as titles, links, and headers
Title -- create a title element
SelfClosingTag -- specify that an element is a self-closing tag
Hr -- create a horizontal rule element
Br -- create a line break element
A -- create a link element
Ul -- create an unordered list element
Li -- create a list item element
H -- create a header element
Meta -- create a meta element
"""

class Element(object):
    """Provide core attributes and methods for a document element
    
    Attributes:
    content -- a list of the content between the opening and closing tags of the element
    indent -- the indentation applied to the content
    tag -- the name applied to the tags
    attributes -- a dictionary containing the html attributes and their values for the element,
        not to be confused with the class attributes
    Methods:
    append -- append content to the content attribute
    render -- render an element in html, complete with tags, content, and indentation
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Element class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        if content:
            self.content = [unicode(content)]    # If input is given, convert to unicode
        else:
            self.content = content
	self.indent = u"  "    # Use two spaces as the indentation for html documents
        self.tag = u""
        self.attributes = kwargs    # html attributes, not to be confused with all of the class attributes


    def append(self, text):
        """Append content to the content attribute.
        
        Positional arguments:
        text -- content to be appended to the content attribute
        """
        # If 'text' input is a string or unicode and it is preceded by the same type, add the 'text' input
        # to the preceding list item. If not, append the input for text to content.
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
        """Render an element in html, complete with tags, content, and indentation.
        
        Positional arguments:
        file_out -- the destination file object for the rendered html
        Keyword arguments:
        ind -- the indentation to be applied to the content of the element (default u"")
        """
        # Create a list 'stuff' to contain the writable contents of the element, which will be joined and written to the document.
        # Build the list 'stuff' by processing the list 'content'. Indent the cases for titles, headers, and non-OneLineTags.
        # For objects in 'content', render them recursively.
        stuff = []
        for i in xrange(len(self.content)):
            if type(self.content[i]) in [str, unicode, int, float]:
                if i == 0:
                    stuff.append(u"".join([ind, self.indent]))
                elif not isinstance(self.content[i - 1], OneLineTag) or isinstance(self.content[i - 1], (Title, H)):
                    stuff.append(u"".join([ind, self.indent]))
                stuff.append(unicode(self.content[i]))
                if i == (len(self.content) - 1):
                    stuff.append(u"\n")    # Create a new line at the end of an element
                elif not isinstance(self.content[i + 1], OneLineTag) or isinstance(self.content[i + 1], (Title, H)):
                    stuff.append(u"\n")    # Create a new line at the end of a title, header, or non-OneLineTag
            else:
                self.content[i].render(file_out, ind)
                file_out.seek(0)
                line = file_out.readline()
                while line:
                    # Add the correct indentation or lack thereof
                    stuff.append(u"".join([self.indent if not isinstance(self.content[i], OneLineTag) or isinstance(self.content[i], (Title, H)) else u"", unicode(line)]))
                    line = file_out.readline()
                file_out.seek(0)
                file_out.truncate(0)

        ind = u"".join([ind, self.indent])    # Increment the indentation

        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u">\n", u"".join(stuff), u"</", self.tag, u">\n"])


class Html(Element):
    """Create an html element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    Methods:
    render -- render an element in html, call and override 'render' method from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Html class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"html"


    def render(self, file_out, ind=u""):
        """Render an element in html, complete with tags, content, and indentation.
        
        Positional arguments:
        file_out -- the destination file object for the rendered html
        Keyword arguments:
        ind -- the indentation to be applied to the content of the element (default u"")
        """
        # Prepend the document with doctype label
        Element.render(self, file_out, ind)
        file_out.seek(0)
        document = file_out.read()
        file_out.seek(0)
        file_out.writelines([u"<!DOCTYPE html>\n", document])


class Body(Element):
    """Create a body element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Body class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"body"


class P(Element):
    """Create a paragraph element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the P class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"p"


class Head(Element):
    """Create a head element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Head class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"head"


class OneLineTag(Element):
    """Specify an element to not conain newlines, such as titles, links, and headers.
    
    Inheret from Element.
    Methods:
    render -- render an element in html
    """
    def render(self, file_out, ind=u""):
        """Render an element in html, complete with tags, content, and indentation.
        
        Positional arguments:
        file_out -- the destination file object for the rendered html
        Keyword arguments:
        ind -- the indentation to be applied to the content of the element (default u"")
        """
        # Redefine render without indentation or newlines
        stuff = []
        for item in self.content:
            if type(item) in [str, unicode, int, float]:
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
        
        # Select when you want to end in a newline
        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u">", u"".join(stuff), u"</", self.tag, u">", u"\n" if self.tag in [u"title", u"h1", u"h2", u"h3", u"h4", u"h5", u"h6"] else u""])


class Title(OneLineTag):
    """Create a title element.
    
    Inherit from OneLineTag.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Title class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"title"

class SelfClosingTag(Element):
    """Specify that an element is a self-closing tag.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags
    attributes -- a dictionary containing the html attributes and their values for the element,
        not to be confused with the class attributes
    Methods:
    render -- render an element in html
    """
    def __init__(self, **kwargs):
        """Construct an instance of the SelfClosingTag Class.
        
        Keyword arguments:
        **kwargs -- the html attributes and their values for the element
        """
        self.tag = u""
        self.attributes = kwargs
        
        
    def render(self, file_out, ind=u""):
        """Render an element in html.
        
        Positional arguments:
        file_out -- the destination file object for the rendered html
        Keyword arguments:
        ind -- the indentation to be applied to the content of the element (default=u"")
        """
        # Add a newline to the end since only <hr /> and <br /> are handled
        file_out.writelines([u"<", self.tag, u"".join([u' %s="%s"' % (key, value) for key, value in self.attributes.items()]), u" />\n"])


class Hr(SelfClosingTag):
    """Create a horizontal rule element.
    
    Inherit from SelfClosingTag.
    Attributes:
    tag -- the name applied to the tag, override 'tag' attribute from SelfClosingTag
    """
    def __init__(self, **kwargs):
        """Construct an instance of the Hr class.
        
        Keyword arguments:
        **kwargs -- the html attributes and their values for the element
        """
        SelfClosingTag.__init__(self, **kwargs)
        self.tag = u"hr"


class Br(SelfClosingTag):
    """Create a line break element.
    
    Inherit from SelfClosingTag.
    Attributes:
    tag -- the name applied to the tag, override 'tag' attribute from SelfClosingTag
    """
    def __init__(self, **kwargs):
        """Construct an instance of the Br class.
        
        Keyword arguments:
        **kwargs -- the html attributes and their values for the element
        """
        SelfClosingTag.__init__(self, **kwargs)
        self.tag = u"br"


class A(OneLineTag):
    """Create a link element.
    
    Inherit from OneLineTag.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, link, content=None):
        """Construct an instance of the A class.
        
        Positional arguments:
        link -- the link attribute's value for the element, i.e. "http..."
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        """
        # link is passed as a kwarg with keyword href
        Element.__init__(self, content, href=link)
        self.tag = u"a"


class Ul(Element):
    """Create an unordered list element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Ul class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"ul"


class Li(Element):
    """Create a list item element.
    
    Inherit from Element.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, content=None, **kwargs):
        """Construct an instance of the Li class.
        
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"li"


class H(OneLineTag):
    """Create a header element.
    
    Inherit from OneLineTag.
    Attributes:
    tag -- the name applied to the tags, override 'tag' attribute from Element
    """
    def __init__(self, integer, content=None, **kwargs):
        """Construct an instance of the H class.
        
        Positional arguments:
        integer -- the number corresponding to the header size, i.e. 1-6
        Keyword arguments:
        content -- the content between the opening and closing tags of the element (default None)
        **kwargs -- the html attributes and their values for the element
        """
        Element.__init__(self, content, **kwargs)
        self.tag = u"".join([u"h", unicode(integer)])


class Meta(SelfClosingTag):
    """Create a meta element.
    
    Inherit from SelfClosingTag.
    Attributes:
    tag -- the name applied to the tag, override 'tag' attribute from SelfClosingTag
    """
    def __init__(self, **kwargs):
        """Construct an instance of the Meta class.
        
        Keyword arguments:
        **kwargs -- the html attributes and their values for the element
        """
        SelfClosingTag.__init__(self, **kwargs)
        self.tag = u"meta"

