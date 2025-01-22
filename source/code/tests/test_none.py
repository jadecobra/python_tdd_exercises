import unittest


class TestNone(unittest.TestCase):

    def test_what_is_none(self):
        self.assertIsNone(None)

    def test_is_none_a_boolean(self):
        self.assertNotIsInstance(None, bool)

    def test_is_none_an_integer(self):
        self.assertNotIsInstance(None, int)

    def test_is_none_a_float(self):
        self.assertNotIsInstance(None, float)

    def test_is_none_a_string(self):
        self.assertNotIsInstance(None, str)

    def test_is_none_a_tuple(self):
        self.assertNotIsInstance(None, tuple)

    def test_is_none_a_list(self):
        self.assertNotIsInstance(None, list)

    def test_is_none_a_set(self):
        self.assertNotIsInstance(None, set)

    def test_is_none_a_dictionary(self):
        self.assertNotIsInstance(None, dict)


# NOTES
# None is NOT a dictionary
# None is NOT a set
# None is NOT a list
# None is NOT a tuple
# None is NOT a string
# None is NOT a float
# None is NOT an integer
# None is NOT a boolean
# None is None


# Exceptions Encountered
# AssertionError
