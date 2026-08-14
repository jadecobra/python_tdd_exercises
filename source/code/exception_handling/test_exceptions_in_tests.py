import src.exceptions
import unittest


class TestExceptions(unittest.TestCase):

    @staticmethod
    def assert_raises(code, exception):
        try:
            exec(code)
        except exception:
            pass
        else:
            raise AssertionError

    def test_catching_module_not_found_error(self):
        self.assert_raises(
            'import does_not_exist', ModuleNotFoundError
        )
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

    def test_catching_name_error(self):
        self.assert_raises('not_defined', NameError)
        with self.assertRaises(NameError):
            not_defined

    def test_catching_attribute_error(self):
        self.assert_raises(
            'src.exceptions.does_not_exist', AttributeError
        )
        with self.assertRaises(AttributeError):
            src.exceptions.does_not_exist

    def test_catching_type_error(self):
        self.assert_raises(
            "src.exceptions.function_name('the input')",
            TypeError
        )
        with self.assertRaises(TypeError):
            src.exceptions.function_name('the input')

    def test_catching_index_error(self):
        self.assert_raises("'a string'[8]", IndexError)
        self.assert_raises("'a string'[-9]", IndexError)

        with self.assertRaises(IndexError):
            'a string'[8]
        with self.assertRaises(IndexError):
            'a string'[-9]

        self.assert_raises(
            "(0, 1, 2, 'n')[100]", IndexError
        )
        self.assert_raises(
            "(0, 1, 2, 'n')[-100]", IndexError
        )

        with self.assertRaises(IndexError):
            (0, 1, 2, 'n')[100]
        with self.assertRaises(IndexError):
            (0, 1, 2, 'n')[-100]

    def test_catching_key_error(self):
        self.assert_raises(
            "{'key': 'value'}['not_in_dictionary']",
            KeyError
        )
        with self.assertRaises(KeyError):
            {'key': 'value'}['not_in_dictionary']

    def test_catching_zero_division_error(self):
        self.assert_raises('1 / 0', ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_catching_exceptions(self):
        self.assert_raises('raise Exception', Exception)
        with self.assertRaises(Exception):
            raise Exception


# Exceptions seen
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError
# SyntaxError
# IndexError
# KeyError
# ZeroDivisionError