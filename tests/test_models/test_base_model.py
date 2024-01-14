#!/usr/bin/python3
"""
Unit testing for the base_model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Class to test base class
    """

    def test_rshil(self):
        """
        Test the starting
        """
        hgti = BaseModel()
        self.assertIsNotNone(hgti.id)
        self.assertIsNotNone(hgti.created_at)
        self.assertIsNotNone(hgti.updated_at)

    def test_save(self):
        """
        Test saving
        """
        hgti = BaseModel()
        hgti.save()
        self.assertNotEqual(hgti.created_at, hgti.updated_at)

    def test_funtion(self):
        """
        Test the dictionary case
        """
        hgti = BaseModel()
        hgti_dict = hgti.to_dict()

        self.assertIsInstance(hgti_dict, dict)
        created_at_iso = hgti.created_at.isoformat()
        updated_at_iso = hgti.updated_at.isoformat()

        self.assertEqual(hgti_dict["__class__"], "BaseModel")
        self.assertEqual(hgti_dict["id"], hgti.id)
        self.assertEqual(hgti_dict["created_at"], created_at_iso)
        self.assertEqual(hgti_dict["updated_at"], updated_at_iso)

    def test_the_string(self):
        """
        Test the an attr for string
        """
        hgti = BaseModel()

        self.assertTrue(str(hgti).startswith('[BaseModel]'))
        self.assertIn(hgti.id, str(hgti))
        self.assertIn(str(hgti.__dict__), str(hgti))

    def test_kwargs(self):
        """
        Test the starting
        """
        alwol = "2019-07-01T00:00:00.000000"
        iso_format = datetime.fromisoformat(alwol)
        hgti = BaseModel(created_at=alwol, updated_at=alwol)
        self.assertEqual(hgti.created_at, iso_format)
        self.assertEqual(hgti.updated_at, iso_format)
        self.assertNotEqual(hgti.created_at, datetime.utcnow())
        self.assertNotEqual(hgti.updated_at, datetime.utcnow())


if __name__ == "__main__":
    unittest.main()
