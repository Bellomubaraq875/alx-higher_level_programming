#!/usr/bin/python3
"""Task 4
"""


def inherits_from(obj, a_class):
    """This function returns True if
    the onject js an instance of an ingerited class
    from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
