#!/usr/bin/python3
"""Amenity class Module
    Amenities available
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
        Amenities available
    """
    name = ""

    def __init__(self):
        super().__init__()
