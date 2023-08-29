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
        self.size = size

    def area(self):
        """This function returns the area of a square
        by raising the size to the power of two
        or multiplying it by itself
        """
        return (self.__size * self.__size)

    def my_print(self):
        """This function prints the area of the square to stdout
        thius is printed with thehash character
        and an empty line is size is 0
        """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """This is a fproperty function
        it retrieves the value odf size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Thius is a value setter
        it sets the vslue of size to conform with given attributes
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
