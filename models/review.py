#!/usr/bin/python3
"""Review Class Module
    Review Blueprint
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
        Review Model
    """
    place_id = ""
    user_id = ""
    text = ""
