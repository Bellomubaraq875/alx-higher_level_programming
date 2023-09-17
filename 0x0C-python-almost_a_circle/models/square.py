#!/usr/bin/python3
"""task 10 and below"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class called square inherits from a previously written
    class called Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """classs constructor for the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """the parameter setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a given calc"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """task 12, updating the square with attributes"""
        if args and len(args) != 0:
            b = 0
            for argument in args:
                if b == 0:
                    if argument is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argument
                elif b == 1:
                    self.size = argument
                elif b == 2:
                    self.x = argument
                elif b == 3:
                    self.y = argument
                b += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
