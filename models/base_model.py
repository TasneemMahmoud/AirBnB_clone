#!/usr/bin/python3
"""
Module: base_model.py
This is the "base model" module.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel is the parent for other classes

    Attributes:
      id(str): the unique id of the object(user)
      created_at: created at time
      updated_at: update at time

    Methods:
      __str__: return string
      save(self): change updated_at atr
      to_dict(self): returns the keys and values of the dict

    """
    def __init__(self, *args, **kwargs):
        """Object init

        Args:
          args: won't used
          kwargs: a existing dictionary

        """

        string_time_formate = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, string_time_formate)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """
        Changing the updated_at prop:
        with new current one
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dict with keys
        and values of the dictionary
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Print a string of the obj
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
