#!/usr/bin/python3
"""BaseModel Tests
    Testing BaseModel using python unittest module
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """TestBaseModel
        BaseModel BaseClass
    """
    def setUp(self):
        """Test setUp function to be executed before each test"""
        self.test_object = BaseModel()

    def test_id(self):
        """Tests if id is converted to a string"""
        self.assertEqual(type(self.test_object.id), str)

if __name__ == "__main__":
    unittest.main()
