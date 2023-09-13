#!/usr/bin/python3
"""task 4"""


import json


def from_json_string(my_str):
    """This returns an object rerpresented by a JSON string"""
    return json.loads(my_str)
