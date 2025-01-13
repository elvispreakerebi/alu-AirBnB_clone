#!/usr/bin/python3
"""
This module defines the command interpreter for the HBNB project."""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if not instance:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        result = []
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, instance in storage.all().items():
                if not arg or key.startswith(arg):
                    result.append(str(instance))
            print(result)

    def do_update(self, arg):
        """
        Updates an instance based on class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if not instance:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if attr_name not in ["id", "created_at", "updated_at"]:
                    try:
                        # Cast attribute value to appropriate type
                        if '.' in attr_value:
                            attr_value = float(attr_value)
                        else:
                            attr_value = int(attr_value)
                    except ValueError:
                        pass
                    setattr(instance, attr_name, attr_value)
                    instance.save()

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
