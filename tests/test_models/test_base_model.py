#!/usr/bin/python3
"""BaseModel Tests
    Testing BaseModel using python unittest module
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel
        BaseModel BaseClass
    """

    def setUp(self):
        """Test setUp function to be executed before each test"""
        self.test_obj = BaseModel()

    def test_id(self):
        """Tests if id is converted to a string"""
        self.assertEqual(type(self.test_obj.id), str)

    def test_created_at(self):
        """Checks if created_at is an instance of datetime"""
        self.assertTrue(isinstance(self.test_obj.created_at, datetime))

    def test_updated_at(self):
        """Checks if updated_at is an instance of datetime"""
        self.assertTrue(isinstance(self.test_obj.updated_at, datetime))

    def test___str__(self):
        """Tests __str__ of base clase"""
        pass

    def test_to_dict(self):
        """Test to_dict"""
        result = self.test_obj.to_dict()
        self.assertTrue('created_at' in result)
        self.assertTrue(isinstance(result['created_at'], str))


if __name__ == "__main__":
    unittest.main()
