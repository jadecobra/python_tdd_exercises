import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_make_a_function_w_pass(self):
        self.assertIsNone(src.functions.function_w_pass())

    def test_make_a_function_w_return(self):
        self.assertIsNone(src.functions.function_w_return())

    def test_make_a_function_w_return_none(self):
        self.assertIsNone(src.functions.function_w_return_none())

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(),
            'the same thing'
        )

    def test_constant_functions_w_inputs(self):
        self.assertEqual(
            src.functions.constant_w_inputs('Bob', 'James'),
            'the same thing'
        )
        self.assertEqual(
            src.functions.constant_w_inputs('a', 1, 'c', 3),
            'the same thing'
        )

    def test_passthrough_functions(self):
        self.assertIsNone(src.functions.passthrough(None))
        self.assertEqual(src.functions.passthrough(object), object)



# Exceptions Encountered
# AssertionError
# NameError
# AttributeError