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
# a dictionary with things is true
# a set with things is true
# a list with things is true
# a tuple with things is true
# a string with things is true
# positive and negative numbers are true
# True is true
# True is not false
# True is a boolean
# the empty dictionary is false
# the empty set is false
# the empty list is false
# the empty tuple is false
# the empty string is false
# 0 is false
# None is false
# False is false
# False is not true
# False is a boolean

# Exceptions seen
# AssertionError