import random
import src.list_comprehensions
import unittest


def process(number):
    return number ** 2


def condition(number):
    return number % 2 == 0


class TestListComprehensions(unittest.TestCase):

    def setUp(self):
        self.a_list = []
        self.an_iterable = range(0, random.randint(2, 1000))

    def test_making_a_list_w_a_for_loop(self):
        for number in self.an_iterable:
            self.a_list.append(number)

        self.assertEqual(self.a_list, list(self.an_iterable))
        self.assertEqual(
            src.list_comprehensions.a_for_loop(self.an_iterable),
            self.a_list
        )

    def test_making_a_list_w_extend(self):
        self.assertIsNone(self.a_list.extend(self.an_iterable))
        self.assertEqual(self.a_list, list(self.an_iterable))

    def test_making_a_list_w_a_list_comprehension(self):
        self.assertEqual(
            list(self.an_iterable),
            [item for item in self.an_iterable]
        )
        self.assertEqual(
            src.list_comprehensions.a_list_comprehension(
                self.an_iterable
            ),
            [item for item in self.an_iterable]
        )

    def test_making_a_list_w_conditions(self):
        even_numbers, odd_numbers = [], []
        for item in self.an_iterable:
            if condition(item):
                even_numbers.append(item)
            else:
                odd_numbers.append(item)

        self.assertEqual(
            even_numbers,
            [
                item for item in self.an_iterable
                      if condition(item)
            ]
        )
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(
                self.an_iterable,
            ),
            [
                item for item in self.an_iterable
                      if condition(item)
            ]
        )

        self.assertEqual(
            odd_numbers,
            [
                item for item in self.an_iterable
                      if not condition(item)
            ]
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(
                self.an_iterable
            ),
            [
                item for item in self.an_iterable
                      if not condition(item)
            ]
        )

    def test_making_a_list_w_processes(self):
        square_club = []
        for item in self.an_iterable:
            square_club.append(process(item))

        self.assertEqual(
            square_club,
            [process(item) for item in self.an_iterable]
        )
        self.assertEqual(
            src.list_comprehensions.square(self.an_iterable),
            [process(item) for item in self.an_iterable]
        )

    def test_making_a_list_w_processes_and_conditions(self):
        even_squares, odd_squares = [], []
        for item in self.an_iterable:
            if condition(item):
                even_squares.append(process(item))
            else:
                odd_squares.append(process(item))

        self.assertEqual(
            even_squares,
            [
                process(item)
                for item in self.an_iterable
                if condition(item)
            ]
        )
        self.assertEqual(
            odd_squares,
            [
                process(item)
                for item in self.an_iterable
                if not condition(item)
            ]
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError