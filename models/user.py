#!/usr/bin/python3
"""User class definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """This represents a User.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    pasword = ""
    first_name = ""
    last_name = ""
