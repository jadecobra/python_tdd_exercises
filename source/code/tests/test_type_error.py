import unittest
import src.type_error


class TestTypeError(unittest.TestCase):

    def test_type_error_w_function_signatures(self):
        src.type_error.function_a('a')
        src.type_error.function_b('a', 'b')
        src.type_error.function_c('a', 'b', 'c')
        src.type_error.function_d('a', 'b', 'c', 'd')



# Exceptions Encountered
# AssertionError
# AttributeError
# TypeError