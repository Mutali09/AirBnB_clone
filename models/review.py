#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represent a review.

    Attributes:
        place_id (str): The id of the place associated with the review.
        user_id (str): The id of the user who created the review.
        text (str): The textual content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
