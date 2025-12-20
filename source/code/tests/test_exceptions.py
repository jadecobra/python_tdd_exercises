import src.exceptions
import unittest


class TestExceptions(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

    def test_catching_name_error_in_tests(self):
        with self.assertRaises(NameError):
            does_not_exist

    def test_catching_attribute_error_in_tests(self):
        with self.assertRaises(AttributeError):
            src.exceptions.does_not_exist

    def test_catching_type_error_in_tests(self):
        with self.assertRaises(TypeError):
            src.exceptions.function_name('the input')

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {'key': 'value'}['does_not_exist']

    def test_catching_zero_division_error_in_tests(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_catching_exceptions_in_tests(self):
        with self.assertRaises(Exception):
            raise Exception

    def test_catching_exceptions_w_messages(self):
        with self.assertRaisesRegex(
            Exception, 'BOOM!'
        ):
            src.exceptions.raise_exception()

    def test_catching_failure(self):
        self.assertEqual(
            src.exceptions.an_exception_handler(
                src.exceptions.raise_exception
            ),
            'failed'
        )

    def test_catching_success(self):
        self.assertEqual(
            src.exceptions.an_exception_handler(
                src.exceptions.does_not_raise_exception
            ),
            'succeeded'
        )


# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError