#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Class to test city class
    """
    def setUp(self):
        """
        SetUp finction
        """
        self.the_obj = City()

    def test_creating(self):
        """
        Tests creating
        """
        self.assertIsInstance(self.the_obj, BaseModel)

    def test_create_again(self):
        """
        tests creating too
        """
        self.assertIsInstance(self.the_obj, City)

    def test_set_name(self):
        """
        Tests set name
        """
        self.the_obj.name = "USA"
        self.assertEqual(self.the_obj.name, "USA")

    def test_has_attr(self):
        """
        Tests with attrs checking
        """
        self.assertTrue(hasattr(self.the_obj, "name"))
        self.assertTrue(hasattr(self.the_obj, "id"))
        self.assertTrue(hasattr(self.the_obj, "created_at"))
        self.assertTrue(hasattr(self.the_obj, "updated_at"))
        self.assertTrue(hasattr(self.the_obj, "state_id"))

    def test_for_id(self):
        """
        Test the uuid class
        """
        self.assertIsInstance(uuid.UUID(self.the_obj.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
