#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """This function reads a text file encoded with utf8"""
    with open(filename, encoding="utf-8") as afile:
        print(afile.read(), end='')
