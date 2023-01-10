#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is\
    exactly an instance of the specified class \
    ; otherwise False"""
    if isinstance(a_class(), type(obj)):
        return True
    else:
        return False
