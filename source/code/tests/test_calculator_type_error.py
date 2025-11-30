import random
import src.calculator
import unittest


def a_random_number():
    return random.randint(-10, 10)


class TestCalculator(unittest.TestCase):

    random_x = a_random_number()
    random_y = a_random_number()

    def test_addition(self):
        self.assertEqual(
            src.calculator.add(self.random_x, self.random_y),
            self.random_x+self.random_y
        )

    def test_subtraction(self):
        self.assertEqual(
            src.calculator.subtract(self.random_x, self.random_y),
            self.random_x-self.random_y
        )

    def test_multiplication(self):
        self.assertEqual(
            src.calculator.multiply(self.random_x, self.random_y),
            self.random_x*self.random_y
        )

    def test_division(self):
        while self.random_y == 0:
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_x, self.random_y)
            self.random_random_y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.random_x, self.random_y),
                self.random_x/self.random_y
            )

    def test_calculator_raises_type_error(self):
        self.assertEqual(
            src.calculator.add(self.random_x, None),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.divide(self.random_x, None),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.multiply(self.random_x, None),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.subtract(self.random_x, None),
            'I only work with numbers'
        )

    def test_calculator_with_strings(self):
        self.assertEqual(
            src.calculator.add('hello ', 'world'),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.divide('hello ', 'world'),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.multiply('hello', 'world'),
            'I only work with numbers'
        )
        self.assertEqual(
            src.calculator.subtract('hello', 'world'),
            'I only work with numbers'
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError