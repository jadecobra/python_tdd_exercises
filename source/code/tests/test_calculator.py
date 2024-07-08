import calculator
import random
import unittest


def random_number():
    return random.randint(-1, 1)


class TestCalculator(unittest.TestCase):

    x = random_number()
    y = random_number()

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
            self.y = random_number()
        self.assertEqual(
            calculator.divide(self.x, self.y),
            self.x/self.y
        )


# Exceptions Encountered
# AssertionError
# NameError
# TypeError
# ZeroDivisionError