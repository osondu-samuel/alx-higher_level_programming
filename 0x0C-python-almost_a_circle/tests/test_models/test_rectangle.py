#!/usr/bin/python3
"""Test Suite for Class Rectangle
Email: lukwagoraymond3@gmail.com
Unittest Classes:
    TestRectangleDoc - Line ##
    TestRectangleInstantiation - Line ##
    TestRectangleWidthVal - Line ##
    TestRectangleHeightVal - Line ##
    TestRectangleXVal - Line ##
    TestRectangleYVal - Line ##
    TestRectangleArea - Line ##
    TestRectangleUpdateKwargs - Line ##
"""
import unittest
import os
import json
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.rectangle import __doc__ as module_doc


class TestRectangle(unittest.TestCase):
    """Subclass of unittest.TestCase to test Rectangle class functionality"""

    def setUp(self):
        """Redirect stdout to readable buffer to check output
        of methods relying on print function"""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file
        stream to sys.stdout so printing goes to the screen
        as before"""
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        """Test for existence of docstrings"""
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIs(hasattr(Rectangle, "to_json_string"), True)
        self.assertIsNotNone(Rectangle.to_json_string.__doc__)
        self.assertIs(hasattr(Rectangle, "from_json_string"), True)
        self.assertIsNotNone(Rectangle.from_json_string.__doc__)
        self.assertIs(hasattr(Rectangle, "save_to_file"), True)
        self.assertIsNotNone(Rectangle.save_to_file.__doc__)
        self.assertIs(hasattr(Rectangle, "load_from_file"), True)
        self.assertIsNotNone(Rectangle.load_from_file.__doc__)


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle Class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(2, 10), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 3)
        r2 = Rectangle(11, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 3, 4)
        r2 = Rectangle(2, 6, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 9, 0, 7).id)

    def test_move_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    # Tests for whether attribute is private
    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    # Tests for Getters
    def test_width_getter(self):
        r = Rectangle(5, 5, 0, 0, 1)
        self.assertEqual(5, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 6, 0, 0, 1)
        self.assertEqual(6, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 5, 10, 0, 1)
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 5, 10, 0, 1)
        self.assertEqual(0, r.y)

    # Tests for Setters
    def test_height_setter(self):
        r1 = Rectangle(5, 5, 0, 0, 1)
        r1.height = 10
        self.assertEqual(10, r1.height)

    def test_width_setter(self):
        r1 = Rectangle(5, 5, 0, 0, 1)
        r1.width = 8
        self.assertEqual(8, r1.width)

    def test_x_setter(self):
        r1 = Rectangle(5, 5, 0, 0, 1)
        r1.x = 1
        self.assertEqual(1, r1.x)

    def test_y_setter(self):
        r1 = Rectangle(5, 5, 0, 0, 1)
        r1.y = 2
        self.assertEqual(2, r1.y)


# Tests for value validation of width
class TestRectangleWidthVal(unittest.TestCase):
    """Unittests for validating width attribute"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.7, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Practice', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memory_view_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcdefg'), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 3}), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)
            Rectangle(float('-inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_equals_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)


# Tests for value validation of height
class TestRectangleHeightVal(unittest.TestCase):
    """Unittests for validating width attribute"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "string")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 2.4)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, False)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, b'Practice')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b'abcdefg'))

    def test_memory_view_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(b'abcdefg'))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(5))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({1, 2, 3, 3}))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'))
            Rectangle(2, float('-inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'))

    def test_equals_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)


# Tests for value validation of x Coordinate Attribute
class TestRectangleXVal(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memory_view_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcdefg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)
            Rectangle(1, 2, float('-inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


# Tests for value validation of y Coordinate Attribute
class TestRectangleYVal(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memory_view_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcdefg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))
            Rectangle(1, 2, 1, float('-inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


# Tests for Area Method under Rectangle Class
class TestRectangleArea(unittest.TestCase):
    """Unittests for testing Area method"""

    def test_area_small(self):
        r1 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(8, r1.area())

    def test_area_large(self):
        r1 = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r1.area())

    def test_area_change_attributes(self):
        r1 = Rectangle(2, 4, 0, 0, 1)
        r1.width = 10
        r1.height = 9
        self.assertEqual(90, r1.area())

    def test_area_one_argument(self):
        r1 = Rectangle(2, 4, 0, 0, 1)
        with self.assertRaises(TypeError):
            r1.area(1)


# Tests for Display & Str Methods in Rectangle Class
class TestRectangleDisplayStr(unittest.TestCase):
    """Unittests for methods Display & str to stdout"""

    def setUp(self):
        """Redirect stdout to readable buffer to check output
        of methods relying on print function"""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file
        stream to sys.stdout so printing goes to the screen
        as before"""
        sys.stdout = sys.__stdout__

    def test_display_width_height(self):
        r = Rectangle(4, 5, 0, 0, 0)
        r_out = "####\n####\n####\n####\n####\n"
        try:
            r.display()
            self.assertEqual(sys.stdout.getvalue(), r_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_display_width_height_x(self):
        r1 = Rectangle(3, 2, 1, 0, 1)
        r1_out = " ###\n ###\n"
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_display_width_height_y(self):
        r2 = Rectangle(4, 5, 0, 1, 0)
        r2_out = "\n####\n####\n####\n####\n####\n"
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), r2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_display_width_height_x_y(self):
        r3 = Rectangle(2, 4, 3, 2, 0)
        r3_out = "\n\n   ##\n   ##\n   ##\n   ##\n"
        try:
            r3.display()
            self.assertEqual(sys.stdout.getvalue(), r3_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    # Test __str__ method
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (30) 1/0 - 5/5")

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        correct = "[Rectangle] ({}) 0/0 - 4/6".format(r.id)
        self.assertEqual(str(r), correct)


# Tests for Args Methods in Rectangle Class
class TestRectangleUpdateArgs(unittest.TestCase):
    """Test that `update()` method works with *args unpacking"""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))


# Tests for Kwargs Methods in Rectangle Class
class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test that `update()` method works with *kwargs unpacking"""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/10", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, id=89, x=1, height=2)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))


class TestRectangleToDictionary(unittest.TestCase):
    """Test that `to_dictionary()` method produces valid dictionary
        representation of Rectangle instance. Converts to dictionary and
        updates distinct instance to those values and compares the two
        resulting objects to show that they have the same attributes but
        are not identical objects.
        """

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

    if __name__ == "__main__":
        unittest.main()
