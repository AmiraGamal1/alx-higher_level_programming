#!/usr/bin/python3
"""base class to manage instance id"""
import json


class Base:
    """base class model
    Private class attribute: (int) __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list to JSON"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to the json file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """return list from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """set the attribute from dictionary"""
        if dictionary and dictionary is not dict:
            if cls.__name__ == "Rectangle":
                ins = cls(1, 1)
            else:
                ins = cls(1)
            ins.update(**dictionary)
            return ins

    @classmethod
    def load_from_file(cls):
        """load from json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dict = Base.from_json_string(file.read())
                ins = [cls.create(**dictionary) for dictionary in list_dict]
                return ins
        except IOError:
            return []
