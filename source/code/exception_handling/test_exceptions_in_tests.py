import src.exceptions
import unittest


class TestExceptions(unittest.TestCase):

    def test_catching_module_not_found_error(self):
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

    def test_catching_name_error(self):
        with self.assertRaises(NameError):
            does_not_exist

    def test_catching_attribute_error(self):
        with self.assertRaises(AttributeError):
            src.exceptions.does_not_exist

    def test_catching_type_error(self):
        with self.assertRaises(TypeError):
            src.exceptions.function_name('the input')

    def test_catching_index_error(self):
        a_string = 'a string'
        a_string[0]
        a_string[7]
        a_string[-1]
        a_string[-8]

        with self.assertRaises(IndexError):
            a_string[8]
        with self.assertRaises(IndexError):
            a_string[-9]

        a_tuple = (0, 1, 2, 'n')
        a_tuple[1]
        a_tuple[-2]

        with self.assertRaises(IndexError):
            a_tuple[100]
        with self.assertRaises(IndexError):
            a_tuple[-100]

    def test_catching_key_error(self):
        a_dictionary = {'key': 'value'}
        a_dictionary['key']

        with self.assertRaises(KeyError):
            a_dictionary['not_in_dictionary']

    def test_catching_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            raise Exception


# Exceptions seen
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError