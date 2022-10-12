import unittest
from unittest.mock import patch
from persona import *

class Test_backend(unittest.TestCase):

    @patch("builtins.input", side_effect=["Matias", "Boldrini", "44438082"])
    def testCase_add_user(self, mock_inputs):
        database = Persona()
        result = database.add_Users()
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["Matias", "Boldrini", "44438082"])
    def testCase_add_user_repeated(self, mock_inputs):
        database = Persona()
        result = database.add_Users()
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["", "Boldrini", "44438082"])
    def testCase_add_user_empty_name(self, mock_inputs):
        database = Persona()
        with self.assertRaises(Exception, msg="INCORRECT DATA"):
            database.check_input()

    @patch("builtins.input", side_effect=["Matias", "Boldrini", "hola"])
    def testCase_add_user_wrong_dni(self, mock_inputs):
        database = Persona()
        with self.assertRaises(Exception, msg="INCORRECT DATA"):
            database.check_input()

    @patch("builtins.input", side_effect=["Linus", "Torvalds"])
    def testCase_modify_user_dni(self, mock_inputs):
        database = Persona()
        result = database.modify_Users("44438082")
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["Matias", "Boldrini"])
    def testCase_modify_user_wrong_dni(self, mock_inputs):
        database = Persona()
        result = database.modify_Users("44438083")
        self.assertFalse(result)

    def testCase_search_user_dni(self):
        database = Persona()
        result = database.get_User_Attributes('44438082')
        self.assertEqual(result, ['44438082', 'Linus', 'Torvalds'])

    @patch("builtins.input", side_effect=["Matias", "Boldrini", "324"])
    def testCase_check_input_True(self, mock_inputs):
        database = Persona()
        self.assertTrue(database.check_input)

    @patch("builtins.input", side_effect=["Linus", "", "hola"])
    def testCase_check_input_Exception(self, mock_inputs):
        database = Persona()
        with self.assertRaises(Exception, msg="INCORRECT DATA"):
            database.check_input()

    def testCase_search_user_wrong_dni(self):
        database = Persona()
        result = database.get_User_Attributes("44438083")
        self.assertIsNone(result)

    def testCase_delete_user_not_exist(self):
        database = Persona()
        result = database.delete_Users("44438083")
        self.assertFalse(result)

    def testCase_zdelete_user(self):
        # Los tests se ejecutan en order alfabetico.
        # si uso delete solo, elimina el user antes de modificarlo
        database = Persona()
        result = database.delete_Users("44438082")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
