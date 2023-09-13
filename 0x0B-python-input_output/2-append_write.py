#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """This function appends a stri8ng to the end of a file
    and creates the file if it does not exust before
    """
    with open(filename, "a", encoding="utf-8") as afile:
        return afile.write(text)
