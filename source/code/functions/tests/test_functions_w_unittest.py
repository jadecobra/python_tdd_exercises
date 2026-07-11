import src.functions
import unittest


class TestFunctions(unittest.TestCase):

    first = 'first'
    last = 'last'
    a_tuple = (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']
    a_set = {0, 1, 2, 'n'}
    a_dictionary = {'key': 'value'}

    def test_making_a_function_w_pass(self):
        result = src.functions.w_pass()

        assert result is None
        self.assertIs(result, None)

    def test_making_a_function_w_return(self):
        result = src.functions.w_return()

        assert result is None
        self.assertIs(result, None)

    def test_making_a_function_w_return_none(self):
        result = src.functions.w_return_none()

        assert result is None
        self.assertIs(result, None)

    def test_what_happens_after_functions_return(self):
        result = src.functions.return_leaves_the_function()

        assert result is None
        self.assertIs(result, None)

    def test_constant_function(self):
        result = src.functions.constant()
        expectation = 'the same thing'

        assert result == expectation
        self.assertEqual(result, expectation)

    def test_identity_function(self):
        result = src.functions.identity(None)

        assert result == None
        self.assertEqual(result, None)

        result = src.functions.identity(object)

        assert result == object
        self.assertEqual(result, object)

    def test_why_use_a_function(self):
        def add_x(number):
            return 3 + number

        result = add_x(0)
        expectation = 3
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(1)
        expectation = 4
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(2)
        expectation = 5
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(3)
        expectation = 6
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(4)
        expectation = 7
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(5)
        expectation = 8
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(6)
        expectation = 9
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(7)
        expectation = 10
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(8)
        expectation = 11
        assert result == expectation
        self.assertEqual(result, expectation)

        result = add_x(9)
        expectation = 12
        assert result == expectation
        self.assertEqual(result, expectation)

    def test_positional_arguments(self):
        positional_arguments = (
            src.functions.positional_arguments
        )

        reality = positional_arguments(
            self.first, self.last
        )
        my_expectation = (self.first, self.last)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = positional_arguments(
            self.last, self.first
        )
        my_expectation = (self.last, self.first)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = positional_arguments(0, 1)
        my_expectation = (0, 1)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = positional_arguments(
            self.a_tuple, self.a_list
        )

        my_expectation = (self.a_tuple, self.a_list)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        keyword_arguments = (
            src.functions.keyword_arguments
        )

        reality = keyword_arguments(
            self.a_set, self.a_dictionary,
        )
        my_expectation = (
            self.a_set, self.a_dictionary
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_keyword_arguments(self):
        keyword_arguments = (
            src.functions.keyword_arguments
        )

        reality = keyword_arguments(
            first_input=self.first,
            last_input=self.last,
        )
        my_expectation = (self.first, self.last)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = keyword_arguments(
            last_input=self.last,
            first_input=self.first,
        )
        my_expectation = (self.first, self.last)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = keyword_arguments(
            last_input=0, first_input=1,
        )
        my_expectation = (1, 0)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = keyword_arguments(
            first_input=self.a_tuple,
            last_input=self.a_list,
        )
        my_expectation = (self.a_tuple, self.a_list)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        positional_arguments = (
            src.functions.positional_arguments
        )

        reality = positional_arguments(
            last_input=self.a_dictionary,
            first_input=self.a_set,
        )
        my_expectation = (
            self.a_set, self.a_dictionary
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_args_and_kwargs(self):
        reality = src.functions.args_and_kwargs(
            self.first, last_input=self.last,
        )
        my_expectation = (self.first, self.last)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_optional_arguments(self):
        optional_arguments = (
            src.functions.optional_arguments
        )

        first_name, last_name = 'jane', 'doe'

        reality = optional_arguments(first_name)
        my_expectation = (first_name, last_name)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        first_name, blow = 'joe', 'blow'

        reality = optional_arguments(
            first_name, blow
        )
        my_expectation = (first_name, blow)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        first_name = 'john'

        reality = optional_arguments(
            first_input=first_name
        )
        my_expectation = (first_name, last_name)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        last_name = 'smith'

        reality = optional_arguments(
            last_input=last_name,
            first_input=first_name,
        )
        my_expectation = (first_name, last_name)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_unknown_number_of_arguments(self):
        unknown_number_of_arguments = (
            src.functions.unknown_number_of_arguments
        )

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3}

        reality = unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (a_tuple, a_dictionary)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1)
        a_dictionary = {'a': 2, 'b': 3, 'c': 4}

        reality = unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (a_tuple, a_dictionary)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1, 2)
        a_dictionary = {'a': 3, 'b': 4, 'c': 5}

        reality = unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        )
        my_expectation = (a_tuple, a_dictionary)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        a_tuple = (0, 1, 2, 'n')

        reality = unknown_number_of_arguments(*a_tuple)
        my_expectation = (a_tuple, {})
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}

        reality = unknown_number_of_arguments(
            **a_dictionary
        )
        my_expectation = ((), a_dictionary)
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = unknown_number_of_arguments()
        my_expectation = ((), {})
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# TypeError
# SyntaxError
# ModuleNotFoundError
# AttributeError