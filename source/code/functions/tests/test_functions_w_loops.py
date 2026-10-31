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

    def test_functions_return_none_by_default(self):
        for a_function in (
            src.functions.w_pass,
            src.functions.w_return,
            src.functions.w_return_none,
            src.functions.return_leaves_the_function,
        ):
            with self.subTest(a_function):
                result = a_function()
                assert_is_none(result)
                self.assertIsNone(result)

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(), 'the same thing'
        )

    def test_identity_function(self):
        for an_object in (
            None, self.first, self.last,
            self.a_tuple, self.a_list,
            self.a_set, self.a_dictionary,
        ):
            with self.subTest(an_object):
                self.assertEqual(
                    src.functions.identity(an_object), an_object
                )

    def test_why_use_a_loop(self):
        def add_x(number):
            return 3 + number

        for number in range(9):
            self.assertEqual(add_x(number), 3+number)

    def test_positional_arguments(self):
        for first, second in (
            (self.first, self.last),
            (self.last, self.first),
            (0, 1),
            (self.a_tuple, self.a_list),
            (self.a_set, self.a_dictionary),
        ):
            self.assertEqual(
                src.functions.positional_arguments(
                    first, second
                ),
                (first, second)
            )
            self.assertEqual(
                src.functions.keyword_arguments(
                    first, second
                ),
                (first, second)
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