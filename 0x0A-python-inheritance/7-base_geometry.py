#!/usr/bin/python3
"""Task 7
"""


class BaseGeometry:
    """an BaseGeometry class
    """
    def area(self):
        """This is supposed to define an area of a geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates a string called Value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
