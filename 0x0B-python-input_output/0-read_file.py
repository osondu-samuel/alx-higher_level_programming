#!/usr/bin/python3
"""
Module containing a function to read a file
"""


def read_file(filename=""):
    """
    Function to read a file

    Args:
        filename: the name of the file to be read.

    Raise:
        None
    """

    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data, end="")
