#!/usr/bin/python3
"""
Test anything for review
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Class to checking for issue in review
    """
    def setUp(self):
        """
        This start in the first
        """
        self.adewq = Review()

    def test_creating_one(self):
        """
        Test to creating
        """
        self.assertIsInstance(self.adewq, BaseModel)

    def test_create_again(self):
        """
        Test for creating too
        """
        self.assertIsInstance(self.adewq, Review)

    def test_with_attr_asm(self):
        """
        Test checking for name
        """
        self.adewq.text = "sssqqwe"
        self.assertEqual(self.adewq.text, "sssqqwe")

    def test_with_somtaahing(self):
        """
        Test for validations
        """
        self.assertTrue(hasattr(self.adewq, "text"))
        self.assertTrue(hasattr(self.adewq, "id"))
        self.assertTrue(hasattr(self.adewq, "created_at"))
        self.assertTrue(hasattr(self.adewq, "updated_at"))
        self.assertTrue(hasattr(self.adewq, "place_id"))
        self.assertTrue(hasattr(self.adewq, "user_id"))

    def test_for_id(self):
        """
        Test validte uuid
        """
        self.assertIsInstance(uuid.UUID(self.adewq.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
