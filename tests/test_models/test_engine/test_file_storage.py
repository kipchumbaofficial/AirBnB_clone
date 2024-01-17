#!/usr/bin/python3
"""Unittests for FileStorage
    JSON serialization and Deserialization tests
"""
import json
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage Class"""

    def setUp(self):
        """Prepares for test"""
        self.test_obj = BaseModel()
        self.dict_obj = storage._FileStorage__objects

    def test___file_path(self):
        """Tests File path atribute"""
        path = storage._FileStorage__file_path
        self.assertTrue(isinstance(path, str))
        self.assertTrue(path == 'file.json')

    def test___object(self):
        """Tests Object attribute"""
        self.assertTrue(isinstance(self.dict_obj, dict))

    def test_all(self):
        """Tests all() method"""
        retval = storage.all()
        self.assertTrue(retval == self.dict_obj)

    def test_new(self):
        """Tests new() method
