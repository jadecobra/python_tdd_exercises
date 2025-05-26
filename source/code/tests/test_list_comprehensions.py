import src.list_comprehensions
import unittest


class TestListComprehensions(unittest.TestCase):

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        iterable = range(4)

        for item in iterable:
            a_list.append(item)

        self.assertEqual(a_list, [0, 1, 2, 3])
        self.assertEqual(
            src.list_comprehensions.for_loop(iterable),
            a_list
        )

    def test_make_a_list_w_list_comprehensions(self):
        iterable = range(4)

        self.assertEqual(
            src.list_comprehensions.for_loop(iterable),
            [item for item in iterable]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(iterable),
            src.list_comprehensions.for_loop(iterable)
        )

    def test_list_comprehensions_w_conditions_i(self):
        iterable = range(10)
        even_numbers = []

        for item in iterable:
            if item % 2 == 0:
                even_numbers.append(item)

        self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
        self.assertEqual(
            [item for item in iterable if item % 2 == 0],
            even_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(iterable),
            even_numbers
        )

    def test_list_comprehensions_w_conditions_ii(self):
        iterable = range(10)
        odd_numbers = []

        for item in iterable:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
        self.assertEqual(
            [item for item in iterable if item % 2 != 0],
            odd_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(iterable),
            odd_numbers
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError