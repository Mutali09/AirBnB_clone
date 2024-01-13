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

    def save(self):
        """Update the last modification time, which is updated_at, and save object to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation ofBaseModel instance.

        Includes the key/value pairs for all attributes, with special
        handling for created_at and updated_at attritbutes, which are converted
        to ISO format strings. Includes key/value pair for __class__ representing
        class name of object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the string representation of BaseModel instance.

        Displays the class name, ID, and key/value pairs of
        attributes in a formatted string.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
