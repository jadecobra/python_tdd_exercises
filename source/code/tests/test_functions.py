import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_make_a_function_w_pass(self):
        self.assertIsNone(src.functions.w_pass())

    def test_make_a_function_w_return(self):
        self.assertIsNone(src.functions.w_return())

    def test_make_a_function_w_return_none(self):
        self.assertIsNone(src.functions.w_return_none())

    def test_constant_functions(self):
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

    def test_functions_w_unknown_positional_arguments(self):
        self.assertEqual(
            src.functions.w_unknown_positional_arguments(0, 1, 2, 3),
            (0, 1, 2, 3)
        )
        self.assertEqual(
            src.functions.w_unknown_positional_arguments(
                None, bool, int, float, str, tuple, list, set, dict
            ),
            (None, bool, int, float, str, tuple, list, set, dict)
        )

    def test_functions_w_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_keyword_arguments(x='first', y='second'),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments(y='second', x='first'),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_keyword_arguments('second', 'first'),
            ('second', 'first')
        )

    def test_functions_w_unknown_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_unknown_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        )
        self.assertEqual(
            src.functions.w_unknown_keyword_arguments(
                none=None, a_boolean=bool, an_integer=int,
                a_float=float, a_string=str, a_tuple=tuple,
                a_list=list, a_set=set, a_dictionary=dict,
            ),
            dict(
                a_boolean=bool, a_dictionary=dict, a_float=float,
                a_list=list, a_set=set, a_string=str, a_tuple=tuple,
                an_integer=int, none=None,
            )
        )

    def test_functions_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_positional_and_keyword_arguments(
                'first', y='second'
            ),
            ('first', 'second')
        )
        self.assertEqual(
            src.functions.w_positional_and_keyword_arguments('first_name'),
            ('first_name', 'Doe')
        )
        self.assertEqual(
            src.functions.w_positional_and_keyword_arguments(
                'second', 'first'
            ),
            ('second', 'first')
        )

    def test_functions_unknown_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.w_unknown_positional_and_keyword_arguments(
                None, bool, int, float, str, tuple, list, set, dict,
                none=None, a_boolean=bool, an_integer=int,
                a_float=float, a_string=str, a_tuple=tuple,
                a_list=list, a_set=set, a_dictionary=dict,
            ),
            (
                (
                    None, bool, int, float, str, tuple, list,
                    set, dict
                ),
                {
                    'a_boolean': bool, 'a_dictionary': dict,
                    'a_float': float, 'a_list': list, 'a_set': set,
                    'a_string': str, 'a_tuple': tuple,
                    'an_integer': int, 'none': None
                }
            )
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# SyntaxError