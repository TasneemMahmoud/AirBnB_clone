#!/usr/bin/python3
"""
Test cases for Amenity class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Class to test amenity class
    """
    def setUp(self):
        """
        This method starting seting up
        """
        self.theawe = Amenity()

    def test_creating(self):
        """
        Test creating new one
        """
        self.assertIsInstance(self.theawe, BaseModel)

    def test_create(self):
        """
        Tests creating the new obj
        """
        self.assertIsInstance(self.theawe, Amenity)

    def test_name(self):
        """
        Test set name
        """
        self.theawe.name = "ayhaga"
        self.assertEqual(self.theawe.name, "ayhaga")

    def test_is_with(self):
        """
        Tests has attrbuite
        """
        self.assertTrue(hasattr(self.theawe, "name"))
        self.assertTrue(hasattr(self.theawe, "id"))
        self.assertTrue(hasattr(self.theawe, "created_at"))
        self.assertTrue(hasattr(self.theawe, "updated_at"))

    def test_for_id(self):
        """
        Tests teh uuid checking
        """
        self.assertIsInstance(uuid.UUID(self.theawe.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
