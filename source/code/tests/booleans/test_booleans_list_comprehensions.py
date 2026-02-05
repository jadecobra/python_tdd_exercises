import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, (bool, int))
        self.assertNotIsInstance(False, float)
        for false_item in (
            False,
            None,
            0, 0.0,
            str(),
            tuple(),
            list(),
            set(),
            dict(),
        ):
            with self.subTest(i=false_item):
                self.assertFalse(false_item)

    def test_what_is_true(self):
        self.assertIsInstance(True, (bool, int))
        self.assertNotIsInstance(True, float)
        for true_item in (
            True,
            -1, 1,
            -0.1, 0.1,
            'text',
            (1, 2, 3, 'n'),
            [1, 2, 3, 'n'],
            {1, 2, 3, 'n'},
            {'key': 'value'},
        ):
            with self.subTest(i=true_item):
                self.assertTrue(true_item)

    def test_the_value_of_false(self):
        self.assertEqual(False+1, 1)
        self.assertEqual(False-1, -1)
        self.assertEqual(False*1, 0)
        with self.assertRaises(ZeroDivisionError):
            1 / False

    def test_the_value_of_true(self):
        self.assertEqual(True+1, 2)
        self.assertEqual(True-1, 0)
        self.assertEqual(True*1, 1)
        self.assertEqual(True/1, 1)


# NOTES
# a dictionary with things is true
# a set with things is true
# a list with things is true
# a tuple with things is true
# a string with things is true
# positive and negative numbers are True
# True is true
# True is not false
# True is a boolean
# True is an integer
# True is not a float
# True is 1
# the empty dictionary is false
# the empty set is false
# the empty list is false
# the empty tuple is false
# the empty string is false
# 0 is False
# None is false
# False is false
# False is not true
# False is a boolean
# False is an integer
# False is not a float
# False is 0


# Exceptions seen
# AssertionError
