# Python - Inheritance
This document stores a simple description of each file in the  [0x0A-python-inheritance](https://github.com/arvicrin/holbertonschool-higher_level_programming/tree/master/0x0A-python-inheritance "0x0A-python-inheritance") repository.

## Files

[tests](https://github.com/arvicrin/holbertonschool-higher_level_programming/tree/master/0x0A-python-inheritance/tests "tests")
Directory where there are some Test cases

- [1-my_list.txt:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/tests/1-my_list.txt "1-my_list.txt")
Test Cases of [1-my_list.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py "1-my_list.py")

- [7-base_geometry.txt:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/tests/7-base_geometry.txt "7-base_geometry.txt")
Test cases of [7-base_geometry.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py "7-base_geometry.py")

[0-lookup.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py "0-lookup.py")
Function that returns the list of available attributes and methods of an object.

[1-my_list.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py "1-my_list.py")
Class MyList that inherits from list, Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort).

[2-is_same_class.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py "2-is_same_class.py")
Function that returns True if the object is exactly an instance of the specified class ; otherwise False.

[3-is_kind_of_class.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py "3-is_kind_of_class.py")
Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

[4-inherits_from.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py "4-inherits_from.py")
Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

[5-base_geometry.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py "5-base_geometry.py")
Empty class BaseGeometry.

[6-base_geometry.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py "6-base_geometry.py")
Class BaseGeometry, Public instance method: def area(self): that raises an Exception with the message area() is not implemented.

[7-base_geometry.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py "7-base_geometry.py")
Class BaseGeometry (based on 6-base_geometry.py), Public instance method: def integer_validator(self, name, value): that validates value., fix condition value != int.

[8-rectangle.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/8-rectangle.py "8-rectangle.py")
Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)., Instantiation with width and height: def __init__(self, width, height), width and height must be positive integers, validated by integer_validator.

[9-rectangle.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py "9-rectangle.py")
Class Rectangle that inherits from BaseGeometry, the area() method must be implemented, print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>.

[10-square.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/10-square.py "10-square.py")
Class Square that inherits from Rectangle, size must be a positive integer, validated by integer_validator, the area() method must be implemented.

[100-my_int.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/100-my_int.py "100-my_int.py")
Class MyInt that inherits from int, MyInt is a rebel. MyInt has == and != operators inverted.

[101-add_attribute.py:](https://github.com/arvicrin/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/101-add_attribute.py "101-add_attribute.py")
Function that adds a new attribute to an object if it’s possible.

## Reference 

- [Inheritance](https://intranet.hbtn.io/rltoken/E2Bs3bxX8GuSEKuWqswU7g "Inheritance")
- [Multiple inheritance](https://intranet.hbtn.io/rltoken/auwnZOKkBZ97JaLtrMryuA "Multiple inheritance")
- [Inheritance in Python](https://intranet.hbtn.io/rltoken/ycewwwPmDpXqRp2R1FW51w "Inheritance in Python")
- [Learn to Program 10 : Inheritance Magic Methods](https://intranet.hbtn.io/rltoken/F8LUzmvPI4yur1Z37ZM1fQ "Learn to Program 10 : Inheritance Magic Methods")

## Authors
[Raymond Lukwago
