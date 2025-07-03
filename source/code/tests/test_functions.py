import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_function_w_pass(self):
        self.assertIsNone(src.functions.function_w_pass())

    def test_function_w_return(self):
        self.assertIsNone(src.functions.function_w_return())

    def test_function_w_return_none(self):
        self.assertIsNone(src.functions.function_w_return_none())

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(),
            'the same thing'
        )

    def test_constant_function_w_inputs(self):
        self.assertEqual(
            src.functions.constant_w_inputs('Bob', 'James'),
            src.functions.constant()
        )
        self.assertEqual(
            src.functions.constant_w_inputs('a', 1, 'c', 3),
            src.functions.constant()
        )

    def test_identity_function(self):
        self.assertIsNone(src.functions.identity(None))
        self.assertEqual(src.functions.identity(object), object)

    def test_functions_w_positional_arguments(self):
        self.assertEqual(
            src.functions.takes_positional_arguments(
                'first_name', 'last_name'
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            src.functions.takes_positional_arguments(
                'last_name', 'first_name'
            ),
            ('last_name', 'first_name')
        )

    def test_function_w_unknown_positional_arguments(self):
        self.assertEqual(
            src.functions.takes_unknown_positional_arguments(
                0, 1, 2, 3
            ),
            (0, 1, 2, 3)
        )
        self.assertEqual(
            src.functions.takes_unknown_positional_arguments(
                None, bool, int, float, str, tuple, list, set, dict
            ),
            (None, bool, int, float, str, tuple, list, set, dict)
        )

    def test_function_w_keyword_arguments(self):
        self.assertEqual(
            src.functions.takes_keyword_arguments(
                first_name='first_name',
                last_name='last_name',
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            src.functions.takes_keyword_arguments(
                last_name='last_name',
                first_name='first_name',
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            src.functions.takes_keyword_arguments(
                'last_name', 'first_name'
            ),
            ('last_name', 'first_name')
        )

    def test_function_w_unknown_arguments(self):
        self.assertEqual(
            src.functions.takes_unknown_keyword_arguments(
                a=1, b=2, c=3, d=4
            ),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        )
        self.assertEqual(
            src.functions.takes_unknown_keyword_arguments(
                none=None,
                a_boolean=bool,
                an_integer=int,
                a_float=float,
                a_string=str,
                a_tuple=tuple,
                a_list=list,
                a_set=set,
                a_dictionary=dict,
            ),
            dict(
                a_boolean=bool,
                a_dictionary=dict,
                a_float=float,
                a_list=list,
                a_set=set,
                a_string=str,
                a_tuple=tuple,
                an_integer=int,
                none=None,
            )
        )

    def test_function_w_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.takes_positional_and_keyword_arguments(
                'first_name', last_name='last_name',
            ),
            ('first_name', 'last_name')
        )
        self.assertEqual(
            src.functions.takes_positional_and_keyword_arguments('first_name'),
            ('first_name', 'Doe')
        )

    def test_function_w_unknown_positional_and_keyword_arguments(self):
        self.assertEqual(
            src.functions.takes_unknown_positional_and_keyword_arguments(
                None, bool, int, float, str, tuple, list, set, dict,
                none=None, a_boolean=bool, an_integer=int, a_float=float,
                a_string=str, a_tuple=tuple, a_list=list, a_set=set,
                a_dictionary=dict,
            ),
            (
                (None, bool, int, float, str, tuple, list, set, dict),
                {
                    'a_boolean': bool, 'a_dictionary': dict, 'a_float': float, 'a_list': list,
                    'a_set': set, 'a_string': str, 'a_tuple': tuple, 'an_integer': int,
                    'none': None
                }
            )
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError