import unittest
import src.type_error


class TestTypeError(unittest.TestCase):

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00()
        src.type_error.function_01('a')
        src.type_error.function_02('a', 'b')
        src.type_error.function_03('a', 'b', 'c')


# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError