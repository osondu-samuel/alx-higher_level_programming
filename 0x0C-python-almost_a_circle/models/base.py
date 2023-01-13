#!/usr/bin/python3
"""A module containing Base Class of
all other classes in this project
"""
import json


class Base:
    """Represents a Base Class
    Attributes:
         __nb_objects (object): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convents python dictionaries to jason strings"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Function for loading json data from a string"""
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a jason string to file like object"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                lst = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(lst))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        c.update(**dictionary)
        return c

    @classmethod
    def load_from_file(cls):
        """Loads json string and returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__),
                      mode='r', encoding='utf-8') as rf:
                lst_dictionaries = cls.from_json_string(rf.read())
                return [cls.create(**i) for i in lst_dictionaries]
        except FileNotFoundError:
            return []
