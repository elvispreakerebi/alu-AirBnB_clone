#!/usr/bin/python3
"""
This module defines the Place class that inherits from BaseModel."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    city_id = ""  # Will hold the ID of a City object
    user_id = ""  # Will hold the ID of a User object
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Will hold a list of Amenity IDs
