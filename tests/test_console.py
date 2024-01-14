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


if __name__ == "__main__":
    unittest.main()
