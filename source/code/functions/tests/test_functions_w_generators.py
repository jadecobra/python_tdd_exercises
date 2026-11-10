import itertools
import src.functions
import unittest


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
                self.assertIsNone(a_function())

    def test_constant_function(self):
        self.assertEqual(
            src.functions.constant(), 'the same thing'
        )

    def test_identity_function(self):
        for an_object in (
            None, object, self.first, self.last,
            self.a_tuple, self.a_list,
            self.a_set, self.a_dictionary,
        ):
            with self.subTest(an_object):
                self.assertEqual(
                    src.functions.identity(an_object),
                    an_object
                )

    def test_why_use_a_for_loop(self):
        def add_x(number):
            return 3 + number

        for a_number in range(1000):
            with self.subTest(a_number):
                self.assertEqual(
                    add_x(a_number), a_number+3
                )

    def test_args_and_kwargs(self):
        for (first, second), a_function in itertools.product(
            (
                (self.first, self.last),
                (self.last, self.first),
                (0, 1),
                (self.a_tuple, self.a_list),
                (self.a_set, self.a_dictionary),
            ), (
                src.functions.positional_arguments,
                src.functions.keyword_arguments,
                src.functions.args_and_kwargs,
                src.functions.optional_arguments,
            )
        ):
            with self.subTest(
                a_function=a_function, inputs=(first, second)
            ):
                self.assertEqual(
                    a_function(first, second),
                    (first, second)
                )
                self.assertEqual(
                    a_function(
                        last_input=first,
                        first_input=second
                    ),
                    (second, first)
                )
                self.assertEqual(
                    a_function(
                        first, last_input=second,
                    ),
                    (first, second)
                )
                self.assertEqual(
                    a_function(
                        second, last_input=first,
                    ),
                    (second, first)
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