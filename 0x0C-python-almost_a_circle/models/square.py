#!/usr/bin/python3
"""square.py module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises a rectangle
                Args:
                    size (int): size of the rectangle
                    x (int): integer of x coordinate
                    y (int): integer of y coordinate
                    id (int): unique base attribute id
                Raises:
                    TypeError: If args are not int (or None for id)
                    ValueError: If size is <= 0 or x, y and < 0 or id < 0
                """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        setattr(self, "width", value)

    def __str__(self):
        """Return the print() and str() representation of Square"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                       self.id,
                                                       self.x,
                                                       self.y,
                                                       self.size)

    def update(self, *args, **kwargs):
        """Update Square instances with *args and **kwargs.
               Order of *args is 'id', 'size', 'x', 'y'. **kwargs can be in
               any order.
            Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
               """
        if args and len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns dictionary representations of Instance"""
        keys = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in keys}
