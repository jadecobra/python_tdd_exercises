import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertIs(False, False)
        self.assertEqual(bool(False), False)
        self.assertFalse(bool(False))
        self.assertFalse(False)

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertIs(True, True)
        self.assertEqual(bool(True), True)
        self.assertTrue(bool(True))
        self.assertTrue(True)

    def test_is_none_falsy_or_truthy(self):
        self.assertFalse(bool(None))
        self.assertFalse(None)

    def test_is_an_integer_falsy_or_truthy(self):
        negative_integer = -1
        self.assertTrue(bool(negative_integer))
        self.assertTrue(negative_integer)

        self.assertFalse(bool(0))
        self.assertFalse(0)

        positive_integer = 1
        self.assertTrue(bool(positive_integer))
        self.assertTrue(positive_integer)

    def test_is_a_float_falsy_or_truthy(self):
        negative_float = -0.1
        self.assertTrue(bool(negative_float))
        self.assertTrue(negative_float)

        self.assertFalse(bool(0.0))
        self.assertFalse(0.0)

        a_positive_float = 0.1
        self.assertTrue(bool(a_positive_float))
        self.assertTrue(0.1)

    def test_is_a_string_falsy_or_truthy(self):
        self.assertFalse(bool(str()))
        self.assertFalse(str())

        a_string = "a string with things"
        self.assertTrue(bool(a_string))
        self.assertTrue(a_string)

    def test_is_a_tuple_falsy_or_truthy(self):
        self.assertFalse(bool(tuple()))
        self.assertFalse(tuple())

        a_tuple = (1, 2, 3, 'n')
        self.assertTrue(bool(a_tuple))
        self.assertTrue(a_tuple)

    def test_is_a_list_falsy_or_truthy(self):
        self.assertFalse(bool(list()))
        self.assertFalse(list())

        a_list = [1, 2, 3, 'n']
        self.assertTrue(bool(a_list))
        self.assertTrue(a_list)

    def test_is_a_set_falsy_or_truthy(self):
        self.assertFalse(bool(set()))
        self.assertFalse(set())

        a_set = {1, 2, 3, 'n'}
        self.assertTrue(bool(a_set))
        self.assertTrue(a_set)

    def test_is_a_dictionary_falsy_or_truthy(self):
        self.assertFalse(bool(dict()))
        self.assertFalse(dict())

        a_dictionary = {'key': 'value'}
        self.assertTrue(bool(a_dictionary))
        self.assertTrue(a_dictionary)


# NOTES
# bool(a dictionary with things) is True
# bool(a set with things) is True
# bool(a list with things) is True
# bool(a tuple with things) is True
# bool(a string with things) is True
# bool(a positive number) is True
# bool(a negative number) is True
# True is NOT False
# True is NOT equal to False
# True is a boolean
# bool(the empty dictionary) is False
# bool(the empty set) is False
# bool(the empty list) is False
# bool(the empty tuple) is False
# bool(the empty string) is False
# bool(zero) is False
# bool(None) is False
# False is NOT True
# False is NOT equal to True
# False is a boolean


# Exceptions seen
# AssertionError