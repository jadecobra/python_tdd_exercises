import random
import src.calculator
import unittest


def a_random_number():
    return random.triangular(-1000.0, 1000.0)


class TestCalculator(unittest.TestCase):

    @staticmethod
    def get_division_result(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()

        x = self.random_first_number
        y = self.random_second_number

        self.calculator_tests = {
            'add': x+y,
            'subtract': x-y,
            'multiply': x*y,
            'divide': self.get_division_result(x, y)
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

        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    src.calculator.__getattribute__(operation)(
                        *two_numbers
                    ),
                    self.calculator_tests[operation]
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

        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    src.calculator.__getattribute__(operation)(
                        **two_numbers
                    ),
                    self.calculator_tests[operation]
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
        for operation in self.calculator_tests:
            with (
                self.subTest(operation=operation),
                self.assertRaises(TypeError),
            ):
                src.calculator.__getattribute__(operation)(
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
            for operation in self.calculator_tests:
                with self.subTest(
                    operation=operation,
                    bad_input=bad_input,
                ):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            bad_input, a_random_number()
                        ),
                        'brmph?! Numbers only. Try again...'
                    )

    def test_calculator_functions(self):
        for operation in self.calculator_tests:
            with self.subTest(operation=operation):
                self.assertEqual(
                    src.calculator.__getattribute__(operation)(
                        self.random_first_number,
                        self.random_second_number
                    ),
                    self.calculator_tests[operation]
                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# KeyError