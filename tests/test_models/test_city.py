#!/usr/bin/python3
"""City Class Tests
    Unit tests for city class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City class"""
    def test_state_id(self):
        """Tests State id attribute"""
        self.assertTrue(isinstance(City.state_id, str))

    def test_name(self):
        """Tests city name"""
        self.assertTrue(isinstance(City.name, str))
