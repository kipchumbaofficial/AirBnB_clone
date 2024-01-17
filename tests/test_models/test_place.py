#!/usr/bin/python3
"""PLace Class tests
    Unit Testing Place Class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests Place Class"""
    def test_city_id(self):
        """Tests City id"""
        self.assertTrue(isinstance(Place.city_id, str))

    def test_user_id(self):
        """Tests User id"""
        self.assertTrue(isinstance(Place.user_id, str))

    def test_name(self):
        """Tests Place Name"""
        self.assertTrue(isinstance(Place.name, str))

    def test_description(self):
        """Tests Place Description"""
        self.assertTrue(isinstance(Place.description, str))

    def test_number_rooms(self):
        """Tests Number of rooms"""
        self.assertTrue(isinstance(Place.number_rooms, int))

    def test_number_bathrooms(self):
        """Tests Number of Bathrooms"""
        self.assertTrue(isinstance(Place.number_bathrooms, int))

    def test_max_guest(self):
        """Tests Max guest"""
        self.assertTrue(isinstance(Place.max_guest, int))

    def test_price_by_night(self):
        """Tests Price Per Night"""
        self.assertTrue(isinstance(Place.price_by_night, int))

    def test_latitude(self):
        """Tests Latitude coordinates"""
        self.assertTrue(isinstance(Place.latitude, float))

    def test_longitude(self):
        """Tests Longitude coordinates"""
        self.assertTrue(isinstance(Place.longitude, float))

    def test_amenity_ids(self):
        """Tests ammenity ids"""
        self.assertTrue(isinstance(Place.amenity_ids, list))
