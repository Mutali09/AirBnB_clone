#!/usr/bin/python3
"""This defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is a representation of BaseModel of HBnB project."""

    def __init__(self, *args, **kwargs):
        """New BaseModel Initialization.

        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of the attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
