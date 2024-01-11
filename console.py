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

    def default(self, args):
        """molas

        Args:
            line (str): _description_

        Returns:
            _type_: _description_
        """
        commands = args.split('.')
        n_of_c = commands[0]

        method = commands[1].split('(')
        method_name = method[0]

        mota = method[1].split(')')[0]
        masf_motas= mota.split(',')

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            'count': self.do_count,
        }


        if method_name in method_dict.keys():
            if method_name == "update":
                mota_id = masf_motas[0]
                update_key = masf_motas[1]
                update_value = masf_motas[2]
                return method_dict[method_name]("{} {} {} {}".format(n_of_c,
                                                                 mota_id,
                                                                 update_key,
                                                                 update_value))
            else:
                return method_dict[method_name](f"{n_of_c} {mota}")

        print(f"*** Unknown syntax: {args}")
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

    def do_count(self, params):
        """molas

        params:
            arg (_type_): _description_
        """
        command_params = shlex.split(params)
        if len(command_params) == 0:
            print("** class name missing **")
        elif command_params[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            all_instances = storage.all()
            num_count = 0
            for key, value in all_instances.items():
                if key.split('.')[0] == command_params[0]:
                    num_count += 1
            print(num_count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
