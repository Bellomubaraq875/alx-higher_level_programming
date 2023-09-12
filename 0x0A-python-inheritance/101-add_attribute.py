#!/usr/bin/python3
"""task 13"""


def add_attribute(obj, attribute, value):
    """This checks if a new attribute can
    be added to an object and raises a typeerror if it can not
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
