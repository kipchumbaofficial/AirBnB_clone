#!/usr/bin/python3
"""FileStorage Class Module
    A module to Handle JSON Serialization & Deserialization
"""
import json
from models import base_model
import os

BaseModel = base_model.BaseModel


class FileStorage:
    """FileStorage Class
        A class handling JSON encoding and Decoding
    """
    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """Returns class attribute __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj in __objects for serialization"""
        key = type(obj).__name__ + "." + obj.id
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """JSON Encoder"""
        dict_from = {}
        for key, value in FileStorage.__objects.items():
            dict_from[key] = value.to_dict()
        json_str = json.dumps(dict_from)
        path = FileStorage.__file_path
        with open(path, "w", encoding="utf-8") as file_to:
            file_to.write(json_str)

    def reload(self):
        """JSON Decoder"""
        dict_to = {}
        FileStorage.__objects = {}
        if not os.path.exists(FileStorage.__file_path):
            return
        path = FileStorage.__file_path
        with open(path, "r", encoding="utf-8") as file_from:
            dict_to = json.load(file_from)
            for key, value in dict_to.items():
                class_name = key.split(".")[0]
                if class_name == "BaseModel":
                    FileStorage.__objects[key] = eval(class_name)(**value)
                else:
                    pass
