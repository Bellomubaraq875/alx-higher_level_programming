#!/usr/bin/python3
"""Task 8
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class bamed Rectangle
    and it inherits grim the class BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
