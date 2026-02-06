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


class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))
        self.assertFalse(src.truth_table.contradiction(False, False))

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))
        self.assertFalse(src.truth_table.logical_conjunction(False, False))

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))
        self.assertFalse(src.truth_table.project_second(False, False))

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))


# Exceptions seen
# AssertionError
# AttributeError
# TypeError