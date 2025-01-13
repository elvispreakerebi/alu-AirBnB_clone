#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""
    prompt = "(hbnb) "  # Custom prompt for the command interpreter

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        print()  # Print a newline for a clean exit
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
