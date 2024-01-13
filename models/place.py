#!/usr/bin/python3
"""Place class definition."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The id of the city where the place is located.
        user_id (str): The id of the User.
        name (str): The name of the place.
        description (str): A detailed description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The nightly rental price of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of ids for amenities available in the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by+night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
