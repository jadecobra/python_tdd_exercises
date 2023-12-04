

How to create a simple Calculator: Tests and Solutions
======================================================


tests
-----

Here is the code in ``tests/test_assertion_error.py``

.. code-block:: python

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

    # TODO
    # test division

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # ZeroDivisionError

solutions
---------

Here are the solutions in ``calculator.py``

.. code-block:: python

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y
