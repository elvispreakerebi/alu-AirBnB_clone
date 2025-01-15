#!/usr/bin/python3
"""
This module defines the Review class that inherits from BaseModel."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""  # Will hold the ID of a Place object
    user_id = ""  # Will hold the ID of a User object
    text = ""
