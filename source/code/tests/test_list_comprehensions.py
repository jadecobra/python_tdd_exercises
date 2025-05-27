import src.list_comprehensions
import unittest


class TestListComprehensions(unittest.TestCase):

    def setUp(self):
        self.iterable = range(10000000)

    def test_make_a_list_w_a_for_loop(self):
        a_list = []

        for item in self.iterable:
            a_list.append(item)

        self.assertEqual(
            a_list, list(self.iterable)
        )
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            a_list
        )

    def test_make_a_list_w_list_comprehensions(self):
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            [item for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.iterable),
            src.list_comprehensions.for_loop(self.iterable)
        )

    def test_list_comprehensions_w_conditions_i(self):
        even_numbers = []
        for item in self.iterable:
            if item % 2 == 0:
                even_numbers.append(item)

        self.assertEqual(
            [item for item in self.iterable if item % 2 == 0],
            even_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(self.iterable),
            even_numbers
        )

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []
        for item in self.iterable:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(
            [item for item in self.iterable if item % 2 != 0],
            odd_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(self.iterable),
            odd_numbers
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError