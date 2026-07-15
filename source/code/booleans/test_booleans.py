import unittest


class TestBooleans(unittest.TestCase):

    def test_what_is_false(self):
        self.assertIsInstance(False, (bool, int))
        self.assertNotIsInstance(
            False,
            (
                float, tuple, str,
                list, set, dict
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
                list, set, dict
            )
        )
        self.assertIs(True, True)
        self.assertIs(bool(True), True)
        self.assertTrue(bool(True))
        self.assertTrue(True)

    def test_is_none_falsy_or_truthy(self):
        self.assertFalse(bool(None))
        self.assertFalse(None)
        self.assertIsNot(None, False)

    def test_is_an_integer_falsy_or_truthy(self):
        a_negative_integer = -1
        self.assertTrue(bool(a_negative_integer))
        self.assertTrue(a_negative_integer)
        self.assertIsNot(a_negative_integer, True)

        self.assertFalse(bool(0))
        self.assertFalse(0)
        self.assertIsNot(0, False)

        a_positive_integer = 1
        self.assertTrue(bool(a_positive_integer))
        self.assertTrue(a_positive_integer)
        self.assertIsNot(a_positive_integer, True)

    def test_is_a_float_falsy_or_truthy(self):
        a_negative_float = -0.1
        self.assertTrue(bool(a_negative_float))
        self.assertTrue(a_negative_float)
        self.assertIsNot(a_negative_float, True)

        self.assertFalse(bool(0.0))
        self.assertFalse(0.0)
        self.assertIsNot(0.0, False)

        a_positive_float = 0.1
        self.assertTrue(bool(a_positive_float))
        self.assertTrue(a_positive_float)
        self.assertIsNot(a_positive_float, True)

    def test_is_a_string_falsy_or_truthy(self):
        self.assertFalse(bool(str()))
        self.assertFalse(str())
        self.assertIsNot(str(), False)

        a_string = "string with things"
        self.assertTrue(bool(a_string))
        self.assertTrue(a_string)
        self.assertIsNot(a_string, True)

    def test_is_a_tuple_falsy_or_truthy(self):
        self.assertFalse(bool(tuple()))
        self.assertFalse(tuple())
        self.assertIsNot(tuple(), False)

        a_tuple = (0, 1, 2, 'n')
        self.assertTrue(bool(a_tuple))
        self.assertTrue(a_tuple)
        self.assertIsNot(a_tuple, True)

    def test_is_a_list_falsy_or_truthy(self):
        self.assertFalse(bool(list()))
        self.assertFalse(list())
        self.assertIsNot(list(), False)

        a_list = [0, 1, 2, 'n']
        self.assertTrue(bool(a_list))
        self.assertTrue(a_list)
        self.assertIsNot(a_list, True)

    def test_is_a_set_falsy_or_truthy(self):
        self.assertFalse(bool(set()))
        self.assertFalse(set())
        self.assertIsNot(set(), False)

        a_set = {0, 1, 2, 'n'}
        self.assertTrue(bool(a_set))
        self.assertTrue(a_set)
        self.assertIsNot(a_set, True)

    def test_is_a_dictionary_falsy_or_truthy(self):
        self.assertFalse(bool(dict()))
        self.assertFalse(dict())
        self.assertIsNot(dict(), False)

        a_dictionary = {'key': 'value'}
        self.assertTrue(bool(a_dictionary))
        self.assertTrue(a_dictionary)
        self.assertIsNot(a_dictionary, True)

    def test_the_value_of_false(self):
        self.assertEqual(False+1, 1)
        self.assertEqual(False-1, -1)
        self.assertEqual(False*1, 0)

        # raises ZeroDivisionError
        # 1 / False

    def test_the_value_of_true(self):
        self.assertEqual(True+1, 2)
        self.assertEqual(True-1, 0)
        self.assertEqual(True*1, 1)
        self.assertEqual(True/1, 1)


# NOTES
# bool(a dictionary with things) is True
# bool(a set with things) is True
# bool(a list with things) is True
# bool(a tuple with things) is True
# bool(a string with things) is True
# bool(a positive number) is True
# bool(a negative number) is True
# True is True
# True is an integer
# the value of True is 1
# True is a boolean
# True is NOT False
# bool(the empty dictionary) is False
# bool(the empty set) is False
# bool(the empty list) is False
# bool(the empty tuple) is False
# bool(the empty string) is False
# bool(zero) is False
# bool(None) is False
# False is False
# False is an integer
# the value of False is 0
# False is a boolean
# False is NOT True


# Exceptions seen
# AssertionError
# ZeroDivisionError