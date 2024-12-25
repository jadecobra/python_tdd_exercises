import unittest
import src.type_error


class TestTypeError(unittest.TestCase):

    def test_type_error_w_callables(self):
        src.type_error.none()
        src.type_error.true()
        src.type_error.false()

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')
        src.type_error.function_03('a', 'b', 'c', 'd')


# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError