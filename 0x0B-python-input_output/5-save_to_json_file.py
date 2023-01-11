#!/usr/bin/python3
"""
Module containing a function that writes an Object
to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text
    file, using a JSON representation:

    Args:
        my_obj: a python object or data type
        filename: the file to write the JSON
                representatons to.
    """
    with open(filename, 'w+', encoding='utf-8') as filename:
        json.dump(my_obj, filename)
