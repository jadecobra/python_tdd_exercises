import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_making_a_function_w_pass(self):
        self.assertIsNone(src.functions.w_pass())

    def test_making_a_function_w_return(self):
        self.assertIsNone(src.functions.w_return())

    def test_making_a_function_w_return_none(self):
        self.assertIsNone(src.functions.w_return_none())

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(),
            'the same thing'
        )

    def test_identity_function(self):
        self.assertIsNone(src.functions.identity(None))
        self.assertEqual(src.functions.identity(object), object)

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            src.functions.w_positional_arguments('first', 'second'),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_positional_arguments('second', 'first'),
            ('second', 'first')
        )

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_keyword_arguments(
                first='first', second='second',
            ),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments(
                second='second', first='first',
            ),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments('second', 'first'),
            ('second', 'first')
        )

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_positional_and_keyword_arguments(
                'john', last_name='smith',
            ),
            ('john', 'smith')
        )

    def test_functions_w_default_arguments(self):
        self.assertEqual(
            src.functions.w_default_arguments('jane'),
            ('jane', 'doe')
        )
        self.assertEqual(
            src.functions.w_default_arguments('joe', 'blow'),
            ('joe', 'blow')
        )

    def test_functions_w_unknown_arguments(self):
        self.assertEqual(
            src.functions.w_unknown_arguments(
                0, 1, 2, 3, a=4, b=5, c=6, d=7,
            ),
            ((0, 1, 2, 3), {'a': 4, 'b': 5, 'c': 6, 'd': 7})
        )
        self.assertEqual(
            src.functions.w_unknown_arguments(0, 1, 2, 3),
            ((0, 1, 2, 3), {})
        )
        self.assertEqual(
            src.functions.w_unknown_arguments(a=4, b=5, c=6, d=7),
            ((), dict(a=4, b=5, c=6, d=7))
        )
        self.assertEqual(
            src.functions.w_unknown_arguments(),
            ((), {})
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# IndentationError