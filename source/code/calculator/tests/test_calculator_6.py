import random
import src.calculator
import unittest


def a_random_number():
    return random.triangular(-1000.0, 1000.0)


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()

    def test_addition(self):
        self.assertEqual(
            src.calculator.add(
                self.random_first_number,
                self.random_second_number
            ),
            self.random_first_number+self.random_second_number
        )

    def test_subtraction(self):
        self.assertEqual(
            src.calculator.subtract(
                self.random_first_number,
                self.random_second_number
            ),
            self.random_first_number-self.random_second_number
        )

    def test_multiplication(self):
        self.assertEqual(
            src.calculator.multiply(
                self.random_first_number,
                self.random_second_number
            ),
            self.random_first_number*self.random_second_number
        )

    def test_division(self):
        try:
            self.assertEqual(
                src.calculator.divide(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number/self.random_second_number
            )
        except ZeroDivisionError:
            self.assertEqual(
                src.calculator.divide(self.random_first_number, 0),
                'brmph?! I cannot divide by 0. Try again...'
            )

    def test_calculator_w_list_items(self):
        two_numbers = [
            self.random_first_number,
            self.random_second_number
        ]

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
        self.assertEqual(
            src.calculator.add(*two_numbers),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(*two_numbers),
            self.random_first_number/self.random_second_number
        )
        self.assertEqual(
            src.calculator.multiply(*two_numbers),
            self.random_first_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(*two_numbers),
            self.random_first_number-self.random_second_number
        )

    def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
        not_two_numbers = [0, 1, 2]

        with self.assertRaises(TypeError):
            src.calculator.add(*not_two_numbers)
        with self.assertRaises(TypeError):
            src.calculator.divide(*not_two_numbers)
        with self.assertRaises(TypeError):
            src.calculator.multiply(*not_two_numbers)
        with self.assertRaises(TypeError):
            src.calculator.subtract(*not_two_numbers)

    def test_calculator_sends_message_when_input_is_not_a_number(self):
        error_message = 'brmph?! Numbers only. Try again...'

        [
            self.assertEqual(
                src.calculator.add(data_type, a_random_number()),
                error_message
            ) for data_type in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            )
        ]

        for data_type in (
            None,
            True, False,
            str(), 'text',
            tuple(), (0, 1, 2, 'n'),
            list(), [0, 1, 2, 'n'],
            set(), {0, 1, 2, 'n'},
            dict(), {'key': 'value'},
        ):
            with self.subTest(data_type=data_type):
                self.assertEqual(
                    src.calculator.add(
                        data_type, a_random_number()
                    ),
                    error_message
                )
                self.assertEqual(
                    src.calculator.divide(
                        data_type, a_random_number()
                    ),
                    error_message
                )
                self.assertEqual(
                    src.calculator.multiply(
                        data_type, a_random_number()
                    ),
                    error_message
                )
                self.assertEqual(
                    src.calculator.subtract(
                        data_type, a_random_number()
                    ),
                    error_message
                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError