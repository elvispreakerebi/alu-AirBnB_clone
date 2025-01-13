#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class."""

from models import storage
from models.base_model import BaseModel

# Reload existing objects from the file
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)

# Create a new object and save it
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
