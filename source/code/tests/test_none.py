import unittest


class TestNone(unittest.TestCase):

    def test_what_is_none(self):
        self.assertIsNone(None)

    def test_is_none_a_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)
        self.assertNotIsInstance(None, bool)

    def test_is_none_an_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)
        self.assertNotIsInstance(None, int)

    def test_is_none_a_float(self):
        self.assertIsNotNone(-1.2)
        self.assertIsNotNone(3.4)
        self.assertIsInstance(-1.2, float)
        self.assertIsInstance(3.4, float)
        self.assertNotIsInstance(None, float)

    def test_is_none_a_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("text")
        self.assertIsInstance('', str)
        self.assertIsInstance("text", str)
        self.assertNotIsInstance(None, str)

    def test_is_none_a_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((1, 2, 3, 'n'))
        self.assertIsInstance((), tuple)
        self.assertIsInstance((1, 2, 3, 'n'), tuple)

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertNotIsInstance(None, list)

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)
        self.assertNotIsInstance(None, set)

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)
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
