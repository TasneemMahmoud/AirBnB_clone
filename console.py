#!/usr/bin/python3
"""
"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    existing_class = ["BaseModel", "Place", "Review", "User",
                       "City", "State", "Amenity"]

    def emptyline(self):
        """
        Just pass, Do nothing
        """
        pass

    def default(self, params):
        """_summary_

        params:
            args: _description_

        Returns:
            type: _description_
        """
        all_params = params.split('.')
        name_of_class = all_params[0]

        method = all_params[1].split('(')
        method_name = method[0]

        methods_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            # 'count': self.do_count,
        }


        if method_name in methods_dict.keys():
            return methods_dict[method_name](f"{name_of_class} {''}")


        print(f"*** Unknown syntax: {params}")
        return False


    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def do_quit(self, arg):
        """
        """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit to exit")
    
    def do_create(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)
        
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            try:
                new_created_obj = eval(f"{command_args[0]}()")
            except Exception:
                pass
            
            storage.save()
            print(new_created_obj.id)

    def do_show(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)
        
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)
        
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        all_objects = storage.all()
        command_args = shlex.split(args)

        if len(command_args) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split('.')[0] == command_args[0]:
                    print(str(value))

    def do_update(self, args):
        """
        """        
        command_args = shlex.split(args)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key not in all_objects:
                print("** no instance found **")
            elif len(command_args) < 3:
                print("** attribute name missing **")
            elif len(command_args) < 4:
                print("** value missing **")
            else:
                updated_obj = all_objects[key]
                attr_key = command_args[2]
                attr_value = command_args[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(updated_obj, attr_key, attr_value)
                updated_obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
