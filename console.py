#!/usr/bin/python3
"""HBNBCommand class
    command interpreter for data creation and validation
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User


class_list = {'BaseModel': BaseModel, 'User': User}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class
        Command interpreter class for AirBnB clone
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the console"""
        return True

    def do_EOF(self, arg):
        """Handles End of file/ Exits the console"""
        print()
        return True

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

    def do_destroy(self, arg):
        """Deletes instance based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arguments = arg.split()
            if len(arguments) != 2:
                print("** instance id missing **")
            elif arguments[0] not in class_list:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if arguments[1] == value.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, arg):
        """Prints a List of all objects"""
        list_all = []
        if arg:
            arguments = arg.split()
            if argument[0] not in class_list:
                print("** class doesn't exist **")
        for key, value in storage.all().items():
            list_all.append(str(value))
        print(list_all)

    def do_update(self, arg):
        """Udates an instance based on class and id"""
        words = arg.split()
        if len(words) == 0:
            print("** class name missing **")
            return False
        if words[0] in class_list:
            if len(words) > 1:
                key = words[0] + '.' + words[1]
                if key in storage.all():
                    if len(words) > 2:
                        if len(words) > 3:
                            setattr(storage.all()[key], words[2], words[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
