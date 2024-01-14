#!/usr/bin/python3
"""
Unit tests for all functions in this class FileStorage.
"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the for the class 
    """
    def test_FileStorage_init(self):
        """
        Test the starting
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all(self):
        """
        Test all function that get all objs
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_file(self):
        """
        Test type of the file
        """
        self.assertEqual(str, type(FileStorage()._FileStorage__file_path))

    def test_noa_elmsaha(self):
        """
        Test the type of the storage
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_newwing(self):
        """
        Test in the new method
        """
        assas = BaseModel()
        models.storage.new(assas)
        self.assertIn("BaseModel." + assas.id, models.storage.all().keys())
        self.assertIn(assas, models.storage.all().values())

    def test_adding(self):
        """
        Test adding
        """
        shya = BaseModel()
        models.storage.new(shya)
        self.assertIn(shya, models.storage.all().values())

    def test_with_many(self):
        """
        Test with many
        """
        shyui1 = BaseModel()
        shyui2 = BaseModel()
        models.storage.new(shyui1)
        models.storage.new(shyui2)
        self.assertIn(shyui1, models.storage.all().values())
        self.assertIn(shyui2, models.storage.all().values())

    def test_saving(self):
        """
        Test the saveing method
        """
        aswq = BaseModel()
        models.storage.new(aswq)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + aswq.id, save_text)
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """
        Test reload function
        """
        aswq = BaseModel()
        models.storage.new(aswq)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage()._FileStorage__objects
        self.assertIn("BaseModel." + aswq.id, objs)
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
