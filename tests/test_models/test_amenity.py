#!/usr/bin/python3
"""Amenity class tests
    Tests Amenity attributes and methods using:
    unittest module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity Class tests"""
    def test_name(self):
        self.assertTrue(isinstance(Amenity.name, str))
