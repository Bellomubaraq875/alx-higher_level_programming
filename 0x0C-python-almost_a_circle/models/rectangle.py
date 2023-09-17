#!/usr/bin/python3
"""This is a class called Rectangler that inheits from the class
called Base"""


from models.base import Base


class Rectangle(Base):
    """This represents a class called Rectangle
    with its own attributes and the getters and
    setters for its attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor of theclass Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property getter for instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter fdore the attribute: width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Property getter for instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height for attribute height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """property getter for attribute 'x' """
        return self.__x

    @x.setter
    def x(self, value):
        """this sets the method for the attributre called 'x' """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """property getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the method forthe y attribute"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """This returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """this prints out the rectanglewith the character #"""
        for a in range(self.height):
            print('#' * self.width)

    def display(self):
        """task 7: print to stdout, the rectangle using #
        and taking care of attributes x and y"""
        print("\n" * self.__y, end='')
        for b in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """this overrides a method, task 6"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """tasks 8 and 9, this assigns an argument
        to each attribute"""
        if args and len(args) != 0:
            b = 0
            for argument in args:
                if b == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                elif b == 1:
                    self.width = argument
                elif b == 2:
                    self.height = argument
                elif b == 3:
                    self.x = argument
                elif b == 4:
                    self.y = argument
                b += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        try:
            self.__id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
