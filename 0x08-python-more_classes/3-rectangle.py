#!/usr/bin/python3
"""
This program creates an class that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This sets the width of the rectangle
        and its expected conditions
        """
        return self.__width

    @property
    def height(self):
        """This sets the private instance attribute height,
        for the Rectangle created
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the given conditions for the width
        of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """This sets the given requirement for
        the private instance attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Task 3: return printable rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        """algorithm to print rectangle with #"""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
