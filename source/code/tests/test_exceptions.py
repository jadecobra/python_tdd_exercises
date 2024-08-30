import exceptions
import module
import unittest


class TestExceptions(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module

    def test_catching_attribute_error_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
        with self.assertRaises(AttributeError):
            module.non_existent_function()
        with self.assertRaises(AttributeError):
            module.NonExistentClass()

    def test_catching_type_error_in_tests(self):
        with self.assertRaises(TypeError):
            module.function("arg1", "arg2", "arg3", "arg4")

    def test_catching_index_error_in_tests(self):
        with self.assertRaises(IndexError):
            [1, 2, 3, 4][5]

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {"key": "value"}["non_existent_key"]

    def test_catching_zero_division_error_in_tests(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

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