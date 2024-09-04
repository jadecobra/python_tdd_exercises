import src.exceptions
import unittest


class TestExceptions(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import module_that_does_not_exist

    def test_catching_name_error_in_tests(self):
        with self.assertRaises(NameError):
            exceptions

    def test_catching_attribute_error_in_tests(self):
        with self.assertRaises(AttributeError):
            src.exceptions.attribute_that_does_not_exist
        with self.assertRaises(AttributeError):
            src.exceptions.function_that_does_not_exist()
        with self.assertRaises(AttributeError):
            src.exceptions.ClassThatDoesNotExist()

    def test_catching_type_error_in_tests(self):
        with self.assertRaises(TypeError):
            src.exceptions.function('argument')

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {'key': 'value'}['key_that_does_not_exist']

    def test_catching_zero_division_error_in_tests(self):
        with self.assertRaises(ZeroDivisionError):
            0 / 0

    def test_catching_exceptions_in_tests(self):
        with self.assertRaises(Exception):
            raise Exception


# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError