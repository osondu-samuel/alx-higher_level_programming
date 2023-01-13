#!/usr/bin/python3
"""rectangle.py module"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a rectangle
        Args:
            width (int): size of the rectangle
            height (int): size of the rectangle
            x (int): integer
            y (int): integer
            id (int): unique base attribute id
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays # of area to stdout"""
        if self.__height == 0 or self.__width == 0:
            print("")
        for z in range(self.__y):
            print("")
        for i in range(self.__height):
            for d in range(self.__x):
                print(' ', end='')
            for a in range(self.__width):
                print('#', end='')
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Function assigns arguments to each attribute"""
        if args and len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self.x = arg
                elif num == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs.get('id')
            if "width" in kwargs:
                self.width = kwargs.get('width')
            if "height" in kwargs:
                self.height = kwargs.get('height')
            if "x" in kwargs:
                self.x = kwargs.get('x')
            if "y" in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """Returns dictionary representations of Instance"""
        keys = ["id", "width", "height", "x", "y"]
        return {K: getattr(self, K) for K in keys}
