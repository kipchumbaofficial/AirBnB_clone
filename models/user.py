#!/usr/bin/python3
"""User Class Module
    Class representation of a user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
        Creates a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Does initialization of base class"""
        super().__init__()
