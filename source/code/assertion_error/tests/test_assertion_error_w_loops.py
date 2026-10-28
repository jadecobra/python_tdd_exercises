import unittest


def assert_not_equal(x, y):
    assert x != y


def assert_equal(x, y):
    assert x == y


class TestAssertionError(unittest.TestCase):

    basic_objects = (
        None, False, True,
        0, 0.0, '', (), [], set(), {},
    )

    def test_assertion_error(self):
        for first in self.basic_objects:
            for second in self.basic_objects:
                with self.subTest(pair=(first, second)):
                    try:
                        assert first is second
                    except AssertionError:
                        assert first is not second

                    try:
                        self.assertIsNot(first, second)
                    except AssertionError:
                        self.assertIs(first, second)

                    try:
                        self.assertEqual(first, second)
                    except AssertionError:
                        self.assertNotEqual(first, second)

    def test_assert_keyword(self):
        for reality, my_expectation in (
            (1 + 1, 2),
            ('1' + '1', '11'),
            ('I am' + ' alive', 'I am alive')
        ):
            with self.subTest((reality, my_expectation)):
                assert_equal(reality, my_expectation)
                self.assertEqual(reality, my_expectation)

    def test_assertion_error_w_none(self):
        for an_object in self.basic_objects:
            with self.subTest(object=an_object):
                try:
                    self.assertIsNotNone(an_object)
                except AssertionError:
                    self.assertIsNone(an_object)

    def will_not_run():
        # will not run because
        # the name does not start with test
        assert False == True
        self.assertEqual(False, True)

    def test_failure(self):
        assert_not_equal(False, True)
        self.assertEqual(False, False)


# NOTES
# a dictionary is not the same object as True
# a dictionary is not the same object as False
# a dictionary is not the same object as None
# a set is not the same object as True
# a set is not the same object as False
# a set is not the same object as None
# a list is not the same object as True
# a list is not the same object as False
# a list is not the same object as None
# a tuple is not the same object as True
# a tuple is not the same object as False
# a tuple is not the same object as None
# a string is not the same object as True
# a string is not the same object as False
# a string is not the same object as None
# a float is not the same object as True
# a float is not the same object as False
# a float is not the same object as None
# an integer is not the same object as True
# an integer is not the same object as False
# an integer is not the same object as None
# True is True and equal to True
# True is not equal to False
# True is not the same object as False
# True is not equal to None
# True is not the same object as None
# False is not equal to True
# False is not the same object as True
# False is False and equal to False
# False is not equal to None
# False is not the same object as None
# None is not equal to True
# None is not the same object as True
# None is not equal to False
# None is not the same object as False
# None is None and equal to None


# Exceptions seen
# AssertionError
# IndentationError
# AttributeError
# NameError
# TypeError