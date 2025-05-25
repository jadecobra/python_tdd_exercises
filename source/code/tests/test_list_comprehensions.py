import unittest
import src.list_comprehensions


class TestListComprehensions(unittest.TestCase):

    def setUp(self):
        self.a_list = []
        self.container = range(10)

    def test_make_a_list_from_an_iterable(self):
        self.assertEqual(
            list(self.container),
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            src.list_comprehensions.make_a_list(self.container),
            list(self.container)
        )

    def test_make_a_list_w_a_for_loop(self):
        for item in self.container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            src.list_comprehensions.for_loop(self.container),
            self.a_list
        )

    def test_make_a_list_w_list_comprehensions(self):
        a_list = [item for item in self.container]

        self.assertEqual(
            a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.container),
            a_list
        )
        self.assertEqual(
            src.list_comprehensions.for_loop(self.container),
            src.list_comprehensions.make_a_list(self.container)
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.container),
            src.list_comprehensions.make_a_list(self.container)
        )

    def test_list_comprehensions_w_conditions_i(self):
        even_numbers = []

        for item in self.container:
            if item % 2 == 0:
                even_numbers.append(item)

        self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(self.container),
            [item for item in self.container if item % 2 == 0]
        )

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []

        for item in self.container:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
        self.assertEqual(
            [item for item in self.container if item % 2 != 0],
            odd_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(self.container),
            odd_numbers
        )



# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError