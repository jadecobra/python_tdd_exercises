import random
import src.calculator
import unittest


def a_random_number():
    return random.randint(-10, 10)


class TestCalculator(unittest.TestCase):

    random_first_number = a_random_number()
    random_second_number = a_random_number()

    def test_addition(self):
        self.assertEqual(
            src.calculator.add(self.random_first_number, self.random_second_number),
            self.random_first_number+self.random_second_number
        )

    def test_subtraction(self):
        self.assertEqual(
            src.calculator.subtract(self.random_first_number, self.random_second_number),
            self.random_first_number-self.random_second_number
        )

    def test_multiplication(self):
        self.assertEqual(
            src.calculator.multiply(self.random_first_number, self.random_second_number),
            self.random_first_number*self.random_second_number
        )

    def test_division(self):
        while self.random_second_number == 0:
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_first_number, self.random_second_number)
            self.random_second_number = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.random_first_number, self.random_second_number),
                self.random_first_number/self.random_second_number
            )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# ZeroDivisionError