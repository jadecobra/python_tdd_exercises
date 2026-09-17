import src.functions
import unittest


def assert_is_none(something):
    assert something is None


class TestFunctions(unittest.TestCase):

    first = 'first'
    last = 'last'
    a_tuple = (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']
    a_set = {0, 1, 2, 'n'}
    a_dictionary = {'key': 'value'}

    def test_making_a_function_w_pass(self):
        assert_is_none(src.functions.w_pass())
        self.assertIs(src.functions.w_pass(), None)

    def test_making_a_function_w_return(self):
        assert_is_none(src.functions.w_return())
        self.assertIs(
            src.functions.w_return(), None
        )

    def test_making_a_function_w_return_none(self):
        assert_is_none(src.functions.w_return_none())
        self.assertIs(
            src.functions.w_return_none(), None
        )

    def test_what_happens_after_functions_return(self):
        assert_is_none(
            src.functions.return_leaves_the_function()
        )
        self.assertIs(
            src.functions.return_leaves_the_function(),
            None
        )

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(), 'the same thing'
        )

    def test_identity_function(self):
        assert_is_none(src.functions.identity(None))
        self.assertIs(
            src.functions.identity(None), None
        )

        self.assertEqual(
            src.functions.identity(object), object
        )

    def test_why_use_a_function(self):
        def add_x(number):
            return 3 + number

        self.assertEqual(add_x(0), 3)
        self.assertEqual(add_x(1), 4)
        self.assertEqual(add_x(2), 5)
        self.assertEqual(add_x(3), 6)
        self.assertEqual(add_x(4), 7)
        self.assertEqual(add_x(5), 8)
        self.assertEqual(add_x(6), 9)
        self.assertEqual(add_x(7), 10)
        self.assertEqual(add_x(8), 11)
        self.assertEqual(add_x(9), 12)

    def test_positional_arguments(self):
        positional_arguments = (
            src.functions.positional_arguments
        )

        self.assertEqual(
            positional_arguments(self.first, self.last),
            (self.first, self.last)
        )
        self.assertEqual(
            positional_arguments(self.last, self.first),
            (self.last, self.first)
        )

        self.assertEqual(
            positional_arguments(0, 1), (0, 1)
        )

        self.assertEqual(
            positional_arguments(
                self.a_tuple, self.a_list
            ),
            (self.a_tuple, self.a_list)
        )

        self.assertEqual(
            src.functions.keyword_arguments(
                self.a_set, self.a_dictionary
            ),
            (self.a_set, self.a_dictionary)
        )

    def test_keyword_arguments(self):
        keyword_arguments = (
            src.functions.keyword_arguments
        )

        self.assertEqual(
            keyword_arguments(
                first_input=self.first,
                last_input=self.last,
            ),
            (self.first, self.last)
        )
        self.assertEqual(
            keyword_arguments(
                last_input=self.last,
                first_input=self.first,
            ),
            (self.first, self.last)
        )

        self.assertEqual(
            keyword_arguments(
                last_input=0, first_input=1,
            ),
            (1, 0)
        )

        self.assertEqual(
            keyword_arguments(
                first_input=self.a_tuple,
                last_input=self.a_list,
            ),
            (self.a_tuple, self.a_list)
        )

        self.assertEqual(
            src.functions.positional_arguments(
                last_input=self.a_dictionary,
                first_input=self.a_set,
            ),
            (self.a_set, self.a_dictionary)
        )

    def test_args_and_kwargs(self):
        self.assertEqual(
            src.functions.args_and_kwargs(
                self.first, last_input=self.last
            ),
            (self.first, self.last)
        )

    def test_optional_arguments(self):
        optional_arguments = (
            src.functions.optional_arguments
        )

        first_name, last_name = 'jane', 'doe'
        self.assertEqual(
            optional_arguments(
                first_name,
            ),
            (first_name, last_name)
        )

        first_name, blow = 'joe', 'blow'
        self.assertEqual(
            optional_arguments(
                first_name, blow
            ),
            (first_name, blow)
        )

        first_name = 'john'
        self.assertEqual(
            optional_arguments(
                first_input=first_name,
            ),
            (first_name, last_name)
        )

        last_name = 'smith'
        self.assertEqual(
            optional_arguments(
                last_input=last_name,
                first_input=first_name,
            ),
            (first_name, last_name)
        )

    def test_unknown_number_of_arguments(self):
        unknown_number_of_arguments = (
            src.functions.unknown_number_of_arguments
        )

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
        self.assertEqual(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            ),
            (a_tuple, a_dictionary)
        )

        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        self.assertEqual(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            ),
            (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        self.assertEqual(
            unknown_number_of_arguments(
                *a_tuple, **a_dictionary
            ),
            (a_tuple, a_dictionary)
        )

        a_tuple = (0, 1, 2, 'n')
        self.assertEqual(
            unknown_number_of_arguments(*a_tuple),
            (a_tuple, {})
        )

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
        self.assertEqual(
            unknown_number_of_arguments(**a_dictionary),
            ((), a_dictionary)
        )

        self.assertEqual(
            unknown_number_of_arguments(), ((), {})
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# SyntaxError
# AttributeError