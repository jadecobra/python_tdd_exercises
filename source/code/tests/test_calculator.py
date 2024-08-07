import random
import src.calculator
import unittest


def a_random_number():
    return random.randint(-10, 10)


class TestCalculator(unittest.TestCase):

    x = a_random_number()
    y = a_random_number()

    def test_addition(self):
        self.assertEqual(
            src.calculator.add(self.x, self.y),
            self.x+self.y
        )

    def test_subtraction(self):
        self.assertEqual(
            src.calculator.subtract(self.x, self.y),
            self.x-self.y
        )

    def test_multiplication(self):
        self.assertEqual(
            src.calculator.multiply(self.x, self.y),
            self.x*self.y
        )

    def test_division(self):
        while self.y == 0:
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.x, self.y)
            self.y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.x, self.y),
                self.x/self.y
            )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError