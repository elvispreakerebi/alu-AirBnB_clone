#!/usr/bin/python3
"""
This module contains unit tests for the User class."""

from models import storage
from models.user import User

# Reload all objects
print("-- Reloaded objects --")
for obj_id, obj in storage.all().items():
    print(obj)

# Create new User
print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
