import calculator
import random
import unittest


class TestCalculator(unittest.TestCase):

    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    def test_addition(self):
        self.assertEqual(
            calculator.add(self.x, self.y),
            self.x+self.y
        )

    def test_subtraction(self):
        self.assertEqual(
            calculator.subtract(self.x, self.y),
            self.x-self.y
        )

    def test_multiplication(self):
        self.assertEqual(
            calculator.multiply(self.x, self.y),
            self.x*self.y
        )

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(self.x, 0)
        while self.y == 0:
            self.y = random.randint(-1, 1)
        self.assertEqual(
            calculator.divide(self.x, self.y),
            self.x/self.y
        )

# Exceptions Encountered
# AssertionError
# NameError
# TypeError
# ZeroDivisionError