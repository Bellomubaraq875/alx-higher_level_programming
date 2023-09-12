#!/usr/bin/python3
"""Task 11"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This square inherits from a rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
