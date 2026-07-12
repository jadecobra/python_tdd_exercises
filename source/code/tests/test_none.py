import unittest


class TestNone(unittest.TestCase):

    def test_what_is_none(self):
        self.assertIs(None, None)
        self.assertIsNone(None)

    def test_none_v_boolean(self):
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsInstance(False, bool)
        self.assertIsInstance(True, bool)
        self.assertNotIsInstance(None, bool)

    def test_none_v_integer(self):
        self.assertIsNotNone(-1)
        self.assertIsNotNone(0)
        self.assertIsNotNone(1)
        self.assertIsInstance(-1, int)
        self.assertIsInstance(0, int)
        self.assertIsInstance(1, int)
        self.assertNotIsInstance(None, int)

    def test_none_v_float(self):
        self.assertIsNotNone(-0.1)
        self.assertIsNotNone(0.0)
        self.assertIsNotNone(0.1)
        self.assertIsInstance(-0.1, float)
        self.assertIsInstance(0.0, float)
        self.assertIsInstance(0.1, float)
        self.assertNotIsInstance(None, float)

    def test_none_v_string(self):
        self.assertIsNotNone('')
        self.assertIsNotNone("characters")
        self.assertIsInstance("", str)
        self.assertIsInstance('characters', str)
        self.assertNotIsInstance(None, str)

    def test_none_v_tuple(self):
        self.assertIsNotNone(())
        self.assertIsNotNone((0, 1, 2, 'n'))
        self.assertIsInstance((), tuple)
        self.assertIsInstance((0, 1, 2, 'n'), tuple)
        self.assertNotIsInstance(None, tuple)

    def test_none_v_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([0, 1, 2, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([0, 1, 2, 'n'], list)
        self.assertNotIsInstance(None, list)

    def test_none_v_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({0, 1, 2, 'n'})
        self.assertIsInstance({0, 1, 2, 'n'}, set)
        self.assertNotIsInstance(None, set)

    def test_none_v_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance(
            {'key': 'value'}, dict
        )
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


# Exceptions seen
# AssertionError