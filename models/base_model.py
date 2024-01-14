#!/usr/bin/python3
"""
Module: base_model.py
This is the "base model" module.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel the main class that has same attrs

    """
    def __init__(self, *args, **kwargs):
        """Starting the instance
        """

        asm_dtesa = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, asm_dtesa)
                setattr(self, key, value)

    def save(self):
        """
        Modify attr on this obj
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Function return all
        """
        twel_awes = self.__dict__.copy()
        twel_awes['__class__'] = self.__class__.__name__
        twel_awes['created_at'] = self.created_at.isoformat()
        twel_awes['updated_at'] = self.updated_at.isoformat()
        return twel_awes

    def __str__(self):
        """
        Returns simple line with desc as a string
        """
        return f"[{type(self).__name__}] ({self.id}) {str(self.__dict__)}"
