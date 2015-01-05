#!/usr/bin/env python
"""Very basic p-wrapper decorator.

Use p_wrapper to take a function that returns a string
as input and output a string wrapped in html 'p' tags.
"""

def p_wrapper(func):
    """Function for p_wrapper

    Positional arguments:
    func -- input function that returns a string
    """
    def wrapped(my_string):
        """Function which extends the output from another function to include 'p' tags

        Positional arguments:
        my_string -- a string
        """
        result = func(my_string)
        wrapped_result = result.join(["<p>", "</p>"])
        return wrapped_result
    return wrapped

