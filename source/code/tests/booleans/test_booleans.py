import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse(str())
        self.assertFalse(tuple())
        self.assertFalse(list())
        self.assertFalse(set())
        self.assertFalse(dict())

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-0.1)
        self.assertTrue(0.1)
        self.assertTrue("text")
        self.assertTrue((1, 2, 3, 'n'))
        self.assertTrue([1, 2, 3, 'n'])
        self.assertTrue({1, 2, 3, 'n'})
        self.assertTrue({'key': 'value'})


# NOTES
# a set with things is True
# a list with things is True
# a tuple with things is True
# a string with things is True
# positive and negative numbers are True
# True is True
# True is not false
# True is a boolean
# the empty dictionary is False
# the empty set is False
# the empty list is False
# the empty tuple is False
# the empty string is False
# 0 is False
# None is False
# False is False
# False is not true
# False is a boolean


# Exceptions seen
# AssertionError