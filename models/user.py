#!/usr/bin/python3
"""
Module: user.py
This is the user model class.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User extend from base model

    Attributes:
        email: string - an string empty
        password: string - an string empty
        first_name: string - an string empty
        last_name: string - an string empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
