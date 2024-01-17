#!/usr/bin/python3
"""State Class Tests
    State class tests
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests class State"""
    def test_name(self):
        """Tests State Name"""
        self.assertTrue(isinstance(State.name, str))
