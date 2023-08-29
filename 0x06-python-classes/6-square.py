#!/usr/bin/python3
""" this class defines a square with optiuonal size"""


class Square:
    """This is the classs
    the name is Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """size must be optional, that is why it is equal to 0
        it must also be an integer
        """
        self.size = size
        self.position = position

    def area(self):
        """This function returns the area of a square
        by raising the size to the power of two
        or multiplying it by itself
        """
        return (self.__size * self.__size)

    def my_print(self):
        """This function prints the area of the square to stdout
        this is printed with the hash character
        and an empty line is size is 0
        """
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                for blanks in range(self.position[0]):
                    print(" ", end="")
                for c in range(self.__size):
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

    @property
    def position(self):
        """This returns the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
