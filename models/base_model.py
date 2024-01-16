#!/usr/bin/python3
"""Base Class Module
    Contains a base class BaseModel from
    which other classes will inherit from
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel
        A class defining all common attributes/methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes instance atrributes"""
        if args:
            pass
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, date_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Returns informal representation of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a dictionary
            Containing all key/values of __dict__ of instance
        """
        retval = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                retval[key] = value.isoformat()
            else:
                retval[key] = value
        retval['__class__'] = type(self).__name__
        return retval
