#!/usr/bin/python3
"""task 10"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            dic = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dic[key] = value
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        values = json
        try:
            self.first_name = values["first_name"]
        except Exception:
            pass
        try:
            self.last_name = values["last_name"]
        except Exception:
            pass
        try:
            self.age = values["age"]
        except Exception:
            pass
