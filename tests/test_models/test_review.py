#!/usr/bin/python3
"""Review Class Tests
    Unit Testing Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review Class Test Cases"""
    def test_place_id(self):
        """Tests Place id"""
        self.assertTrue(isinstance(Review.place_id, str))

    def test_user_id(self):
        """Test User id"""
        self.assertTrue(isinstance(Review.user_id, str))

    def test_text(self):
        """Test Text"""
        self.assertTrue(isinstance(Review.text, str))
