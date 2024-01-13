#!/usr/bin/python3
import os
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""File storage handler

Returns:
    object: file storage objects
"""


class FileStorage:
    """File storage class handle orations

    Returns:
        dict: objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all objects

        Returns:
            Obj: FileStorage objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (dict): coming from base model
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """_summary_
        """
        all_inst = FileStorage.__objects
        inst_dict = {}

        for inst in all_inst.keys():
            inst_dict[inst] = all_inst[inst].to_dict()

        file_exist_objects = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    file_exist_objects = json.load(file)
                except Exception:
                    pass

        file_exist_objects.update(inst_dict)

        with open(FileStorage.__file_path, "w") as file:
            json.dump(file_exist_objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    file_dict = json.loads(file.read())
                    for key, value in file_dict.items():
                        model_name, obj_id = key.split('.')
                        temp = eval(model_name)
                        obj = temp(**value)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
