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
        src.type_error.function_00('a')
        src.type_error.function_01('a', 'b')
        src.type_error.function_02('a', 'b', 'c')
        src.type_error.function_03('a', 'b', 'c', 'd')

    def test_type_error_w_objects_that_do_not_mix(self):
        with self.assertRaises(TypeError):
            None + 1
        with self.assertRaises(TypeError):
            'text' + 0.1
        with self.assertRaises(TypeError):
            (1, 2, 3, 'n') - {1, 2, 3, 'n'}


# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError