#!/usr/bin/python3
"""Task 10"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This square inherits from a rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
