import unittest


class TestBooleans(unittest.TestCase):

    def test_what_are_booleans(self):
        for boolean in (False, True):
            with self.subTest(boolean):
                self.assertIsInstance(boolean, (bool, int))
                self.assertNotIsInstance(
                    boolean,
                    (
                        float, tuple, str,
                        list, set, dict,
                    )
                )
                self.assertIs(boolean, boolean)
                self.assertIs(bool(boolean), boolean)

    def test_what_is_falsy(self):
        self.assertFalse(bool(False))
        self.assertFalse(False)

        for an_object in (
            None, str(), tuple(),
            list(), set(), dict()
        ):
            with self.subTest(an_object):
                self.assert_is_not_the_same_as_false_or_true(an_object)
                self.assertFalse(bool(an_object))
                self.assertFalse(an_object)

    def test_what_is_truthy(self):
        self.assertTrue(bool(True))
        self.assertTrue(True)

        for an_object in (
            -1, -0.1, 0.1,
            'string with things',
            (0, 1, 2, 'n'),
            [0, 1, 2, 'n'],
            {0, 1, 2, 'n'},
            {'key': 'value'},
        ):
            with self.subTest(an_object):
                self.assert_is_not_the_same_as_false_or_true(an_object)
                self.assertTrue(bool(an_object))
                self.assertTrue(an_object)

    def assert_is_not_the_same_as_false_or_true(self, an_object):
        for boolean in (False, True):
            with self.subTest(
                an_object=an_object, boolean=boolean
            ):
                self.assertNotEqual(an_object, boolean)
                self.assertIsNot(an_object, boolean)

    def test_the_value_of_false(self):
        for zero in (0, 0.0):
            with self.subTest(zero):
                self.assertEqual(zero, False)
                self.assertIsNot(zero, True)
                self.assertNotEqual(zero, True)
                self.assertIsNot(zero, False)
                self.assertFalse(bool(zero))
                self.assertFalse(zero)

    def test_the_value_of_true(self):
        a_positive_integer = 1
        self.assertNotEqual(a_positive_integer, False)
        self.assertIsNot(a_positive_integer, False)
        self.assertEqual(1, True)
        self.assertIsNot(a_positive_integer, True)
        self.assertTrue(bool(a_positive_integer))
        self.assertTrue(a_positive_integer)


# NOTES
# the value of True is 1
# bool(a dictionary with things) is True
# bool(a set with things) is True
# bool(a list with things) is True
# bool(a tuple with things) is True
# bool(a string with things) is True
# bool(a positive number) is True
# bool(a negative number) is True
# True is True
# True is an integer
# True is a boolean
# True is NOT False
# the value of False is 0
# bool(the empty dictionary) is False
# bool(the empty set) is False
# bool(the empty list) is False
# bool(the empty tuple) is False
# bool(the empty string) is False
# bool(zero) is False
# bool(None) is False
# False is False
# False is an integer
# False is a boolean
# False is NOT True


# Exceptions seen
# AssertionError