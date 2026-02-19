import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_why_use_a_function(self):
        def add_x(x=3, y=0):
            return x + y

        self.assertEqual(add_x(y=0), 3)
        self.assertEqual(add_x(y=1), 4)
        self.assertEqual(add_x(y=2), 5)
        self.assertEqual(add_x(y=3), 6)
        self.assertEqual(add_x(y=4), 7)
        self.assertEqual(add_x(y=5), 8)
        self.assertEqual(add_x(y=6), 9)
        self.assertEqual(add_x(y=7), 10)
        self.assertEqual(add_x(y=8), 11)
        self.assertEqual(add_x(y=9), 12)

    def test_making_a_function_w_pass(self):
        self.assertIsNone(src.functions.w_pass())

    def test_making_a_function_w_return(self):
        self.assertIsNone(src.functions.w_return())

    def test_making_a_function_w_return_none(self):
        self.assertIsNone(src.functions.w_return_none())

    def test_what_happens_after_a_function_returns(self):
        self.assertIsNone(src.functions.return_is_last())

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
            src.functions.w_positional_arguments('first', 'last'),
            ('first', 'last')
        )
        self.assertEqual(
            src.functions.w_positional_arguments('last', 'first'),
            ('last', 'first')
        )

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_keyword_arguments(
                first_input='first', last_input='last',
            ),
            ('first', 'last')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments(
                last_input='last', first_input='first',
            ),
            ('first', 'last')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments('last', 'first'),
            ('last', 'first')
        )

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_positional_and_keyword_arguments(
                'first', last_input='last',
            ),
            ('first', 'last')
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


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError