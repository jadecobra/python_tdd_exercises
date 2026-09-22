import unittest


def assert_is_not(x, y):
    assert x is not y


def assert_is_not_none(x):
    assert_is_not(x, None)


def assert_is_not_false(x):
    assert_is_not(x, False)


def assert_is_not_true(x):
    assert_is_not(x, True)


def assert_not_equal(x, y):
    assert x != y


def assert_equal(x, y):
    assert x == y


class TestAssertionError(unittest.TestCase):

    an_integer = 0
    a_float = 0.0
    a_string = ''
    a_tuple = ()
    a_list = []
    a_set = set()
    a_dictionary = {}

    def test_assert_keyword(self):
        reality = 1 + 1
        my_expectation = 2
        assert_equal(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

        reality = '1' + '1'
        my_expectation = '11'
        assert_equal(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

        reality = 'I am' + ' alive'
        my_expectation = 'I am alive'
        assert_equal(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIs(None, None)
        self.assertIsNone(None)

        assert_is_not_none(False)
        self.assertIsNot(False, None)
        self.assertIsNotNone(False)

        assert_is_not_none(True)
        self.assertIsNot(True, None)
        self.assertIsNotNone(True)

        assert_is_not_none(self.an_integer)
        self.assertIsNot(self.an_integer, None)
        self.assertIsNotNone(self.an_integer)

        assert_is_not_none(self.a_float)
        self.assertIsNot(self.a_float, None)
        self.assertIsNotNone(self.a_float)

        assert_is_not_none(self.a_string)
        self.assertIsNot(self.a_string, None)
        self.assertIsNotNone(self.a_string)

        assert_is_not_none(self.a_tuple)
        self.assertIsNot(self.a_tuple, None)
        self.assertIsNotNone(self.a_tuple)

        assert_is_not_none(self.a_list)
        self.assertIsNot(self.a_list, None)
        self.assertIsNotNone(self.a_list)

        assert_is_not_none(self.a_set)
        self.assertIsNot(self.a_set, None)
        self.assertIsNotNone(self.a_set)

        assert_is_not_none(self.a_dictionary)
        self.assertIsNot(self.a_dictionary, None)
        self.assertIsNotNone(self.a_set)

    def test_assertion_error_w_false(self):
        assert False is False
        self.assertIs(False, False)

        assert_is_not_false(None)
        self.assertIsNot(None, False)

        assert_is_not_false(True)
        self.assertIsNot(True, False)

        assert_is_not_false(self.an_integer)
        self.assertIsNot(self.an_integer, False)

        assert_is_not_false(self.a_float)
        self.assertIsNot(self.a_float, False)

        assert_is_not_false(self.a_string)
        self.assertIsNot(self.a_string, False)

        assert_is_not_false(self.a_tuple)
        self.assertIsNot(self.a_tuple, False)

        assert_is_not_false(self.a_list)
        self.assertIsNot(self.a_list, False)

        assert_is_not_false(self.a_set)
        self.assertIsNot(self.a_set, False)

        assert_is_not_false(self.a_dictionary)
        self.assertIsNot(self.a_dictionary, False)

    def test_assertion_error_w_true(self):
        assert True is True
        self.assertIs(True, True)

        assert_is_not_true(None)
        self.assertIsNot(None, True)

        assert_is_not_true(False)
        self.assertIsNot(False, True)

        assert_is_not_true(self.an_integer)
        self.assertIsNot(self.an_integer, True)

        assert_is_not_true(self.a_float)
        self.assertIsNot(self.a_float, True)

        assert_is_not_true(self.a_string)
        self.assertIsNot(self.a_string, True)

        assert_is_not_true(self.a_tuple)
        self.assertIsNot(self.a_tuple, True)

        assert_is_not_true(self.a_list)
        self.assertIsNot(self.a_list, True)

        assert_is_not_true(self.a_set)
        self.assertIsNot(self.a_set, True)

        assert_is_not_true(self.a_dictionary)
        self.assertIsNot(self.a_dictionary, True)

    def test_assertion_error_w_equality(self):
        assert_equal(None, None)
        self.assertEqual(None, None)

        assert_equal(False, False)
        self.assertEqual(False, False)

        assert_equal(True, True)
        self.assertEqual(True, True)

        assert_not_equal(False, None)
        self.assertNotEqual(False, None)

        assert_not_equal(False, True)
        self.assertNotEqual(False, True)

        assert_not_equal(True, None)
        self.assertNotEqual(True, None)

    def test_assertion_error_w_is_vs_equal(self):
        assert_is_not(0, 0.0)
        self.assertIsNot(0, 0.0)

        assert_equal(0, 0.0)
        self.assertEqual(0, 0.0)

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