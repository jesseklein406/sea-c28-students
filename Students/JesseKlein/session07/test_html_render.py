#!/usr/bin/env python
"""Test file for 'html_render.py

Execute this file to run unit tests for 'html_render.py'
"""

import html_render
import cStringIO
import unittest

class HtmlTestCase(unittest.TestCase):
    def test_html(self):
        f = cStringIO.StringIO()
        html_el = html_render.Html(u"this is content", this=u"is in the tag")
        html_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<!DOCTYPE html>\n<html this="is in the tag">\n  this is content\n</html>\n'    # Add two spaces for indentation
        
        self.assertEquals(actual, expected)


class BodyTestCase(unittest.TestCase):
    def test_body(self):
        f = cStringIO.StringIO()
        body_el = html_render.Body(u"this is content", this=u"is in the tag")
        body_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<body this="is in the tag">\n  this is content\n</body>\n'
        
        self.assertEquals(actual, expected)


class PTestCase(unittest.TestCase):
    def test_p(self):
        f = cStringIO.StringIO()
        p_el = html_render.P(u"this is content", this=u"is in the tag")
        p_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<p this="is in the tag">\n  this is content\n</p>\n'
        
        self.assertEquals(actual, expected)


class HeadTestCase(unittest.TestCase):
    def test_head(self):
        f = cStringIO.StringIO()
        head_el = html_render.Head(u"this is content", this=u"is in the tag")
        head_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<head this="is in the tag">\n  this is content\n</head>\n'
        
        self.assertEquals(actual, expected)


class TitleTestCase(unittest.TestCase):
    def test_title(self):
        f = cStringIO.StringIO()
        title_el = html_render.Title(u"this is content", this=u"is in the tag")
        title_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<title this="is in the tag">this is content</title>\n'
        
        self.assertEquals(actual, expected)


class HrTestCase(unittest.TestCase):
    def test_hr(self):
        f = cStringIO.StringIO()
        hr_el = html_render.Hr(this=u"is in the tag")
        hr_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<hr this="is in the tag" />\n'
        
        self.assertEquals(actual, expected)


class BrTestCase(unittest.TestCase):
    def test_br(self):
        f = cStringIO.StringIO()
        br_el = html_render.Br(this=u"is in the tag")
        br_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<br this="is in the tag" />\n'
        
        self.assertEquals(actual, expected)


class ATestCase(unittest.TestCase):
    def test_a(self):
        f = cStringIO.StringIO()
        a_el = html_render.A(u"this is the link", u"this is content")
        a_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<a href="this is the link">this is content</a>'
        
        self.assertEquals(actual, expected)


class UlTestCase(unittest.TestCase):
    def test_ul(self):
        f = cStringIO.StringIO()
        ul_el = html_render.Ul(u"this is content", this=u"is in the tag")
        ul_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<ul this="is in the tag">\n  this is content\n</ul>\n'
        
        self.assertEquals(actual, expected)


class LiTestCase(unittest.TestCase):
    def test_li(self):
        f = cStringIO.StringIO()
        li_el = html_render.Li(u"this is content", this=u"is in the tag")
        li_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<li this="is in the tag">\n  this is content\n</li>\n'
        
        self.assertEquals(actual, expected)


class HTestCase(unittest.TestCase):
    def test_h(self):
        f = cStringIO.StringIO()
        h_el = html_render.H(6, u"this is content", this=u"is in the tag")
        h_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<h6 this="is in the tag">this is content</h6>\n'
        
        self.assertEquals(actual, expected)


class MetaTestCase(unittest.TestCase):
    def test_meta(self):
        f = cStringIO.StringIO()
        meta_el = html_render.Meta(this=u"is in the tag")
        meta_el.render(f)
        f.seek(0)
        actual = unicode(f.read())
        expected = u'<meta this="is in the tag" />\n'
        
        self.assertEquals(actual, expected)


if __name__ == "__main__":
    unittest.main()

