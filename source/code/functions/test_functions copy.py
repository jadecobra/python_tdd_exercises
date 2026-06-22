import src.functions
import unittest


def add_x(number):
    # return 2 + number
    return 3 + number


class TestFunctions(unittest.TestCase):

    def test_why_use_a_function(self):
        # reality = 1 + 0
        # reality = 2 + 0
        reality = add_x(0)
        # my_expectation = 0
        # my_expectation = 1
        # my_expectation = 2
        my_expectation = 3
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 1
        # reality = 2 + 1
        reality = add_x(1)
        # my_expectation = 1
        # my_expectation = 2
        # my_expectation = 3
        my_expectation = 4
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 2
        # reality = 2 + 2
        reality = add_x(2)
        # my_expectation = 2
        # my_expectation = 3
        # my_expectation = 4
        my_expectation = 5
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 3
        # reality = 2 + 3
        reality = add_x(3)
        # my_expectation = 3
        # my_expectation = 4
        # my_expectation = 5
        my_expectation = 6
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 4
        # reality = 2 + 4
        reality = add_x(4)
        # my_expectation = 4
        # my_expectation = 5
        # my_expectation = 6
        my_expectation = 7
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 5
        # reality = 2 + 5
        reality = add_x(5)
        # my_expectation = 5
        # my_expectation = 6
        # my_expectation = 7
        my_expectation = 8
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 6
        # reality = 2 + 6
        reality = add_x(6)
        # my_expectation = 6
        # my_expectation = 7
        # my_expectation = 8
        my_expectation = 9
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 7
        # reality = 2 + 7
        reality = add_x(7)
        # my_expectation = 7
        # my_expectation = 8
        # my_expectation = 9
        my_expectation = 10
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 8
        # reality = 2 + 8
        reality = add_x(8)
        # my_expectation = 8
        # my_expectation = 9
        # my_expectation = 10
        my_expectation = 11
        self.assertEqual(reality, my_expectation)

        # reality = 1 + 9
        # reality = 2 + 9
        reality = add_x(9)
        # my_expectation = 9
        # my_expectation = 10
        # my_expectation = 11
        my_expectation = 12
        self.assertEqual(reality, my_expectation)

    def test_making_a_function_w_pass(self):
        self.assertIs(src.functions.w_pass(), None)

    def test_making_a_function_w_return(self):
        self.assertIs(src.functions.w_return(), None)

    def test_making_a_function_w_return_none(self):
        self.assertIs(
            src.functions.w_return_none(), None
        )

    def test_what_happens_after_a_function_returns(self):
        self.assertIs(
            src.functions.return_is_last(), None
        )

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

    def test_w_positional_arguments(self):
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

        a_tuple = (1, 2, 3, 'n')
        a_list = [1, 2, 3, 'n']
        reality = src.functions.w_positional_arguments(
            a_tuple, a_list,
        )
        my_expectation = (a_tuple, a_list)
        self.assertEqual(reality, my_expectation)

    def test_w_keyword_arguments(self):
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

        a_tuple = (1, 2, 3, 'n')
        a_list = [1, 2, 3, 'n']
        reality = src.functions.w_positional_arguments(
            first_input=a_list,
            last_input=a_tuple,
        )
        my_expectation = (a_list, a_tuple)
        self.assertEqual(reality, my_expectation)

    def test_w_args_and_kwargs(self):
        first, last = 'first', 'last'
        reality = (
            src.functions.w_args_and_kwargs(
                first, last_input=last,
            )
        )
        my_expectation = (first, last)
        self.assertEqual(reality, my_expectation)

    def test_w_optional_arguments(self):
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
            first_input=first_name,
        )
        my_expectation = (first_name, last_name)
        self.assertEqual(reality, my_expectation)

        last_name = 'smith'
        reality = src.functions.w_optional_arguments(
            last_input=last_name,
            first_input=first_name,
        )
        my_expectation = (first_name, last_name)
        self.assertEqual(reality, my_expectation)

    def test_w_unknown_arguments(self):
        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}
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
            *a_tuple, **a_dictionary,
        )
        my_expectation = (
            a_tuple, a_dictionary
        )
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1, 2, 3)
        reality = src.functions.w_unknown_arguments(
            *a_tuple
        )
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