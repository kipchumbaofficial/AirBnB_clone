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

    def test___file_path(self):
        """Tests File path atribute"""
        path = storage._FileStorage__file_path
        self.assertTrue(isinstance(path, str))
