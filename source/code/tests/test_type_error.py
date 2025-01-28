import unittest
import src.type_error


class TestTypeError(unittest.TestCase):

    def test_type_error_w_non_callables(self):
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()
        src.type_error.a_list()
        src.type_error.a_dictionary()

    def test_type_error_w_function_signatures(self):
        src.type_error.function_00(1)
        src.type_error.function_01(1, 2)
        src.type_error.function_02(1, 2, 3)
        src.type_error.function_03(1, 2, 3, 'n')



# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError