"""
   6-base_geometry.py module
   Class BaseGeometry, Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self): \
           that raises an Exception with\
           the message area() is not implemented
           """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
