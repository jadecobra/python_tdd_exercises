import random
import src.calculator
import unittest


def a_random_number():
    return random.triangular(-1000.0, 1000.0)


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()

        x = self.random_first_number
        y = self.random_second_number

        try:
            division_result = x / y
        except ZeroDivisionError:
            division_result = 'brmph?! I cannot divide by 0. Try again...'

        self.arithmetic_tests = {
            'addition': {
                'function': src.calculator.add,
                'expectation': x+y,
            },
            'subtraction': {
                'function': src.calculator.subtract,
                'expectation': x-y,
            },
            'division': {
                'function': src.calculator.divide,
                'expectation': division_result,
            },
            'multiplication': {
                'function': src.calculator.multiply,
                'expectation': x*y,
            }
        }

    def test_calculator_w_list_items(self):
        # two_numbers = [
        #     self.random_first_number,
        #     self.random_second_number
        # ]
        a_dictionary = {
            'x': self.random_first_number,
            'y': self.random_second_number
        }
        two_numbers = list(a_dictionary.values())

        for operation in self.arithmetic_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.arithmetic_tests[operation]['function'](
                        *two_numbers
                    ),
                    self.arithmetic_tests[operation]['expectation']
                )

        self.assertEqual(
            src.calculator.add(
                two_numbers[0],
                two_numbers[1]
            ),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(
                two_numbers[-2],
                two_numbers[-1]
            ),
            self.random_first_number/self.random_second_number
        )
        self.assertEqual(
            src.calculator.multiply(
                two_numbers[1],
                two_numbers[-1]
            ),
            self.random_second_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(
                two_numbers[-2],
                two_numbers[0]
            ),
            self.random_first_number-self.random_first_number
        )

    def test_calculator_w_dictionary_items(self):
        two_numbers = {
            'first_input': self.random_first_number,
            'second_input': self.random_second_number,
        }

        for operation in self.arithmetic_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.arithmetic_tests[operation]['function'](
                        **two_numbers
                    ),
                    self.arithmetic_tests[operation]['expectation']
                )

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
            self.random_first_number/self.random_second_number
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

    def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
        for operation in self.arithmetic_tests:
            with (
                self.subTest(operation=operation),
                self.assertRaises(TypeError),
            ):
                self.arithmetic_tests[operation]['function'](
                    [0, 1, 2]
                )

    def test_calculator_sends_message_when_input_is_not_a_number(self):
        for bad_input in (
            None,
            True, False,
            str(), 'text',
            tuple(), (0, 1, 2, 'n'),
            list(), [0, 1, 2, 'n'],
            set(), {0, 1, 2, 'n'},
            dict(), {'key': 'value'},
        ):
            for operation in self.arithmetic_tests:
                with self.subTest(
                    operation=operation,
                    bad_input=bad_input,
                ):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            bad_input, a_random_number()
                        ),
                        'brmph?! Numbers only. Try again...'
                    )

    def test_calculator_functions(self):
        for operation in self.arithmetic_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    self.arithmetic_tests[operation]['function'](
                        self.random_first_number,
                        self.random_second_number
                    ),
                    self.arithmetic_tests[operation]['expectation']
                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# KeyError