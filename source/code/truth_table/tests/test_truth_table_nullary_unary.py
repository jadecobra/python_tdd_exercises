import unittest
import src.truth_table


class TestNullaryOperations(unittest.TestCase):

    def test_logical_true(self):
        self.assertTrue(src.truth_table.logical_true())

    def test_logical_false(self):
        self.assertFalse(src.truth_table.logical_false())


class TestUnaryOperations(unittest.TestCase):

    def test_logical_identity(self):
        self.assertTrue(src.truth_table.logical_identity(True))
        self.assertFalse(src.truth_table.logical_identity(False))

    def test_logical_negation_aka_not(self):
        self.assertFalse(src.truth_table.logical_negation(True))
        self.assertTrue(src.truth_table.logical_negation(False))


# Exceptions seen
# AssertionError
# AttributeError
# TypeError