#!/usr/bin/python3
"""
TestConsoleClass
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test cases for console.py
    """
    def test_destroing(self):
        """
        checking deleteing method
        """
        command = 'create User'
        mfrtl = '** no instance found **'

        with patch('sys.stdout', new=StringIO()) as m4haia:
            HBNBCommand().onecmd(command)

        command = 'destroy User 123'

        with patch('sys.stdout', new=StringIO()) as m4haia:
            HBNBCommand().onecmd(command)
            mkrg = m4haia.getvalue().strip()

        self.assertEqual(mkrg, mfrtl)

    def test_showing(self):
        """
        Getting the obj testing
        """
        command = 'show'
        mfrtl = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as m4haia:
            HBNBCommand().onecmd(command)
            mkrg = m4haia.getvalue().strip()

        self.assertEqual(mkrg, mfrtl)

    def test_create_unexist_cls(self):
        """
        Test create for invalid class name
        """
        command = 'create InvalidClass'
        mfrtl = '** class doesn\'t exist **'

        with patch('sys.stdout', new=StringIO()) as m4haia:
            HBNBCommand().onecmd(command)
            mkrg = m4haia.getvalue().strip()

        self.assertEqual(mkrg, mfrtl)

    def test_without_class(self):
        """
        Test create command with no class name
        """
        command = 'create'
        mfrtl = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as m4haia:
            HBNBCommand().onecmd(command)
            mkrg = m4haia.getvalue().strip()

        self.assertEqual(mkrg, mfrtl)

    def test_hgat(self):
        """
        test ayhaga testing
        """
        with patch("sys.stdout", new=StringIO()) as moragats:
            mwsqon = "create"
            motwka = "** class name missing **"
            HBNBCommand().onecmd(mwsqon)
            self.assertEqual(motwka, moragats.getvalue().strip())


    def test_amr_fadi(self):
        """ Test stoor fadyaa """
        with patch("sys.stdout", new=StringIO()) as moragats:
            self.assertEqual("", moragats.getvalue())


    def test_mshkl(self):
        """ test wrong unique id """
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as moragats:
            mwsqon = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(mwsqon)
            res = "** no instance found **"
            self.assertEqual(moragats.getvalue().strip(), res)

        """ test passing no class """
        with patch("sys.stdout", new=StringIO()) as moragats:
            mwsqon = 'show'
            HBNBCommand().onecmd(mwsqon)
            res = "** class name missing **"
            self.assertEqual(moragats.getvalue().strip(), res)

        """ test with unknowen classs"""
        with patch("sys.stdout", new=StringIO()) as moragats:
            mwsqon = 'places.show("232342")'
            HBNBCommand().onecmd(mwsqon)
            res = "** class doesn't exist **"
            self.assertEqual(moragats.getvalue().strip(), res)

        """ test without an id """
        with patch("sys.stdout", new=StringIO()) as moragats:
            mwsqon = 'Place.show()'
            HBNBCommand().onecmd(mwsqon)
            res = "** instance id missing **"
            self.assertEqual(moragats.getvalue().strip(), res)


if __name__ == "__main__":
    unittest.main()
