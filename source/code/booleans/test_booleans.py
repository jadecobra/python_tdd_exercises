import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, (bool, int))
        self.assertNotIsInstance(
            False,
            (
                float, tuple, str,
                list, set, dict,
            )
        )
        self.assertIs(False, False)
        self.assertIs(bool(False), False)
        self.assertFalse(bool(False))
        self.assertFalse(False)

    def test_what_is_true(self):
        self.assertIsInstance(True, (bool, int))
        self.assertNotIsInstance(
            True,
            (
                float, tuple, str,
                list, set, dict,
            )
        )
        self.assertIs(True, True)
        self.assertIs(bool(True), True)
        self.assertTrue(bool(True))
        self.assertTrue(True)

    def assert_is_not_the_same_as_false_or_true(self, an_object):
        self.assertNotEqual(an_object, False)
        self.assertIsNot(an_object, False)
        self.assertNotEqual(an_object, True)
        self.assertIsNot(an_object, True)

    def assert_is_falsy(self, an_object):
        self.assert_is_not_the_same_as_false_or_true(an_object)
        self.assertFalse(bool(an_object))
        self.assertFalse(an_object)

    def assert_is_truthy(self, an_object):
        self.assert_is_not_the_same_as_false_or_true(an_object)
        self.assertTrue(bool(an_object))
        self.assertTrue(an_object)

    def test_is_none_falsy_or_truthy(self):
        self.assert_is_falsy(None)

    def test_is_an_integer_falsy_or_truthy(self):
        self.assert_is_truthy(-1)

        self.assertEqual(0, False)
        self.assertIsNot(0, False)
        self.assertNotEqual(0, True)
        self.assertIsNot(0, True)
        self.assertFalse(bool(0))
        self.assertFalse(0)

        a_positive_integer = 1
        self.assertNotEqual(a_positive_integer, False)
        self.assertIsNot(a_positive_integer, False)
        self.assertEqual(1, True)
        self.assertIsNot(a_positive_integer, True)
        self.assertTrue(bool(a_positive_integer))
        self.assertTrue(a_positive_integer)

    def test_is_a_float_falsy_or_truthy(self):
        self.assert_is_truthy(-0.1)

        self.assertEqual(0.0, False)
        self.assertIsNot(0.0, False)
        self.assertNotEqual(0.0, True)
        self.assertIsNot(0.0, True)
        self.assertFalse(bool(0.0))
        self.assertFalse(0.0)

        self.assert_is_truthy(0.1)

    def test_is_a_string_falsy_or_truthy(self):
        self.assert_is_falsy(str())
        self.assert_is_truthy('a string with things')

    def test_is_a_tuple_falsy_or_truthy(self):
        self.assert_is_falsy(tuple())
        self.assert_is_truthy((0, 1, 2, 'n'))

    def test_is_a_list_falsy_or_truthy(self):
        self.assert_is_falsy(list())
        self.assert_is_truthy([0, 1, 2, 'n'])

    def test_is_a_set_falsy_or_truthy(self):
        self.assert_is_falsy(set())
        self.assert_is_truthy({0, 1, 2, 'n'})

    def test_is_a_dictionary_falsy_or_truthy(self):
        self.assert_is_falsy(dict())
        self.assert_is_truthy({'key': 'value'})


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