#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """This writes to a file"""
    noOfChars = 0
    with open(filename, "w", encoding="utf-8") as afile:
        afile.write(text)
    return len(text)
