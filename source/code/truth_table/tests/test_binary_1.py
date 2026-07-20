import src.truth_table
import unittest


class TestBinaryOperations(unittest.TestCase):

    def test_contradiction(self):
        contradiction = src.truth_table.contradiction
        self.assertFalse(contradiction(True, True))
        self.assertFalse(contradiction(True, False))
        self.assertFalse(contradiction(False, True))
        self.assertFalse(contradiction(False, False))

    def test_logical_conjunction(self):
        logical_conjunction = (
            src.truth_table.logical_conjunction
        )
        self.assertTrue(logical_conjunction(True, True))
        self.assertFalse(logical_conjunction(True, False))
        self.assertFalse(logical_conjunction(False, True))
        self.assertFalse(logical_conjunction(False, False))

    def test_project_second(self):
        project_second = src.truth_table.project_second
        self.assertTrue(project_second(True, True))
        self.assertFalse(project_second(True, False))
        self.assertTrue(project_second(False, True))
        self.assertFalse(project_second(False, False))

    def test_converse_non_implication(self):
        converse_non_implication = (
            src.truth_table.converse_non_implication
        )
        self.assertFalse(converse_non_implication(True, True))
        self.assertFalse(converse_non_implication(True, False))
        self.assertTrue(converse_non_implication(False, True))
        self.assertFalse(converse_non_implication(False, False))


# Exceptions seen
# AttributeError
# TypeError
# AssertionError