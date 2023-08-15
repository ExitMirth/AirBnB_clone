#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
        expected_output = (
            "Prints string representation of an instance based "
            "on the class name and id\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
