import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, (bool, int))
        self.assertNotIsInstance(False, float)
        for false_item in (
            False,
            None, bool(None),
            0, 0.0, bool(0), bool(0.0),
            str(), bool(str()),
            tuple(), bool(tuple()),
            list(), bool(list()),
            set(), bool(set()),
            dict(), bool(dict()),
        ):
            with self.subTest(item=false_item):
                self.assertFalse(false_item)

    def test_what_is_true(self):
        self.assertIsInstance(True, (bool, int))
        self.assertNotIsInstance(True, float)

        for true_item in (
            True,
            -1, bool(-1), 1, bool(1),
            -0.1, bool(-0.1), 0.1, bool(0.1),
            "text", bool("text"),
            ((1, 2, 3, 'n')), bool((1, 2, 3, 'n')),
            [1, 2, 3, 'n'], bool([1, 2, 3, 'n']),
            {1, 2, 3, 'n'}, bool({1, 2, 3, 'n'}),
            {'key': 'value'}, bool({'key': 'value'}),
        ):
            with self.subTest(item=true_item):
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
# a dictionary with things is True
# a set with things is True
# a list with things is True
# a tuple with things is True
# a string with things is True
# positive and negative numbers are True
# True is True
# True is not false
# True is a boolean
# True is an integer
# True is not a float
# True is 1
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
# False is an integer
# False is not a float
# False is 0


# Exceptions seen
# AssertionError