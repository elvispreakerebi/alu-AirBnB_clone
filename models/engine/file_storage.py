"""
This module contains the FileStorage class."""

import json
from os.path import exists

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)."""
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        from models.base_model import BaseModel  # Import here to avoid circular import
                        self.__objects[key] = BaseModel(**value)
