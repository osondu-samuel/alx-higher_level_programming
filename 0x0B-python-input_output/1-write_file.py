#!/usr/bin/python3
"""
Module containing a function to write to a file
"""


def write_file(filename="", text=""):
    """
    Function to write to a file

    Args:
        filename: the name of the file to be read.
        text: file content

    Raise:
        None
    """

    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(text)
        return f.tell()
