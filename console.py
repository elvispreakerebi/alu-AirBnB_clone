"""
Console module for command-line interaction with the storage system.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage  # Assuming `models` module initializes `FileStorage`

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the system."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Ignore empty lines."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel or User."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        if class_name == "BaseModel":
            new_instance = BaseModel()
        elif class_name == "User":
            new_instance = User()
        else:
            print("** class doesn't exist **")
            return
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance of a class by ID."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        obj_dict = storage.all()
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance of a class by ID."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        obj_dict = storage.all()
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Show all instances of a class or all instances if no class is specified."""
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
            return
        class_name = arg.strip()
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in obj_dict.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """Update an instance of a class by ID."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        obj = obj_dict[key]
        try:
            # Convert value to int or float if applicable
            if "." in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass  # Leave value as a string if conversion fails
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
