#!/usr/bin/python3
"""This directory is task 1
under the tasks on 0x0A in the
directory given
"""


class MyList(list):
    """This is a class
    that inherits from
    another class
    """

    def print_sorted(self):
        """This function
        sorts then prints all
        elements in a list
        """
        print(sorted(self))
