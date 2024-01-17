#!/usr/bin/python3
"""User class tests
    Testing user
"""
import unittest
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """User class tests
    """
    def test_email(self):
        """Tests email of user"""
        self.assertTrue(isinstance(User.email, str))
