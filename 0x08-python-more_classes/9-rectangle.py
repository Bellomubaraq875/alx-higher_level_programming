#!/usr/bin/python3
"""
This program creates an class that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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

    def area(self):
        """Public instance method that returns
        the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """This function returns
        the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

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
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """This prints a message for
        every deletion of
        the rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This static method returns the
        biggest rectangle based on their areas.
        The comparison is between two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """This uses class method
        to return anew rectangle instance
        """
        return cls(size, size)
