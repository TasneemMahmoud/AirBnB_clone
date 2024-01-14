#!/usr/bin/python3
"""
"""
import cmd
import shlex
import re
import ast
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def asm_kmos(param):
    """Splitting
    """
    kms_ks = re.search(r"\{(.*?)\}", param)
    if kms_ks:
        t_ids = shlex.split(param[:kms_ks.span()[0]])
        id = [i.strip(",") for i in t_ids][0]
        str_dict = kms_ks.group(1)
        try:
            kns_p = ast.literal_eval("{" + str_dict + "}")
        except Exception:
            print(f"*** Unknown syntax: {kns_p}")
            return
        return id, kns_p
    else:
        cmd_args = param.split(",")
        try:
            elid = cmd_args[0]
            elkey = cmd_args[1]
            elvalue = cmd_args[2]
            return f"{elid}", f"{elkey} {elvalue}"
        except Exception:
            print(f"*** Unknown syntax: {kns_p}")


class HBNBCommand(cmd.Cmd):
    """Class that extend from cmd
    """
    prompt = "(hbnb) "
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Enter a new line
        """
        if not sys.stdin.isatty():
            print()

    def do_EOF(self, arg):
        """EOF to kill the process
        """
        if not sys.stdin.isatty():
            print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        if not sys.stdin.isatty():
            print()

        return True

    def do_help(self, arg):
        """Help cmd
        """
        if not sys.stdin.isatty():
            print()
        cmd.Cmd.do_help(self, arg)

    def do_create(self, args):
        """Create command
        """
        amr_hgt = shlex.split(args)

        if len(amr_hgt) == 0:
            print("** class name missing **")
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            try:
                created_instance = eval(f"{amr_hgt[0]}()")
            except Exception:
                pass

            storage.save()
            print(created_instance.id)

    def do_show(self, args):
        """Show single instance 
        """
        amr_hgt = shlex.split(args)

        if len(amr_hgt) == 0:
            print("** class name missing **")
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(amr_hgt) < 2:
            print("** instance id missing **")
        else:
            kol_hgj = storage.all()
            key = "{}.{}".format(amr_hgt[0], amr_hgt[1])

            if key in kol_hgj:
                print(kol_hgj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Destroy single instance
        """
        amr_hgt = shlex.split(args)

        if len(amr_hgt) == 0:
            print("** class name missing **")
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(amr_hgt) < 2:
            print("** instance id missing **")
        else:
            kol_hgj = storage.all()
            key = "{}.{}".format(amr_hgt[0], amr_hgt[1])

            if key in kol_hgj:
                del kol_hgj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Get all objects
        """
        kol_hgj = storage.all()
        amr_hgt = shlex.split(args)

        if len(amr_hgt) == 0:
            for key, value in kol_hgj.items():
                print(str(value))
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            for key, value in kol_hgj.items():
                if key.split('.')[0] == amr_hgt[0]:
                    print(str(value))

    def do_update(self, args):
        """Update the class object
        """
        amr_hgt = shlex.split(args)
        if len(amr_hgt) == 0:
            print("** class name missing **")
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(amr_hgt) < 2:
            print("** instance id missing **")
        else:
            kol_hgj = storage.all()
            key = "{}.{}".format(amr_hgt[0], amr_hgt[1])

            if key not in kol_hgj:
                print("** no instance found **")
            elif len(amr_hgt) < 3:
                print("** attribute name missing **")
            elif len(amr_hgt) < 4:
                print("** value missing **")
            else:
                hdis_at = kol_hgj[key]

                bass_dict = re.search(r"\{(.*?)\}", args)
                if bass_dict:
                    str_dict = bass_dict.group(1)
                    try:
                        kns_p = ast.literal_eval("{" + str_dict + "}")
                    except Exception:
                        print(f"*** Unknown syntax: {kns_p}")

                    dict_keys = list(kns_p.keys())
                    dict_values = list(kns_p.values())

                    elksw = dict_keys[0]
                    alval = dict_keys[1]
                    kmsama = dict_values[0]
                    jmatna = dict_values[1]

                    setattr(hdis_at, elksw, kmsama)
                    setattr(hdis_at, alval, jmatna)

                else:
                    prrmss = amr_hgt[2]
                    prsvaw = amr_hgt[3]

                    try:
                        prsvaw = eval(prsvaw)
                    except Exception:
                        pass
                    setattr(hdis_at, prrmss, prsvaw)

                hdis_at.save()

    def do_count(self, args):
        """count objects in the class
        """
        amr_hgt = shlex.split(args)
        if len(amr_hgt) == 0:
            print("** class name missing **")
        elif amr_hgt[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            kol_hgj = storage.all()
            count = 0
            for key, value in kol_hgj.items():
                if key.split('.')[0] == amr_hgt[0]:
                    count += 1
            print(count)

    def default(self, args):
        """Edit the default behavior
        """
        hasg = args.split('.')
        asmkls = hasg[0]
        asdlsq = asmkls

        # orty = cmd_fun  just for pycodestyle
        orty = hasg[1].split('(')
        orty_name = orty[0]

        param = orty[1].split(')')[0]

        orty_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            'count': self.do_count,
        }

        if orty_name in orty_dict.keys():
            if orty_name == "update":
                elid, kns_p = asm_kmos(param)
                try:
                    if isinstance(kns_p, str):
                        attrs = kns_p
                        return orty_dict[orty_name](f"{asdlsq} {elid} {attrs}")
                    elif isinstance(kns_p, dict):
                        da = kns_p
                        return orty_dict[orty_name](f"{asdlsq} {elid} {da}")
                except Exception:
                    print(f"*** Unknown syntax: {kns_p}")
            else:
                return orty_dict[orty_name]("{} {}".format(asdlsq, param))

        print(f"*** Unknown syntax: {args}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
