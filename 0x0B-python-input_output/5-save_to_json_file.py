#!/usr/bin/python3
"""Task 5"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as afile:
        json.dump(my_obj, afile)
