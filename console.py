#!/usr/bin/python3
"""HBNBCommand class
    command interpreter for data creation and validation
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel


class_list = {'BaseModel': BaseModel}


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

    def do_create(self, arg):
        """Crestes an instance of a class, saves and print id"""
        try:
            if not arg:
                raise ValueError("** class name missing **")
            if arg not in class_list:
                raise TypeError("** class doesn't exist **")
            my_object = eval(arg)()
            my_object.save()
            print(my_object.id)

        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints a string representation of an nstance"""
        try:
            if not arg:
                raise ValueError("** class name missing **")
            else:
                arguments = arg.split()
                if len(arguments) != 2:
                    raise ValueError("** instance id missing **")
                elif arguments[0] not in class_list:
                    raise ValueError("** class doesn't exist **")
                else:
                    for key, value in storage.all().items():
                        if arguments[1] == value.id:
                            print(value)
                            return
                    raise TypeError("** no instance found **")

        except Exception as e:
            print(e)

    def do_quit(self, arg):
        """Quit command exits the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handles End-Of-File"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
