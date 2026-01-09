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
                'undefined: I cannot divide by 0'
            )

    def test_calculator_sends_message_when_input_is_not_a_number(self):
        error_message = 'Excuse me?! I only work with numbers. Please try again...'

        for data_type in (
            None,
            True,
            False,
            str(),
            tuple(),
            list(),
            set(),
            dict(),
        ):
            with self.subTest(i=data_type):
                self.assertEqual(
                    src.calculator.add(data_type, a_random_number()),
                    error_message
                )
                self.assertEqual(
                    src.calculator.divide(data_type, a_random_number),
                    error_message
                )
                self.assertEqual(
                    src.calculator.multiply(data_type, a_random_number()),
                    error_message
                )
                self.assertEqual(
                    src.calculator.subtract(data_type, a_random_number()),
                    error_message
                )

    def test_calculator_w_list_items(self):
        a_list = [self.random_first_number, self.random_second_number]

        self.assertEqual(
            src.calculator.add(a_list[0], a_list[1]),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(a_list[-2], a_list[-1]),
            self.random_first_number/self.random_second_number
        )
        self.assertEqual(
            src.calculator.multiply(a_list[1], a_list[-1]),
            self.random_second_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(a_list[-2], a_list[0]),
            self.random_first_number-self.random_first_number
        )
        self.assertEqual(
            src.calculator.add(*a_list),
            self.random_first_number+self.random_second_number
        )
        self.assertEqual(
            src.calculator.divide(*a_list),
            self.random_first_number/self.random_second_number
        )
        self.assertEqual(
            src.calculator.multiply(*a_list),
            self.random_first_number*self.random_second_number
        )
        self.assertEqual(
            src.calculator.subtract(*a_list),
            self.random_first_number-self.random_second_number
        )

    def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
        another_list = [0, 1, 2]

        with self.assertRaises(TypeError):
            src.calculator.add(*another_list)
        with self.assertRaises(TypeError):
            src.calculator.divide(*another_list)
        with self.assertRaises(TypeError):
            src.calculator.multiply(*another_list)
        with self.assertRaises(TypeError):
            src.calculator.subtract(*another_list)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError
# SyntaxError