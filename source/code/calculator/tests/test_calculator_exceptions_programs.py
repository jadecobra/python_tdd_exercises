import random
import src.calculator
import unittest


def a_random_number():
    return random.triangular(-1000.0, 1000.0)


class TestCalculator(unittest.TestCase):

    random_first_number = a_random_number()
    random_second_number = a_random_number()

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
                'brmph?! cannot divide by 0. Try again...'
            )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError