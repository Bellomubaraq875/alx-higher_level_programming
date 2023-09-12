#!/usr/bin/python3
"""Task 9
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

    def area(self):
        """This function returns the area
        of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """This rertuens the desciption of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
