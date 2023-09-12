#!/usr/bin/python3
"""This is for task 2 of the python
inheritance class
"""


def is_same_class(obj, a_class):
    """This function returns True
    if thr object js the smae class as the soecidied class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
