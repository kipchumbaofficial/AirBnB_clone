#!/usr/bin/python3
"""City Class Module
    Details about a city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class
        Blueprint for a city
    """
    state_id = ""
    name = ""
