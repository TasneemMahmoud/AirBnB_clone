#!/usr/bin/python3
"""File_storage file that handle storage
"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Create new obj
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Save new object
        """
        kol_ashya = FileStorage.__objects
        kmskolggt = {}

        for object in kol_ashya.keys():
            kmskolggt[object] = kol_ashya[object].to_dict()

        mwgdaflq = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    mwgdaflq = json.load(f)
                except Exception:
                    pass

        mwgdaflq.update(kmskolggt)

        with open(FileStorage.__file_path, "w") as f:
            json.dump(mwgdaflq, f)

    def reload(self):
        """Get all objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    hlwawyds = json.loads(f.read())
                    for key, value in hlwawyds.items():
                        class_name, obj_id = key.split('.')
                        ahtty = eval(class_name)
                        syha = ahtty(**value)
                        FileStorage.__objects[key] = syha
                except Exception:
                    pass
