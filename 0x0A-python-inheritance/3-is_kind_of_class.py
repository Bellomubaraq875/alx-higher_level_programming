#!/usr/bin/python3
"""This is task 3 of the Pythin inheritance tasks
"""


def is_kind_of_class(obj, a_class):
    """This function returns true if the object
    is an instance of a specified class
    or ingerited class of the specified class
    """
    return isinstance(obj, a_class)
