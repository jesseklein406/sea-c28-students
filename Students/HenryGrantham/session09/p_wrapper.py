# -*- coding: utf-8 -*-


def p_wrapper(func):
    """Wraps original output in an HTML 'p' tag
    """
    def wrapped(text):
        result = u"<p> {} </p>".format(func(text))
        return result
    return wrapped


@p_wrapper
def return_a_string(string):
    """Returns a string
    """
    return string
