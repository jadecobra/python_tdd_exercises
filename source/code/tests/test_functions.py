import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions_w_pass(self):
        self.assertIsNone(src.functions.function_w_pass())

    def test_functions_w_return(self):
        self.assertIsNone(src.functions.function_w_return())

    def test_functions_w_return_none(self):
        self.assertIsNone(src.functions.function_w_return_none())

    def test_singleton_functions(self):
        self.assertEqual(src.functions.singleton(), 'my_first_name')

    def test_singleton_functions_w_inputs(self):
        self.assertEqual(
            src.functions.singleton_w_inputs('Bob', 'James', 'Frank'),
            'joe'
        )
        self.assertEqual(
            src.functions.singleton_w_inputs('a', 1, 'c', 3),
            'joe'
        )

    def test_passthrough_functions(self):
        self.assertEqual(src.functions.passthrough(False), False)
        self.assertEqual(src.functions.passthrough(True), True)
        self.assertEqual(src.functions.passthrough(None), None)
        self.assertEqual(src.functions.passthrough(int), int)
        self.assertEqual(src.functions.passthrough(float), float)
        self.assertEqual(src.functions.passthrough(str), str)
        self.assertEqual(src.functions.passthrough(tuple), tuple)
        self.assertEqual(src.functions.passthrough(list), list)
        self.assertEqual(src.functions.passthrough(set), set)
        self.assertEqual(src.functions.passthrough(dict), dict)


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError