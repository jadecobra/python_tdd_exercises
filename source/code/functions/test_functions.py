import src.functions
import unittest


def add_x(number):
    return 3 + number


class TestFunctions(unittest.TestCase):

    def test_why_use_a_function(self):
        reality = add_x(0)
        my_expectation = 3
        self.assertEqual(reality, my_expectation)

        reality = add_x(1)
        my_expectation = 4
        self.assertEqual(reality, my_expectation)

        reality = add_x(2)
        my_expectation = 5
        self.assertEqual(reality, my_expectation)

        reality = add_x(3)
        my_expectation = 6
        self.assertEqual(reality, my_expectation)

        reality = add_x(4)
        my_expectation = 7
        self.assertEqual(reality, my_expectation)

        reality = add_x(5)
        my_expectation = 8
        self.assertEqual(reality, my_expectation)

        reality = add_x(6)
        my_expectation = 9
        self.assertEqual(reality, my_expectation)

        reality = add_x(7)
        my_expectation = 10
        self.assertEqual(reality, my_expectation)

        reality = add_x(8)
        my_expectation = 11
        self.assertEqual(reality, my_expectation)

        reality = add_x(9)
        my_expectation = 12
        self.assertEqual(reality, my_expectation)

    def test_making_a_function_w_pass(self):
        reality = src.functions.w_pass()
        my_expectation = None
        self.assertEqual(reality, my_expectation)

    def test_making_a_function_w_return(self):
        reality = src.functions.w_return()
        my_expectation = None
        self.assertEqual(reality, my_expectation)

    def test_making_a_function_w_return_none(self):
        reality = src.functions.w_return_none()
        my_expectation = None
        self.assertEqual(reality, my_expectation)

    def test_what_happens_after_functions_return(self):
        reality = src.functions.return_is_last()
        my_expectation = None
        self.assertEqual(reality, my_expectation)

    def test_constant_function(self):
        reality = src.functions.constant()
        my_expectation = 'the same thing'
        self.assertEqual(reality, my_expectation)

    def test_identity_function(self):
        reality = src.functions.identity(None)
        my_expectation = None
        self.assertEqual(reality, my_expectation)

        reality = src.functions.identity(object)
        my_expectation = object
        self.assertEqual(reality, my_expectation)

    def test_functions_w_positional_arguments(self):
        first, last = 'first', 'last'

        reality = src.functions.w_positional_arguments(
            first, last,
        )
        my_expectation = (first, last)
        self.assertEqual(reality, my_expectation)

        reality = src.functions.w_positional_arguments(
            last, first,
        )
        my_expectation = (last, first)
        self.assertEqual(reality, my_expectation)

        first_number, second_number = 0, 1
        reality = src.functions.w_positional_arguments(
            first_number, second_number,
        )
        my_expectation = (first_number, second_number)
        self.assertEqual(reality, my_expectation)

        a_tuple, a_list = (1, 2, 3, 'n'), [1, 2, 3, 'n']
        reality = src.functions.w_positional_arguments(
            a_tuple, a_list,
        )
        my_expectation = (a_tuple, a_list)
        self.assertEqual(reality, my_expectation)

    def test_functions_w_keyword_arguments(self):
        first, last = 'first', 'last'

        reality = src.functions.w_keyword_arguments(
            first_input=first, last_input=last,
        )
        my_expectation = (first, last)
        self.assertEqual(reality, my_expectation)

        reality = src.functions.w_keyword_arguments(
            last_input=last, first_input=first,
        )
        my_expectation = (first, last)
        self.assertEqual(reality, my_expectation)

        reality = src.functions.w_keyword_arguments(
            last, first,
        )
        my_expectation = (last, first)
        self.assertEqual(reality, my_expectation)

        zero, one = 0, 1
        reality = src.functions.w_keyword_arguments(
            last_input=zero, first_input=one,
        )
        my_expectation = (one, zero)
        self.assertEqual(reality, my_expectation)

        a_set = {1, 2, 3, 'n'}
        a_dictionary = {'key': 'value'}
        reality = src.functions.w_keyword_arguments(
            first_input=a_set,
            last_input=a_dictionary,
        )
        my_expectation = (a_set, a_dictionary)
        self.assertEqual(reality, my_expectation)

        a_tuple, a_list = (1, 2, 3, 'n'), [1, 2, 3, 'n']
        reality = src.functions.w_positional_arguments(
            first_input=a_list,
            last_input=a_tuple,
        )
        my_expectation = (a_list, a_tuple)
        self.assertEqual(reality, my_expectation)

    def test_functions_w_positional_and_keyword_args(self):
        first, last = 'first', 'last'
        reality = (
            src.functions.w_positional_and_keyword_args(
                first, last_input=last,
            )
        )
        my_expectation = (first, last)
        self.assertEqual(reality, my_expectation)

    def test_functions_w_optional_arguments(self):
        first_name, last_name = 'jane', 'doe'
        reality = src.functions.w_optional_arguments(
            first_name,
        )
        my_expectation = (first_name, last_name)
        self.assertEqual(reality, my_expectation)

        first_name, blow = 'joe', 'blow'
        reality = src.functions.w_optional_arguments(
            first_name, blow,
        )
        my_expectation = (first_name, blow)
        self.assertEqual(reality, my_expectation)

        first_name = 'john'
        reality = src.functions.w_optional_arguments(
            first_input=first_name
        )
        my_expectation = (first_name, last_name)
        self.assertEqual(reality, my_expectation)

        last_name = 'smith'
        reality = src.functions.w_optional_arguments(
            last_input=last_name, first_input=first_name,
        )
        my_expectation = (first_name, last_name)
        self.assertEqual(reality, my_expectation)

    def test_functions_w_unknown_arguments(self):
        a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
        reality = src.functions.w_unknown_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (a_tuple, a_dictionary)
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3, 'c': 4}
        reality = src.functions.w_unknown_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (
            a_tuple, a_dictionary
        )
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}
        reality = src.functions.w_unknown_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (
            a_tuple, a_dictionary
        )
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1, 2, 3)
        reality = src.functions.w_unknown_arguments(*a_tuple)
        my_expectation = (a_tuple, {})
        self.assertEqual(reality, my_expectation)

        a_dictionary = {'a': 4, 'b': 5, 'c': 6, 'd': 7}
        reality = src.functions.w_unknown_arguments(
            **a_dictionary
        )
        my_expectation = ((), a_dictionary)
        self.assertEqual(reality, my_expectation)

        reality = src.functions.w_unknown_arguments()
        my_expectation = ((), {})
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError