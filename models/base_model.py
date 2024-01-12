#!/usr/bin/python3
"""Base Class Module
    Contains a base class BaseModel from
    which other classes will inherit from
"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel
        A class defining all common attributes/methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes instance atrributes"""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs.pop('__class__', None)
            creation_date = kwargs.get('created_at')
            kwargs['created_at'] = datetime.strptime(creation_date, date_format)
            updating_date = kwargs.get('updated_at')
            kwargs['updated_at'] = datetime.strptime(updating_date, date_format)
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates updated_at when instance is changed"""
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns informal representation of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a dictionary
            Containing all key/values of __dict__ of instance
        """
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['__class__'] = type(self).__name__
        return self.__dict__
