#!/usr/bin/python3
"""HBNBCommand class
    command interpreter for data creation and validation
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class
        Command interpreter class for AirBnB clone
    """
    def __init__(self):
        """Initialize instance variables"""
        super().__init__()
        self.prompt = "(hbnb) "

    def emptyline(self):
        """Overrides emptyline so as to do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command exits the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handles End-Of-File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
