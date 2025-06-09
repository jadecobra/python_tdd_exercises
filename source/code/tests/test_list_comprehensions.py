import random
import src.list_comprehensions
import unittest


def condition(number):
    return number % 2 == 0


def process(number):
    return number * number


class TestListComprehensions(unittest.TestCase):

    def setUp(self):
        self.iterable = range(random.randint(0, 1000))

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        for item in self.iterable:
            a_list.append(item)

        self.assertEqual(a_list, list(self.iterable))
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            list(self.iterable)
        )

    def test_make_a_list_w_list_comprehensions(self):
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            [item for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.iterable),
            [item for item in self.iterable]
        )

    def test_list_comprehensions_w_conditions_i(self):
        even_numbers = []
        for item in self.iterable:
            if condition(item):
                even_numbers.append(item)

        self.assertEqual(
            even_numbers,
            [item for item in self.iterable if condition(item)]
        )
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(self.iterable),
            [item for item in self.iterable if condition(item)]
        )

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []
        for item in self.iterable:
            if not condition(item):
                odd_numbers.append(item)

        self.assertEqual(
            odd_numbers,
            [item for item in self.iterable if not condition(item)]
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(self.iterable),
            [item for item in self.iterable if not condition(item)]
        )

    def test_list_comprehension_w_functions(self):
        square_numbers = []
        for item in self.iterable:
            square_numbers.append(process(item))

        self.assertEqual(
            square_numbers,
            [process(item) for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.get_square_numbers(self.iterable),
            [process(item) for item in self.iterable]
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError