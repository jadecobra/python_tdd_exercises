import random
import src.calculator
import unittest


def a_random_number():
    return random.triangular(-1000.0, 1000.0)


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.history = {}
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()
        try:
            self.division_result = (
                self.random_first_number / self.random_second_number
            )
        except ZeroDivisionError:
            self.division_result = 'brmph?! cannot divide by 0. Try again...'

        self.calculator_tests = {
            'addition': {
                'function': src.calculator.add,
                'expectation': (
                    self.random_first_number+self.random_second_number
                ),
            },
            'subtraction': {
                'function': src.calculator.subtract,
                'expectation': (
                    self.random_first_number-self.random_second_number
                ),
            },
            'division': {
                'function': src.calculator.divide,
                'expectation': self.division_result,
            },
            'multiplication': {
                'function': src.calculator.multiply,
                'expectation': (
                    self.random_first_number*self.random_second_number
                ),
            },
            'square': {
                'function': src.calculator.square,
                'expectation': self.random_first_number**2
            },
        }

    def test_calculator_functions(self):
        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.calculator_tests[operation]['function'](
                        self.random_first_number,
                        self.random_second_number
                    ),
                    self.calculator_tests[operation]['expectation']
                )

    def test_calculator_sends_message_when_input_is_not_a_number(self):
        error_message = 'brmph?! Numbers only. Try again...'

        for data in (
            None,
            True, False,
            str(), 'text',
            tuple(), (0, 1, 2, 'n'),
            list(), [0, 1, 2, 'n'],
            set(), {0, 1, 2, 'n'},
            dict(), {'key': 'value'},
        ):
            with self.subTest(i=data):
                for operation in self.calculator_tests:
                    self.assertEqual(
                        self.calculator_tests[operation]['function'](
                            data, a_random_number()
                        ),
                        error_message
                    )

    def test_calculator_w_list_items(self):
        # two_numbers = [self.random_first_number, self.random_second_number]
        a_dictionary = {
            'x': self.random_first_number,
            'y': self.random_second_number
        }
        two_numbers = list(a_dictionary.values())

        self.assertEqual(
            src.calculator.add(two_numbers[0], two_numbers[1]),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(two_numbers[-2], two_numbers[-1]),
            self.division_result
        )
        self.assertEqual(
            src.calculator.multiply(two_numbers[1], two_numbers[-1]),
            self.random_second_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(two_numbers[-2], two_numbers[0]),
            self.random_first_number-self.random_first_number
        )

        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.calculator_tests[operation]['function'](
                        *two_numbers
                    ),
                    self.calculator_tests[operation]['expectation']
                )

    def test_calculator_w_dictionary_items(self):
        two_numbers = {
            'first_input': self.random_first_number,
            'second_input': self.random_second_number,
        }

        self.assertEqual(
            src.calculator.add(
                two_numbers['first_input'],
                two_numbers['second_input']
            ),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(
                two_numbers['first_input'],
                two_numbers['second_input']
            ),
            self.division_result
        )
        self.assertEqual(
            src.calculator.multiply(
                two_numbers['second_input'],
                two_numbers['second_input']
            ),
            self.random_second_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(
                two_numbers['first_input'],
                two_numbers['first_input']
            ),
            self.random_first_number-self.random_first_number
        )

        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.calculator_tests[operation]['function'](
                        **two_numbers
                    ),
                    self.calculator_tests[operation]['expectation']
                )

    def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
        for operation in self.calculator_tests:
            with (
                self.subTest(operation=operation),
                self.assertRaises(TypeError),
            ):
                self.calculator_tests[operation]['function'](
                    *[0, 1, 2]
                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError
# SyntaxError