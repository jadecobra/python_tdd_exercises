import random
import src.dict_comprehensions
import unittest


def process(number):
    return number ** 2


class TestDictComprehensions(unittest.TestCase):

    def setUp(self):
        self.iterable = range(0, random.randint(2, 1000))

    def test_make_a_dictionary_w_a_dict_comprehension(self):
        a_dictionary = {}
        for item in self.iterable:
            a_dictionary[item] = item

        self.assertEqual(
            src.dict_comprehensions.for_loop(self.iterable),
            {item: item for item in self.iterable}
        )
        self.assertEqual(
            src.dict_comprehensions.dict_comprehension(self.iterable),
            {item: item for item in self.iterable}
        )

    def test_dict_comprehensions_w_functions(self):
        squares = {}
        for item in self.iterable:
            squares[item] = process(item)

        self.assertEqual(
            squares,
            {item: process(item) for item in self.iterable}
        )
        self.assertEqual(
            src.dict_comprehensions.square(self.iterable),
            {item: process(item) for item in self.iterable}
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError