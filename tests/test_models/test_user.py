#!/usr/bin/python3
"""
Test the user casses class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Testing casse class
    """
    def setUp(self):
        """
        checking for user casses test
        """
        self.pers = User()

    def test_creating_first(self):
        """
        Test creating and method test
        """
        self.assertIsInstance(self.pers, BaseModel)

    def test_creating_too(self):
        """
        Creating again to
        """
        self.assertIsInstance(self.pers, User)

    def test_checking_the(self):
        """
        Checking for all things
        """
        self.pers.name = "Mikesl"
        self.assertEqual(self.pers.name, "Mikesl")

    def test_hmaas_asr(self):
        """
        Test casses for all it hase
        """
        self.assertTrue(hasattr(self.pers, "id"))
        self.assertTrue(hasattr(self.pers, "created_at"))
        self.assertTrue(hasattr(self.pers, "updated_at"))
        self.assertTrue(hasattr(self.pers, "email"))
        self.assertTrue(hasattr(self.pers, "password"))
        self.assertTrue(hasattr(self.pers, "first_name"))
        self.assertTrue(hasattr(self.pers, "last_name"))

    def test_uuid_to_id(self):
        """
        Checking validation for uuid with id
        """
        self.assertIsInstance(uuid.UUID(self.pers.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
