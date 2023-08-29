#!/usr/bin/python3
""" this class defines a square with optiuonal size"""


class Square:
    """This is the classs
    the name is Square
    """
    def __init__(self, size=0):
        """size must be optional, that is why it is equal to 0
        it must also be an integer
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
