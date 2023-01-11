#!/usr/bin/python3
"""
Importing the JSON module from python libraries
Module that contains a function that returns the python
object of a JSON representation
"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: a JSON string.

    Raises:
        Exception: when the object can't be decoded
    """

    return json.loads(my_str)
