#!/usr/bin/python3
"""
Test casses for state
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test for evry cas
    """
    def setUp(self):
        """
        This start at first if every test
        """
        self.wlya = State()

    def test_creating_one(self):
        """
        Test first creating
        """
        self.assertIsInstance(self.wlya, BaseModel)

    def test_creating_again(self):
        """
        Test for creating too
        """
        self.assertIsInstance(self.wlya, State)

    def test_edit_asm(self):
        """
        Test editing the attr
        """
        self.wlya.name = "KSA"
        self.assertEqual(self.wlya.name, "KSA")

    def test_with_some(self):
        """
        Test checkin for any wrong
        """
        self.assertTrue(hasattr(self.wlya, "name"))
        self.assertTrue(hasattr(self.wlya, "id"))
        self.assertTrue(hasattr(self.wlya, "created_at"))
        self.assertTrue(hasattr(self.wlya, "updated_at"))

    def test_for_id(self):
        """
        Test valide uuid with id
        """
        self.assertIsInstance(uuid.UUID(self.wlya.id), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
