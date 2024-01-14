#!/usr/bin/python3
"""
Test cases for base class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Class testing place class
    """
    def setUp(self):
        """
        This checksh for issues
        """
        self.n_obq = Place()

    def test_creating(self):
        """
        Tests creating first
        """
        self.assertIsInstance(self.n_obq, BaseModel)

    def test_creating_again(self):
        """
        test creating too
        """
        self.assertIsInstance(self.n_obq, Place)

    def test_ame_attr(self):
        """
        Test the name attr
        """
        self.n_obq.name = "anyss"
        self.assertEqual(self.n_obq.name, "anyss")

    def test_with_asd(self):
        """
        Test checking the properties
        """
        self.assertTrue(hasattr(self.n_obq, "name"))
        self.assertTrue(hasattr(self.n_obq, "id"))
        self.assertTrue(hasattr(self.n_obq, "created_at"))
        self.assertTrue(hasattr(self.n_obq, "updated_at"))
        self.assertTrue(hasattr(self.n_obq, "user_id"))
        self.assertTrue(hasattr(self.n_obq, "city_id"))
        self.assertTrue(hasattr(self.n_obq, "description"))
        self.assertTrue(hasattr(self.n_obq, "number_bathrooms"))
        self.assertTrue(hasattr(self.n_obq, "price_by_night"))
        self.assertTrue(hasattr(self.n_obq, "number_rooms"))
        self.assertTrue(hasattr(self.n_obq, "longitude"))
        self.assertTrue(hasattr(self.n_obq, "max_guest"))
        self.assertTrue(hasattr(self.n_obq, "amenity_ids"))
        self.assertTrue(hasattr(self.n_obq, "latitude"))

    def test_for_id(self):
        """
        Test checking uuid
        """
        self.assertIsInstance(uuid.UUID(self.n_obq.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
