#!/usr/bin/python3
"""
Module containing a function to append content to a file
"""


def append_write(filename="", text=""):
    """
    Function to append content to a file

    Args:
        filename: the name of the file to be read.
        text: file content

    Raise:
        None
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
