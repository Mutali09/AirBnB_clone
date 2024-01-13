#!/usr/bin/python3
"""Amenity class definition."""
from models.base_model impoort BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
