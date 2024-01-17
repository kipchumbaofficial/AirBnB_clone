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

    def test_password(self):
        """Tests User Password"""
        self.assertTrue(isinstance(User.password, str))

    def test_first_name(self):
        """Tests User First name"""
        self.assertTrue(isinstance(User.first_name, str))

    def test_last_name(self):
        """Tests User Last Name"""
        self.assertTrue(isinstance(User.last_name, str))
