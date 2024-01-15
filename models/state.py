#!/usr/bin/python3
"""State Class Module
    Blue Print for the state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class to create state"""
    name = ""

    def __init__(self):
        """Initialize Base class"""
        super().__init__()
