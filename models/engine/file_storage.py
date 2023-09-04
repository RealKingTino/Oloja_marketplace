#!/usr/bin/python3
"""a module that serializes instances to a JSON file and deserializes JSON
    file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
import sys



class FileStorage:
    """ FileStorage class serializes instances to a JSON file
        and deserializes JSON file to instances
        Private method:
            __file_path: a private attribute that holds name of file
            __objects: a private attribute for object
        Public method:
            all: a method that returns the dictionary of an __objects
            new: a method that sets a private attribute with key value (id)
            reload: a method that deserialize the JSON file to private
            objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "."
        key += str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        j_dict = {}
        for key in self.__objects:
            j_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(j_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    name = sys.modules[__name__]
                    my_class = getattr(name, value['__class__'])
                    self.__objects[key] = my_class(**value)
